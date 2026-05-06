"""
main.py - Banking System with Fraud Detection
Entry point for the banking simulation program.
Handles user interaction, account management, and fraud detection.
"""

import json
import os
from modules.account import Account
from modules.detection import FraudDetector
from modules.analytics import average_transaction, find_large_transactions, transaction_summary
from modules.DataManager import load_transactions, save_transactions

# File path for storing account data
ACCOUNTS_FILE = "data/accounts.json"
TRANSACTIONS_FILE = "data/transactions.json"


def load_accounts(file_path):
    """
    Load all accounts from a JSON file.

    Args:
        file_path (str): Path to the accounts JSON file.

    Returns:
        dict: Dictionary of account_id -> Account objects.
    """
    accounts = {}

    # Exception handling for file loading errors
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
            for acc_id, info in data.items():
                acc = Account(
                    account_id=acc_id,
                    username=info["username"],
                    password=info["password"],
                    balance=info["balance"]
                )
                # Reload saved transactions as tuples
                acc.transactions = [tuple(t) for t in info.get("transactions", [])]
                accounts[acc_id] = acc
    except FileNotFoundError:
        print("No existing accounts file found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading accounts file. Starting fresh.")

    return accounts


def save_accounts(file_path, accounts):
    """
    Save all accounts to a JSON file.

    Args:
        file_path (str): Path to save the accounts JSON file.
        accounts (dict): Dictionary of account_id -> Account objects.
    """
    data = {}
    for acc_id, acc in accounts.items():
        data[acc_id] = {
            "username": acc.username,
            "password": acc.password,
            "balance": acc.balance,
            "transactions": [list(t) for t in acc.transactions]
        }

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def create_account(accounts):
    """
    Prompt user to create a new bank account.

    Args:
        accounts (dict): Existing accounts dictionary to add to.

    Returns:
        Account: The newly created Account object.
    """
    print("\n--- Create New Account ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Generate a simple account ID
    account_id = f"A{str(len(accounts) + 1).zfill(3)}"

    # Check for duplicate usernames
    for acc in accounts.values():
        if acc.username == username:
            print("Username already exists. Please try again.")
            return None

    new_account = Account(account_id, username, password)
    accounts[account_id] = new_account
    print(f"\nAccount created! Your account ID is: {account_id}")
    return new_account


def login(accounts, fraud_detector):
    """
    Handle user login with failed attempt tracking.

    Args:
        accounts (dict): Dictionary of all accounts.
        fraud_detector (FraudDetector): The fraud detection instance.

    Returns:
        Account or None: The logged-in Account, or None if login fails.
    """
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Loop through accounts to find matching credentials
    for acc in accounts.values():
        if acc.username == username and acc.password == password:
            print(f"\nWelcome back, {username}!")
            return acc

    # Track failed login attempt
    flagged = fraud_detector.track_failed_login(username)
    if flagged:
        print(f"WARNING: Multiple failed login attempts detected for '{username}'.")
    else:
        print("Invalid username or password.")

    return None


def account_menu(account, accounts, fraud_detector):
    """
    Display and handle the main account menu for a logged-in user.

    Args:
        account (Account): The currently logged-in account.
        accounts (dict): All accounts in the system.
        fraud_detector (FraudDetector): The fraud detection instance.
    """
    while True:
        print("\n--- Account Menu ---")
        print("1. View Account Info")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction Summary")
        print("6. Run Fraud Analysis")
        print("7. Logout")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            # Uses __str__ overload
            print(f"\n{account}")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                # Uses __add__ operator overload
                account + amount
                flagged = fraud_detector.check_transaction(account, amount)
                if flagged:
                    print(f"WARNING: Large deposit of ${amount} flagged as suspicious.")
                else:
                    print(f"Successfully deposited ${amount}.")
                save_accounts(ACCOUNTS_FILE, accounts)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)
                flagged = fraud_detector.check_transaction(account, amount)
                if flagged:
                    print(f"WARNING: Large withdrawal of ${amount} flagged as suspicious.")
                else:
                    print(f"Successfully withdrew ${amount}.")
                save_accounts(ACCOUNTS_FILE, accounts)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            target_id = input("Enter target account ID: ").strip()
            if target_id not in accounts:
                print("Account not found.")
            else:
                try:
                    amount = float(input("Enter transfer amount: $"))
                    account.transfer(accounts[target_id], amount)
                    flagged = fraud_detector.check_transaction(account, amount)
                    if flagged:
                        print(f"WARNING: Large transfer of ${amount} flagged as suspicious.")
                    else:
                        print(f"Successfully transferred ${amount} to {target_id}.")
                    save_accounts(ACCOUNTS_FILE, accounts)
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "5":
            # Use enumerate() to display transaction history with index
            print("\n--- Transaction History ---")
            if not account.transactions:
                print("No transactions yet.")
            else:
                for i, transaction in enumerate(account.transactions, start=1):
                    print(f"  {i}. {transaction[0].capitalize()}: ${transaction[1]}")

                avg = average_transaction(account.transactions)
                summary = transaction_summary(account.transactions)
                print(f"\nTotal Transactions: {summary['count']}")
                print(f"Total Amount:       ${summary['total']:.2f}")
                print(f"Average Amount:     ${avg:.2f}")

        elif choice == "6":
            print("\n--- Fraud Analysis ---")
            large = find_large_transactions(account.transactions, fraud_detector.threshold)

            # List comprehension to extract flagged amounts
            flagged_amounts = [t[1] for t in large]

            if flagged_amounts:
                print(f"Suspicious transactions found (above ${fraud_detector.threshold}):")
                for i, transaction in enumerate(large, start=1):
                    print(f"  {i}. {transaction[0].capitalize()}: ${transaction[1]}")
            else:
                print("No suspicious transactions detected.")

            if account.account_id in fraud_detector.suspicious_accounts:
                print("NOTE: This account has been flagged for suspicious activity.")

        elif choice == "7":
            print("Logged out successfully.")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    """
    Main entry point for the banking system.
    Loads accounts, runs the login/create loop, and launches the account menu.
    """
    print("=" * 40)
    print("  Welcome to the Banking System")
    print("=" * 40)

    # Load existing accounts and transactions
    accounts = load_accounts(ACCOUNTS_FILE)
    fraud_detector = FraudDetector(threshold=1000)

    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            account = login(accounts, fraud_detector)
            if account:
                account_menu(account, accounts, fraud_detector)

        elif choice == "2":
            new_acc = create_account(accounts)
            if new_acc:
                save_accounts(ACCOUNTS_FILE, accounts)

        elif choice == "3":
            print("\nThank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
