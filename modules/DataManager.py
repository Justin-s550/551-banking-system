"""
Handles loading and saving JSON data.
"""

import json


def load_transactions(file_path):
    """Load transactions from JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print("Error: File not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def save_transactions(file_path, data):
    """Save transactions to JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
