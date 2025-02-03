class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Balance: ${self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account = BankAccount(username)

class BankSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username not in self.users:
            new_user = User(username, password)
            self.users[username] = new_user
            print(f"User {username} successfully registered.")
        else:
            print(f"Username {username} is already taken.")

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid login credentials.")
            return None

def show_menu():
 
    print("\nBank System Menu:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Logout")

def main():

    bank_system = BankSystem()
    
    bank_system.register_user("AShutosh", "123467")
    bank_system.register_user("gautam", "mypassword")

    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register New User")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
          
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = bank_system.login(username, password)
            
            if user:
                while True:
                    show_menu()
                    action = input("Choose an option (1-5): ")

                    if action == '1':
                        amount = float(input("Enter amount to deposit: $"))
                        user.account.deposit(amount)
                    elif action == '2':
                        amount = float(input("Enter amount to withdraw: $"))
                        user.account.withdraw(amount)
                    elif action == '3':
                        user.account.check_balance()
                    elif action == '4':
                        user.account.show_transactions()
                    elif action == '5':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice, please try again.")

        elif choice == '2':
           
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            bank_system.register_user(username, password)
            
        elif choice == '3':
            print("Exiting the system...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
