# Bank Transaction Management with Fraud Detection

Team Members: 
Justin Phan, email: jphan1@stevens.edu, Stevens ID: 20011192 
Diego Giraldo Tabares, email: dgiraldo@stevens.edu, Stevens ID: 20014654 
Michael Altamirano, email: maltamr@stevens.edu, Stevens ID: 20011442 

Project Description
This project simulates a banking system with fraud detection. Users can create accounts, deposit, withdraw, and transfer money. The program analyzes transaction patterns to detect suspicious activity such as large transfers or repeated login attempts.

Libraries Used
- numpy
- matplotlib
- json
- time
- pytest

File Structure
main.ipynb – main program
modules/account.py – account class
modules/fraud_detection.py – fraud detection class
modules/data_manager.py – handles JSON data
modules/analytics.py – transaction statistics
tests/test_bank.py – pytest test cases

How to Run

1 Install dependencies

pip install -r requirements.txt

2 Run the notebook

jupyter notebook main.ipynb
