"""
Analytics functions for transaction data.
"""

import numpy as np


def average_transaction(transactions):
    """Return average transaction amount."""
    if not transactions:
        return 0

    amounts = [t[1] for t in transactions]  # list comprehension
    return np.mean(amounts)


def find_large_transactions(transactions, limit):
    """Return transactions above a certain limit."""
    return list(filter(lambda t: t[1] > limit, transactions))


def transaction_summary(transactions):
    """Return total and count of transactions."""
    total = sum(t[1] for t in transactions)  # generator expression
    count = len(transactions)

    return {"total": total, "count": count}
