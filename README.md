# Personal Finance Tracker - README

## Introduction
The Personal Finance Tracker is a Command Line Interface (CLI) application that allows users to log, categorize, and review their financial transactions. It helps users track income and expenses while providing summaries for better financial management.

## Prerequisites
Before using this application, ensure you have the following installed:
- Python 3.x
- VS Code (Recommended for development and database management)
- SQLite database client (Install from VS Code Extensions)

## Setup Instructions
1. **Clone the Repository** (if applicable)
   ```bash
   git clone <repository_url>
   cd Finance-Tracker
   ```
2. **Create a Virtual Environment** (Optional but recommended)
   ```
   ```
3. **Install Dependencies**
      ??????
   ```
4. **Run the Application**
   ```bash
   python main.py
   ```

## How to Use
1. **Adding a Transaction**
   - Select option `1` from the menu.
   - Enter the date (dd-mm-yyyy) or press Enter for today's date.
   - Enter the transaction amount.
   - Choose a category ('I' for Income, 'E' for Expense).
   - Optionally, enter a description.
   - The transaction will be saved in the database.

2. **Viewing Transactions in a Date Range**
   - Select option `2` from the menu.
   - Enter the start and end dates (dd-mm-yyyy format).
   - The program will display all transactions within the given range along with a financial summary.

3. **Exiting the Program**
   - Select option `3` and confirm to exit.

## Database Management
- The application uses SQLite to store transactions in `finance.db`.
- To view or manage the database, install a **SQLite database client** from the VS Code Extensions Marketplace.
- Open the `finance.db` file within the extension to browse and query data.

## Troubleshooting
- Ensure Python is installed and correctly set up in your system.
- If you get database errors, delete `finance.db` and restart the program to reinitialize the database.


## Contributing
Feel free to modify and improve the application. Pull requests are welcome!

## License
This project is open-source and free to use Thank U for using the DEMO.

