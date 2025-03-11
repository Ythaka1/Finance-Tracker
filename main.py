from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

db_url = "sqlite:///finance.db"

Base = declarative_base()
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind = engine)

#THe main class(Transaction)/model
class Transaction(Base):
    __tablename__ = "transactions"
    id          = Column(Integer, primary_key=True)
    date        = Column(Date, nullable=False)
    amount      = Column(Float, nullable= False)
    category    = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
 #Initialize database
def initialize_def():
    Base.metadata.create_all(engine)
    
# 4 adding a new transaction
def add_transaction(date,amount,category,description):
    try:
        transaction = Transaction(date=date, amount=amount, category=category, description=description)
        session.add(transaction)
        session.commit()
        print("Transaction added successfully")  
    except Exception as e:
        session.rollback()
        print(f"Error adding transaction: {e}")     