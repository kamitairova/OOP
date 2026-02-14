Personal Account Management System

Project Overview

The system allows users to:
Create a personal bank account
Deposit funds
Withdraw funds (with balance validation)
Track account balance
View transaction history
Use operator overloading (+ and -) for transactions

The project demonstrates the practical implementation of:
Classes and objects
Encapsulation
Data validation
Magic methods (str, add, sub)
Transaction history management
Unit testing with pytest
🏗 Project Structure
Копировать код

OOP/
│
├── personal_account.py      # Contains Amount and PersonalAccount classes
├── demo.py                  # Basic demonstration of functionality
├── test_2.py            # Extended test scenarios
├── test_personal_account.py # Automated test cases (pytest)
└── README.md

Class Descriptions

1️⃣ Amount Class
Represents a single transaction (deposit or withdrawal).
Attributes:
amount (float) – transaction amount
timestamp (datetime) – date and time of transaction
transaction_type (str) – "DEPOSIT" or "WITHDRAWAL"
Methods:
init() – initializes transaction data
str() – returns readable string representation
2️⃣ PersonalAccount Class
Represents a personal bank account.
Attributes:
_account_number (int)
_account_holder (str)
_balance (float)
_transactions (list of Amount objects)
Methods:
deposit(amount) – adds funds to account
withdraw(amount) – withdraws funds with balance validation
print_transaction_history() – prints all transactions
get_balance() – returns current balance
get_account_number() – returns account number
set_account_number() – sets account number
get_account_holder() – returns account holder
set_account_holder() – sets account holder
str() – returns formatted account information
add(amount) – same as deposit (operator +)
sub(amount) – same as withdraw (operator -)

▶️ How to Run the Program
Make sure you are inside the project directory:

cd OOP

🔹 Run Basic Demonstration
Bash
python demo.py

This script performs predefined deposit and withdrawal operations.
🔹 Run Extended Test Scenario
Bash
python extra_demo.py
This script demonstrates:
Multiple transactions
Operator overloading
Error handling
Account modification

Running Automated Tests
Install pytest (if not installed)
Bash
python -m pip install pytest
Run tests

Bash
python -m pytest

Quiet mode:
Bash
python -m pytest -q

