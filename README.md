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
```
551-banking-system/
│
├── main.py                    # Entry point, runs the banking program
│
├── data/
│   ├── accounts.json          # Persistent storage for user accounts
│   └── transactions.json      # Sample transaction data
│
├── modules/
│   ├── account.py             # Account class with banking operations
│   ├── analytics.py           # Transaction analysis and statistics
│   ├── data_manager.py        # JSON file read/write helpers
│   └── detection.py           # FraudDetector class
│
├── test/
│   └── test_bank.py           # Pytest unit tests
│
└── README.md
```

**How to Run**
1. Clone the repository
```bash
git clone https://github.com/Justin-s550/551-banking-system.git
cd 551-banking-system
```
2. Install dependencies
```bash
pip install numpy matplotlib pytest
```
 3. Run the program
```bash
python main.py
```
4. Run the tests
```bash
python -m pytest test/test_bank.py -v
```
