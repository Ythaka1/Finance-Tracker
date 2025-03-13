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
        # Converting the  date format
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
    try:
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        transactions = session.query(Transaction).filter(Transaction.date >= start_date, Transaction.date <= end_date).all()

        if not transactions:
            print("⚠️ No transactions found in the given date range.")
        else:
            for t in transactions:
                print(f"{t.date.strftime('%d-%m-%Y')}: {t.amount} - {t.category} ({t.description})")
        return transactions
    except Exception as e:
        print(f"❌ Error retrieving transactions: {e}")
        return []
    
def main():
    initialize_db()
    while True:
        print("\n1. Add a new transaction") 
        print("2, View transaction within a date range")
        print("3.Exit")
        choice = input("Enter your choice (1-3):")  
        
     
        if choice == "1":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            amount = float(input("Enter amount: "))
            category = input("Enter category (Income/Expense): ")
            description = input("Enter description: ")
            add_transaction(date, amount, category, description)
        elif choice == "2":
            start_date_str = input("Enter the start date (YYYY-MM-DD): ")
            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            transactions = get_transactions(start_date, end_date)
        elif choice == "3":
            print("Exiting.....") 
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3 PLZ" )   
         
        
        
if __name__ == "__main__":
    main()         
                    