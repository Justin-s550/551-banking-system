"""
Pytest test cases for banking system.
"""

from modules.account import Account


def test_deposit():
    acc = Account("A001", "Mike", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw():
    acc = Account("A002", "John", 200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_invalid_deposit():
    acc = Account("A003", "Test", 100)

    try:
        acc.deposit(-10)
    except ValueError:
        assert True
    else:
        assert False
