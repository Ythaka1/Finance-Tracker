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


initialize_db()
add_transaction()
