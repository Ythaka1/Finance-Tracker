# Personal Finance Tracker - CLI Application

## Introduction
This Personal Finance Tracker is a simple command-line interface (CLI) application that helps users log and manage their financial transactions. It allows users to:
- Add new transactions (income or expense)
- View transactions within a specified date range
- Get a summary of total income, expenses, and net savings

## Requirements
- Python 3.x installed on your system
- Required Python libraries: `SQLAlchemy`
- A virtual environment (recommended)

## Setup Instructions
### 1. Clone or Download the Project
If you haven't already, clone the project repository.

### 2. Set Up a Virtual Environment (Recommended)
It is best to create a virtual environment for managing dependencies.
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
(`pip install sqlalchemy`)

### 4. Run the Application
To start the finance tracker, run:
```
python main.py
```

## How to Use the Application
Once the application starts, you will see a menu:
```
1. Add a new transaction
2. View transactions within a date range
3. Exit
```

### Adding a New Transaction
1. Select `1` from the menu.
2. Enter the date in `dd-mm-yyyy` format or press Enter for today’s date.
3. Enter the transaction amount (must be a positive number).
4. Choose a category:
   - `I` for Income
   - `E` for Expense
5. Enter an optional description.
6. The transaction is saved, and you will see a confirmation message.

### Viewing Transactions in a Date Range
1. Select `2` from the menu.
2. Enter the start date and end date in `dd-mm-yyyy` format.
3. The application will display all transactions within the given date range, including a summary of total income, expenses, and net savings.

### Exiting the Application
- Select `3` from the menu  when prompted.

## Database
The application uses an SQLite database (`finance.db`) to store transactions.
- Transactions are saved automatically.
- The database is created when the app runs for the first time.

## Troubleshooting
- If an error occurs, ensure you have Python 3 installed.
- Check that you entered dates in `dd-mm-yyyy` format.
- Ensure SQLAlchemy is installed (`pip install sqlalchemy`).

## Future Enhancements
- Implement an option to delete transactions.
- Add data visualization features .
- Improve user interface.

---
Thank you for using the Personal Finance Tracker! 🚀

