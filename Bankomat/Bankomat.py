import os
import datetime

# Filenames
ACCOUNTS_FILE = 'accounts.txt'
TRANSACTIONS_FILE = 'transactions.txt'

# Load accounts and transactions from files
def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as f:
            for line in f:
                account, balance = line.strip().split(',')
                accounts[account] = float(balance)
    return accounts

def load_transactions():
    transactions = {}
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as f:
            for line in f:
                date, account, amount, ttype = line.strip().split(',')
                if account not in transactions:
                    transactions[account] = []
                transactions[account].append((date, float(amount), ttype))
    return transactions

# Save accounts and transactions to files
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        for account, balance in accounts.items():
            f.write(f'{account},{balance}\n')

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as f:
        for account, t_list in transactions.items():
            for t in t_list:
                f.write(f'{t[0]},{account},{t[1]},{t[2]}\n')

# Display menus
def display_menu_a():
    print("Menu A")
    print("1. Create account")
    print("2. Log in to account")
    print("3. Exit")

def display_menu_b():
    print("Menu B")
    print("1. Withdraw money")
    print("2. Deposit money")
    print("3. Show balance")
    print("4. List transactions")
    print("5. Log out")

# Account operations
def create_account(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("The account number is already taken.")
    else:
        accounts[account_number] = 0.0
        print("Account created.")
    return accounts

def login(accounts):
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Login successful.")
        return account_number
    else:
        print("Account does not exist.")
        return None

def withdraw(accounts, transactions, account_number):
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]:
        print("Insufficient balance.")
    else:
        accounts[account_number] -= amount
        transactions[account_number].append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, 'withdrawal'))
        print("Withdrawal successful.")
    return accounts, transactions

def deposit(accounts, transactions, account_number):
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number] += amount
    transactions[account_number].append((datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, 'deposit'))
    print("Deposit successful.")
    return accounts, transactions

def show_balance(accounts, account_number):
    print(f"Current balance: {accounts[account_number]}")

def list_transactions(transactions, account_number):
    print("Transactions:")
    for t in transactions[account_number]:
        print(f"Date: {t[0]}, Amount: {t[1]}, Type: {t[2]}")

# Main program
def main():
    accounts = load_accounts()
    transactions = load_transactions()
    
    while True:
        display_menu_a()
        choice = input("Choose an option: ")
        
        if choice == '1':
            accounts = create_account(accounts)
        elif choice == '2':
            account_number = login(accounts)
            if account_number:
                if account_number not in transactions:
                    transactions[account_number] = []
                while True:
                    display_menu_b()
                    choice_b = input("Choose an option: ")
                    
                    if choice_b == '1':
                        accounts, transactions = withdraw(accounts, transactions, account_number)
                    elif choice_b == '2':
                        accounts, transactions = deposit(accounts, transactions, account_number)
                    elif choice_b == '3':
                        show_balance(accounts, account_number)
                    elif choice_b == '4':
                        list_transactions(transactions, account_number)
                    elif choice_b == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
        
        save_accounts(accounts)
        save_transactions(transactions)

if __name__ == "__main__":
    main()
