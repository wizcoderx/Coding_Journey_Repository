"""
Question 2: Bank Account Manager
Create a class called BankAccount with:

An __init__ method that initializes the account with an initial balance of 0.
A deposit method that takes an amount and adds it to the balance.
A withdraw method that takes an amount and subtracts it from the balance if there are sufficient funds; otherwise, print "Insufficient funds".
A get_balance method that returns the current balance.

"""
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    #deposite method
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    #withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    #get balance method
    def get_balance(self):
        return self.balance

account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.get_balance())  # Output: 50
account.withdraw(60)          # Output: "Insufficient funds"
