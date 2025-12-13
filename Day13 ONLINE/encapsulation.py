# OOP Aspect: Encapsulation
# =========================
# Encapsulation is about hiding internal details and only exposing what is necessary.
# We use private variables (by convention: _ or __) and public methods to control access.



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance


# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print("Current balance:", account.get_balance())

# Direct access to __balance is not allowed:
# print(account.__balance)  # AttributeError