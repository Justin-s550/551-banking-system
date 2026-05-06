"""
test_bank.py - Pytest test cases for the banking system.
Tests Account, FraudDetector, analytics functions, and data_manager.
"""

import os
import json
import pytest
from modules.account import Account
from modules.detection import FraudDetector
from modules.analytics import average_transaction, find_large_transactions, transaction_summary
from modules.DataManager import load_transactions, save_transactions


# ─────────────────────────────────────────────
# Account Tests
# ─────────────────────────────────────────────

def test_deposit():
    """Test that deposit increases balance correctly."""
    acc = Account("A001", "mike", "pass123", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw():
    """Test that withdrawal decreases balance correctly."""
    acc = Account("A002", "john", "pass123", 200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_invalid_deposit():
    """Test that depositing a negative amount raises ValueError."""
    acc = Account("A003", "test", "pass123", 100)
    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_invalid_withdraw_overdraft():
    """Test that withdrawing more than balance raises ValueError."""
    acc = Account("A004", "test", "pass123", 100)
    with pytest.raises(ValueError):
        acc.withdraw(500)


def test_invalid_withdraw_negative():
    """Test that withdrawing a negative amount raises ValueError."""
    acc = Account("A005", "test", "pass123", 100)
    with pytest.raises(ValueError):
        acc.withdraw(-50)


def test_transfer():
    """Test that transfer moves money correctly between two accounts."""
    acc1 = Account("A006", "alice", "pass123", 500)
    acc2 = Account("A007", "bob", "pass123", 100)
    acc1.transfer(acc2, 200)
    assert acc1.balance == 300
    assert acc2.balance == 300


def test_transfer_no_double_log():
    """Test that transfer does not double-log the transaction."""
    acc1 = Account("A008", "alice", "pass123", 500)
    acc2 = Account("A009", "bob", "pass123", 100)
    acc1.transfer(acc2, 200)
    # acc1 should only have ONE withdraw entry, not two
    withdraw_entries = [t for t in acc1.transactions if t[0] == "withdraw"]
    assert len(withdraw_entries) == 1


def test_add_operator():
    """Test that __add__ operator deposits correctly."""
    acc = Account("A010", "test", "pass123", 100)
    acc + 50
    assert acc.balance == 150


def test_str_operator():
    """Test that __str__ returns a non-empty string with account info."""
    acc = Account("A011", "test", "pass123", 100)
    result = str(acc)
    assert "A011" in result
    assert "test" in result


# ─────────────────────────────────────────────
# FraudDetector Tests
# ─────────────────────────────────────────────

def test_fraud_large_transaction():
    """Test that a transaction above threshold is flagged."""
    acc = Account("A012", "test", "pass123", 5000)
    detector = FraudDetector(threshold=1000)
    flagged = detector.check_transaction(acc, 1500)
    assert flagged is True


def test_fraud_normal_transaction():
    """Test that a transaction below threshold is not flagged."""
    acc = Account("A013", "test", "pass123", 5000)
    detector = FraudDetector(threshold=1000)
    flagged = detector.check_transaction(acc, 200)
    assert flagged is False


def test_fraud_suspicious_account_tracked():
    """Test that flagged account ID is stored in suspicious_accounts."""
    acc = Account("A014", "test", "pass123", 5000)
    detector = FraudDetector(threshold=1000)
    detector.check_transaction(acc, 2000)
    assert "A014" in detector.suspicious_accounts


def test_failed_login_tracking():
    """Test that 3 failed logins triggers a suspicious flag."""
    detector = FraudDetector()
    detector.track_failed_login("hacker")
    detector.track_failed_login("hacker")
    result = detector.track_failed_login("hacker")
    assert result is True


def test_failed_login_under_limit():
    """Test that fewer than 3 failed logins does not trigger flag."""
    detector = FraudDetector()
    detector.track_failed_login("user")
    result = detector.track_failed_login("user")
    assert result is False


# ─────────────────────────────────────────────
# Analytics Tests
# ─────────────────────────────────────────────

def test_average_transaction():
    """Test average transaction calculation."""
    transactions = [("deposit", 100), ("withdraw", 200), ("deposit", 300)]
    avg = average_transaction(transactions)
    assert avg == 200.0


def test_average_transaction_empty():
    """Test average transaction with empty list returns 0."""
    avg = average_transaction([])
    assert avg == 0


def test_find_large_transactions():
    """Test that only transactions above limit are returned."""
    transactions = [("deposit", 500), ("withdraw", 1500), ("transfer", 2000)]
    large = find_large_transactions(transactions, 1000)
    assert len(large) == 2
    assert all(t[1] > 1000 for t in large)


def test_transaction_summary():
    """Test transaction summary returns correct total and count."""
    transactions = [("deposit", 100), ("deposit", 200), ("withdraw", 50)]
    summary = transaction_summary(transactions)
    assert summary["total"] == 350
    assert summary["count"] == 3


# ─────────────────────────────────────────────
# Data Manager Tests
# ─────────────────────────────────────────────

def test_save_and_load_transactions(tmp_path):
    """Test that transactions can be saved and reloaded from JSON."""
    data = [
        {"account": "A001", "type": "deposit", "amount": 500},
        {"account": "A001", "type": "withdraw", "amount": 100}
    ]
    file_path = str(tmp_path / "test_transactions.json")
    save_transactions(file_path, data)
    loaded = load_transactions(file_path)
    assert loaded == data


def test_load_missing_file():
    """Test that loading a missing file returns an empty list."""
    result = load_transactions("data/nonexistent_file.json")
    assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
