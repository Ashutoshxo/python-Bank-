# python-Bank-
# Bank System

A simple Python-based Bank System application that allows users to create accounts, deposit and withdraw money, check balances, and view transaction history.

## Features
- User registration and login.
- Deposit and withdrawal of funds.
- Check account balance.
- View transaction history.
- Secure password-based login.

## Technologies Used
- Python (3.x)

## Files and Structure
1. `bank_system.py`: Contains the main bank system logic, including user registration, login, and transaction operations.
   - `BankAccount` class: Handles deposits, withdrawals, balance checks, and transaction history.
   - `User` class: Represents a user with a username, password, and associated `BankAccount`.
   - `BankSystem` class: Manages users, registration, and login.
2. The main program allows users to register, login, and perform various banking operations.

## Usage

### Running the Application
To run the bank system:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/bank-system.git
    cd bank-system
    ```

2. Run the Python script:

    ```bash
    python bank_system.py
    ```

3. Follow the on-screen instructions to either register a new user, log in with an existing user, or exit the system.

### Basic Operations:
- **Register a new user**: During the initial prompt, select option `2` and enter a new username and password.
- **Login**: After registering, you can log in with your username and password.
- **Deposit money**: Select option `1` in the user menu and enter the amount you wish to deposit.
- **Withdraw money**: Select option `2` in the user menu and enter the amount you wish to withdraw.
- **Check balance**: Select option `3` in the user menu to check your current account balance.
- **Transaction history**: Select option `4` in the user menu to view a history of all transactions.
- **Logout**: Select option `5` to log out from the current session.

### Example Output

```plaintext
Main Menu:
1. Login
2. Register New User
3. Exit
Choose an option (1-3): 1
Enter your username: AShutosh
Enter your password: 123467
Welcome, AShutosh!

Bank System Menu:
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. View Transaction History
5. Logout
Choose an option (1-5): 1
Enter amount to deposit: $100
Deposited $100. New balance: $100.00
