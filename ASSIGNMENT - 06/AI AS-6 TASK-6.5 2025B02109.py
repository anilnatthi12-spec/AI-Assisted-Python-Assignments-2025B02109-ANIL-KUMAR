# Define the BankAccount class
class BankAccount:
    # Constructor to initialize account holder and balance
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance  # Default balance is 0

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount} successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check balance
    def get_balance(self):
        return self.balance


# --- Example usage ---
# Create a new bank account for a user
account1 = BankAccount("anil", 1000)

# Perform operations
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)
print(f"Final Balance: ₹{account1.get_balance()}")