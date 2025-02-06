class BankAccount:
    def __init__(self, account_holder, balance=0):
        """Initialize account with holder name and starting balance"""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        """Check account balance"""
        return f"Account balance: ${self.balance}"

# Example Usage:
account = BankAccount("Alice", 500)
print(account.get_balance())  # Output: Account balance: $500
account.deposit(200)          # Output: Deposited $200. New balance: $700
account.withdraw(100)         # Output: Withdrew $100. New balance: $600
account.withdraw(1000)        # Output: Insufficient funds!
