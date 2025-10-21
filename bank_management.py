class Account:
    """Class to represent a bank account."""
    def __init__(self, name, balance, pin, transactions=None):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.transactions = transactions if transactions is not None else []

    def check_balance(self):
        print(f"\n{self.name}, your current balance is: ₹{self.balance}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"\n Deposit successful! New balance: ₹{self.balance}\n")
        else:
            print("\nInvalid deposit amount.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n Invalid withdrawal amount.\n")
        elif amount > self.balance:
            print("\n Insufficient balance.\n")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f"\n Withdrawal successful! New balance: ₹{self.balance}\n")

    def show_transactions(self):
        print(f"\n Transaction History for {self.name}:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(" -", t)
        print()


class ATM:
    """Class to simulate ATM operations."""
    def __init__(self, accounts):
        # Convert each account dict into an Account object
        self.accounts = [Account(**acc) for acc in accounts]

    def authenticate(self, name, pin):
        """Authenticate user by name and PIN."""
        for acc in self.accounts:
            if acc.name.lower() == name.lower() and acc.pin == pin:
                return acc
        return None

    def menu(self):
        """Display ATM menu and handle user operations."""
        while True:
            print("===== ATM MACHINE =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '5':
                print("\n Thank you for using our ATM. Goodbye!\n")
                break

            name = input("Enter your name: ")
            try:
                pin = int(input("Enter your 4-digit PIN: "))
            except ValueError:
                print("\nInvalid PIN format.\n")
                continue

            user = self.authenticate(name, pin)
            if not user:
                print("\n Invalid name or PIN.\n")
                continue

            if choice == '1':
                user.check_balance()
            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                    user.deposit(amount)
                except ValueError:
                    print("\nInvalid amount.\n")
            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                    user.withdraw(amount)
                except ValueError:
                    print("\n Invalid amount.\n")
            elif choice == '4':
                user.show_transactions()
            else:
                print("\n Invalid choice. Please select 1-5.\n")


# ---------- Predefined Accounts Data ----------
accounts_data = [
    {"name": "Ravi", "balance": 5000, "pin": 1234, "transactions": []},
    {"name": "Priya", "balance": 7000, "pin": 2345, "transactions": []},
    {"name": "Suresh", "balance": 10000, "pin": 3456, "transactions": []},
    {"name": "Anita", "balance": 3000, "pin": 4567, "transactions": []},
    {"name": "Kiran", "balance": 8500, "pin": 5678, "transactions": []},
    {"name": "Meena", "balance": 12000, "pin": 6789, "transactions": []},
    {"name": "Vamsi", "balance": 4500, "pin": 7890, "transactions": []},
    {"name": "Rohit", "balance": 6000, "pin": 8901, "transactions": []},
    {"name": "Sonia", "balance": 9000, "pin": 9012, "transactions": []},
    {"name": "Neha", "balance": 11000, "pin": 1122, "transactions": []}
]


# ---------- Main Program ----------
if __name__ == "__main__":
    atm = ATM(accounts_data)
    atm.menu()
