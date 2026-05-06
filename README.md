# Bank Transaction Management with Fraud Detection

**Team Members:** <br>
Justin Phan, email: jphan1@stevens.edu, Stevens ID: 20011192 <br>
Diego Giraldo Tabares, email: dgiraldo@stevens.edu, Stevens ID: 20014654 <br>
Michael Altamirano, email: maltamr@stevens.edu, Stevens ID: 20011442 <br>

**Project Description:** <br>
This project simulates a banking system with fraud detection. Users can create accounts, deposit, withdraw, and transfer money. The program analyzes transaction patterns to detect suspicious activity such as large transfers or repeated login attempts.

**Libraries Used** <br> 
- numpy
- matplotlib
- json
- time
- pytest 

**File Structure** <br>
main.ipynb – main program <br>
modules/account.py – account class <br>
modules/fraud_detection.py – fraud detection class <br>
modules/data_manager.py – handles JSON data <br>
modules/analytics.py – transaction statistics <br>
tests/test_bank.py – pytest test cases <br>

**How to Run**
1. Install dependencies <br>
    pip install -r requirements.txt
2. Run the notebook <br>
jupyter notebook main.ipynb
