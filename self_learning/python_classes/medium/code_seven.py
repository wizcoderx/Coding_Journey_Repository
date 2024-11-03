'''
 Create a class `BankAccount` with attributes `account_number` and `balance`. Add methods `deposit(amount)` and `withdraw(amount)`. Create another class `Customer` that has an attribute `accounts`, a list to store multiple `BankAccount` instances. Add methods to allow a customer to open a new account, close an account, and check the balance of all accounts.
'''
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance

class Customer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.accounts = []
        self.accounts.append(BankAccount(account_number, balance))

    #Method to allow customer open an account
    def open_account(self, account_number, balance):
        new_account = BankAccount(account_number, balance)
        self.accounts.append(new_account)
        return new_account

    #Method to allow customer to close an account
    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} closed successfully"
            else:
                return f"Account {account_number} does not exist"

    #Method to check balance of all the accounts
    def check_balance(self):
        total_balance = 0
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, has Balance: {account.balance}")
            total_balance += account.balance
        print(f"Total Balance across all accounts: {total_balance}")

# Example Usage
customer = Customer("John Doe", 123456, 500)
customer.open_account(789012, 1000)
customer.check_balance()
print(customer.close_account(123456))
print(customer.close_account(111111))  # Should indicate the account does not exist




