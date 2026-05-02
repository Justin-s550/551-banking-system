"""
Account class representing a bank account.
Handles deposits, withdrawals, and transfers.
"""

class Account:
    def __init__(self, account_id, username, balance=0):
        """Initialize account with ID, username, and balance."""
        self.account_id = account_id
        self.username = username
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
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.transactions.append(("withdraw", amount))

    def transfer(self, other_account, amount):
        """Transfer money to another account."""
        self.withdraw(amount)
        other_account.deposit(amount)
        self.transactions.append(("transfer", amount))

    def __add__(self, amount):
        """Overload + operator for deposits."""
        self.deposit(amount)
        return self

    def __str__(self):
        """Return account details."""
        return f"Account {self.account_id} | User: {self.username} | Balance: ${self.balance}"
