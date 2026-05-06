"""
Account class representing a bank account.
Handles deposits, withdrawals, and transfers.
"""

class Account:
    """
    Represents a bank account with basic banking operations.
 
    Attributes:
        account_id (str): Unique identifier for the account.
        username (str): Account holder's username.
        password (str): Account holder's password.
        balance (float): Current account balance.
        transactions (list): List of tuples recording transaction history.
    """

    def __init__(self, account_id, username, password, balance=0):
        """Initialize account with ID, username, password, and balance."""
        self.account_id = account_id
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = []  # list (mutable type)

    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.transactions.append(("withdraw", amount))

    def transfer(self, other_account, amount):
        """Transfer money to another account."""
        self.withdraw(amount)
        other_account.deposit(amount)

    def __add__(self, amount):
        """Overload + operator for deposits."""
        self.deposit(amount)
        return self

    def __str__(self):
        """Return account details."""
        return (
            f"Account ID: {self.account_id}\n"
            f"Username:   {self.username}\n"
            f"Balance:    ${self.balance:.2f}\n"
            f"Transactions: {len(self.transactions)}"
        )
