class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return True

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        else:
            print("Insufficient funds!")
            return False

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            recipient.transaction_history.append(f"Received ${amount} from {self.user_id}")
            return True
        else:
            print("Insufficient funds!")
            return False

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.users = {}

    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return user
        else:
            return None

    def add_user(self, user):
        self.users[user.user_id] = user

    def display_menu(self):
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def start(self):
        print("Welcome to the ATM!")
        while True:
            user_id = input("Enter your user ID (minimum 5 digits): ")
            pin = input("Enter your PIN (4 digits): ")

            if len(user_id) >= 5 and len(pin) == 4 and user_id.isdigit() and pin.isdigit():
                user = self.authenticate_user(user_id, pin)
                if user:
                    print("Authentication successful!")
                    while True:
                        self.display_menu()
                        choice = input("Enter your choice: ")
                        if choice == '1':
                            user.display_transaction_history()
                        elif choice == '2':
                            amount = float(input("Enter amount to withdraw: "))
                            if user.withdraw(amount):
                                print("Withdrawal successful!")
                            else:
                                print("Withdrawal failed!")
                        elif choice == '3':
                            amount = float(input("Enter amount to deposit: "))
                            if user.deposit(amount):
                                print("Deposit successful!")
                            else:
                                print("Deposit failed!")
                        elif choice == '4':
                            recipient_id = input("Enter recipient's user ID: ")
                            amount = float(input("Enter amount to transfer: "))
                            recipient = self.users.get(recipient_id)
                            if recipient:
                                if user.transfer(amount, recipient):
                                    print("Transfer successful!")
                                else:
                                    print("Transfer failed!")
                            else:
                                print("Recipient not found!")
                        elif choice == '5':
                            print("Thank you for using the ATM!")
                            break
                        else:
                            print("Invalid choice!")
                else:
                    print("Authentication failed. User not found or incorrect PIN.")
            else:
                print("Invalid user ID or PIN format.")

# Example usage:
atm = ATM()
user1 = User("12345", "1234")
user1.deposit(1000)
atm.add_user(user1)
atm.start()
