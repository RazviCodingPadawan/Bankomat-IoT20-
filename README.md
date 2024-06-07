# Bankomat IoT20

This project is a simple banking system simulation implemented in Python. It allows users to create accounts, log in, perform transactions (withdrawals and deposits), and view account balances and transaction logs. The account and transaction data are stored in text files.

## Features

### Menu A
- **Create account**: Allows the user to create a new account.
- **Log in to account**: Allows the user to log in to an existing account.
- **Exit**: Exits the program.

### Menu B (Logged in users)
- **Withdraw money**: Allows the user to withdraw money from their account.
- **Deposit money**: Allows the user to deposit money into their account.
- **Show balance**: Displays the current balance of the user's account.
- **List transactions**: Lists all transactions (deposits and withdrawals) made by the user.
- **Log out**: Logs the user out and returns to Menu A.

## Additional Features for High Grades
- **Transaction logging**: Every deposit and withdrawal is logged with the date, amount, and type of transaction.
- **Persistent storage**: Account details and transaction logs are stored in files and loaded when the program starts.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/RazviCodingPadawan/Bankomat_IoT20.git
    cd Bankomat_IoT20
    ```

2. Run the program:
    ```sh
    python bankomat.py
    ```

## File Structure

- `bankomat.py`: The main program file.
- `accounts.txt`: Stores account numbers and balances.
- `transactions.txt`: Stores transaction logs for each account.

## How It Works

### Account Creation
- User inputs an account number.
- If the account number is already taken, an error message is displayed.
- Otherwise, a new account is created with a balance of 0.

### Login
- User inputs an account number.
- If the account exists, the user is logged in and taken to Menu B.
- Otherwise, an error message is displayed.

### Withdraw Money
- User inputs the amount to withdraw.
- If the amount is greater than the current balance, an error message is displayed.
- Otherwise, the amount is deducted from the balance and a transaction is logged.

### Deposit Money
- User inputs the amount to deposit.
- The amount is added to the balance and a transaction is logged.

### Show Balance
- The current balance of the account is displayed.

### List Transactions
- All transactions for the logged-in account are displayed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
