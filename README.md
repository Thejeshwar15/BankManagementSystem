# 🏦 Bank Account Management System

A simple **Bank Account Management System built using Python** to practice Object-Oriented Programming (OOP). The project supports basic banking operations such as depositing money, withdrawing money, checking account balances, and displaying account information.

It also demonstrates **inheritance and method overriding** through Savings Account and Current Account classes.

## 📌 Features

- **Deposit Money:** Deposit money into a bank account with amount validation.
- **Withdraw Money:** Withdraw money after checking the available balance.
- **Check Balance:** View the current account balance.
- **Account Information:** Display the account holder's name and balance.
- **Savings Account:** Calculate and add interest to the account balance.
- **Withdrawal Charges:** Apply an additional ₹50 charge to savings account withdrawals.
- **Current Account:** Create a current account using the base bank account class.
- **Interactive Menu:** Perform banking operations through a command-line interface.
- **Input Validation:** Handle invalid menu choices and non-numeric inputs.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP)
- **OOP Principles:** Encapsulation, Inheritance, Method Overriding
- **Exception Handling:** `try`, `except`, and `ValueError`
- **Interface:** Command-Line Interface (CLI)

## 📂 Project Structure

```text
Bank-Account-Management-System/
│
├── main.py
└── README.md
```

`main.py` contains the bank account classes and the interactive banking menu.

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check your Python version:

```bash
python --version
```

### Installation

1. Clone the repository:

   ```bash
   git clone <your-github-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Bank-Account-Management-System
   ```

3. Run the Python program:

   ```bash
   python main.py
   ```

## 💻 Sample Menu

```text
🏦 Bank Account System
1. Deposit
2. Withdraw
3. Check Balance
4. Account Info
5. Exit

Enter your choice:
```

## 🧱 Classes Overview

### 1. `BankAccount`

The base class that represents a bank account.

**Responsibilities:**
- Initialize the account holder's name and balance.
- Deposit money.
- Withdraw money.
- Display the account balance.
- Display account information.

The balance is stored using a double underscore (`__balance`) to demonstrate name mangling in Python.

### 2. `SavingsAccount`

Inherits from `BankAccount` and introduces savings-specific functionality.

**Responsibilities:**
- Store an interest rate.
- Calculate and add interest to the account.
- Override the withdrawal method to apply an additional ₹50 charge.

### 3. `CurrentAccount`

Inherits from `BankAccount` and represents a current account. It currently uses the base class functionality without additional custom behavior.

## 📚 Python Concepts Practiced

- Classes and objects
- Constructors using `__init__()`
- Encapsulation and name mangling
- Inheritance using `super()`
- Method overriding
- Conditional statements
- Loops and user input
- Exception handling
- Basic financial calculations

## 🔮 Future Improvements

- Add account numbers and PIN authentication.
- Support multiple accounts through a dictionary or database.
- Store account details and transaction history using SQLite.
- Add transaction receipts with timestamps.
- Introduce minimum balance rules and overdraft limits.
- Improve validation for zero, negative, and invalid transaction amounts.
- Add unit tests using Python's `unittest` framework.
- Build a graphical interface or a REST API using FastAPI.

## 🎯 Learning Objective

This project was created to strengthen Python programming skills and understand how OOP concepts can be applied to a real-world scenario.

It serves as a foundation for developing a more complete banking application with secure authentication, database integration, and transaction management.

## 👨‍💻 Author

**Kafi**

A Python learning project focused on Object-Oriented Programming and basic banking operations.

---

*Disclaimer: This is an educational project. It is not intended for handling real financial transactions or storing real banking credentials.*

