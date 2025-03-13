from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


db_url = "sqlite:///finance.db"
Base = declarative_base()
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

# Define the main Transaction class/model
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)

# Initialize db
def initialize_db():
    Base.metadata.create_all(engine)

# Adding a new transaction
def add_transaction():
    session = SessionLocal()  

    date = get_date("Enter the date (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    try:
        # Converting the date format
        formatted_date = datetime.strptime(date, "%d-%m-%Y").date()

        transaction = Transaction(
            date=formatted_date,
            amount=amount,
            category=category,
            description=description
        )

        session.add(transaction)
        session.commit()
        print("✅ Transaction added successfully.")
    
    except Exception as e:
        session.rollback()
        print(f"❌ Error adding transaction: {e}")
    
    finally:
        session.close()


def get_transactions(start_date, end_date):
    session = SessionLocal()
    try:
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()
        transactions = session.query(Transaction).filter(Transaction.date >= start_date, Transaction.date <= end_date).all()

        if not transactions:
            print("⚠️ No transactions found in the given date range.")
        else:
            for t in transactions:
                print(f"{t.date.strftime('%d-%m-%Y')}: {t.amount} - {t.category} ({t.description})")
                
            total_income = sum(t.amount for t in transactions if t.category.lower() == "income")
            total_expense = sum(t.amount for t in transactions if t.category.lower() == "expense")
            net_savings = total_income - total_expense
            
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${net_savings:.2f}")
        
        return transactions
    except Exception as e:
        print(f"❌ Error retrieving transactions: {e}")
        return []
    finally:
        session.close()
    
def main():
    initialize_db()
    while True:
        print("\n1. Add a new transaction") 
        print("2. View transactions within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")  
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            start_date_str = input("Enter the start date (dd-mm-yyyy): ")
            end_date_str = input("Enter the end date (dd-mm-yyyy): ")
            get_transactions(start_date_str, end_date_str)
        elif choice == "3":
            print("Exiting...") 
            break
        else:
            print("Invalid choice. PLZ Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
