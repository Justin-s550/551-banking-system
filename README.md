# Bank Transaction Management with Fraud Detection

**Team Members:** <br>
Justin Phan, email: jphan1@stevens.edu, Stevens ID: 20011192 <br>
Diego Giraldo Tabares, email: dgiraldo@stevens.edu, Stevens ID: 20014654 <br>
Michael Altamirano, email: maltamr@stevens.edu, Stevens ID: 20011442 <br>

**Project Description:** <br>
This project simulates a banking system with fraud detection. Users can create accounts, deposit, withdraw, and transfer money. The program analyzes transaction patterns and user login activity to detect suspicious activity such as large transfers or repeated login attempts.

***Problem and Solution Approach***
As financial fraud becomes more prevalent today, our program aims to provide users and providers of mobile banking applications a few ways to combat and identify fraudulent activity. Our program does this by utilizing the matplotlib library to visualize suspicious login attempts and the time they occured and flagging transaction amounts above a certain threshold amount as fraudulent which users can view in the program when selected. These are just a few ways we came up with to address the growing issue of financial fraud in the modern world. 

**Libraries Used** <br> 
- numpy
- matplotlib
- json
- time
- pytest
- os

**File Structure** <br>
```
551-banking-system/
│
├── main.ipynb                    # Entry point, runs the banking program
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
2. Open the main.ipynb file
3. Run all cells
4. Use the program in the input field after running the ```main``` function
5. To run the tests
```bash
python -m pytest test/test_bank.py -v
```

**Main Contributions of Each Team Member**  
Michael: Creation of ```Account``` and ```FraudDetector``` classes, Pytest cases, and json files for data handling  
Justin: Implementation of ```matplotlib``` for visualizing suspicious login activity and input handling for account creation  
Diego: Creation of entire main program
