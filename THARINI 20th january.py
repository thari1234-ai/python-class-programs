class BankAccount:
    def __init__(self):
        self.__account_number = None  # Private account number
        self.__balance = 0.0         # Private balance

    def set_account_details(self, account_number, initial_balance):
        # Set the account number and initial balance
        self.__account_number = account_number
        self.__balance = initial_balance
        print(f"Account {self.__account_number} created with balance {self.__balance}")

    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        # Take money out of the account
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        elif amount > self.__balance:
            print("Not enough balance.")
        else:
            print("Enter a valid amount to withdraw.")

    def add_interest(self, rate):
        # Add interest to the balance
        if rate > 0:
            interest = (self.__balance * rate) / 100
            self.__balance += interest
            print(f"Added {interest} as interest. New balance: {self.__balance}")
        else:
            print("Enter a valid interest rate.")

    def get_balance(self):
        # Get the current balance
        return self.__balance

# Example usage
account = BankAccount()
account.set_account_details("123456", 1000)  # Set account number and balance
account.deposit(500)                         # Add money
account.withdraw(200)                        # Take money out
account.add_interest(5)                      # Add 5% interest
print(f"Final balance: {account.get_balance()}")
