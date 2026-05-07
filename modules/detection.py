"""
Fraud detection system for monitoring suspicious activity.
"""

import time
import matplotlib.pyplot as plt
from datetime import datetime

class FraudDetector:
    def __init__(self, threshold=1000):
        """Initialize fraud detector with threshold."""
        self.threshold = threshold
        self.suspicious_accounts = set() # set (mutable type)
        self.failed_logins = {}  # dict (mutable type)

    def check_transaction(self, account, amount):
        """Check if transaction exceeds threshold."""
        if amount > self.threshold:
            self.suspicious_accounts.add(account.account_id)
            return True
        return False

    def track_failed_login(self, username):
        """Track failed login attempts."""
        current_time = time.time()

        if username not in self.failed_logins:
            self.failed_logins[username] = []

        self.failed_logins[username].append(current_time)

        # If 3 attempts in short time → suspicious
        if len(self.failed_logins[username]) >= 3:
            return True

        return False
    
    def plot_failed_logins(self):
        if not self.failed_logins:
            print("No failed logins to display.")
            return

        for username, timestamps in self.failed_logins.items():
            times = [datetime.fromtimestamp(t).strftime('%I:%M:%S %p') for t in timestamps]
            counts = list(range(1, len(timestamps) + 1))
            plt.bar(times, counts, label=username)

        plt.xlabel('Time')
        plt.ylabel('Number of Attempts')
        plt.title('Failed Login Attempts')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()