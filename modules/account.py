# Create an `Account` class which should have the following functionality:
#   - A new account should be created with an `ID` and an initial `balance`
#   - Should have a `withdraw` method that accepts a single parameter which represents the amount of money that will be withdrawn. This method should return the updated account balance.
#   - Should have a `deposit` method that accepts a single parameter which represents the amount of money that will be deposited. This method should return the updated account balance.
#   - Should be able to access the current `balance` of an account at any time.
# - Add an `owner` property to each Account to track information about who owns the account.
#   - The `Account` can be created with an `owner`, OR you can create a method that will add the `owner` after the `Account` has already been created.
import os
import csv
import datetime
from modules.owner import Owner

class Account:
    def __init__(self, id, balance, open_date):
        self.id = int(id)
        balance = int(balance)
        if balance < 0:
            raise Exception("Initial Account Balance cannot be less than zero")
        self.balance = balance
        # self.open_date = open_date
        self.open_date = datetime.datetime.strptime(open_date, '%Y-%m-%d %H:%M:%S %z')

    @classmethod
    def all_accounts(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/accounts.csv")
        accounts = []

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                accounts.append(Account(*(row)))

        return accounts

    @classmethod
    def find(self, id, account_list):
        for account in account_list:
            if account.id == id:
                return account

        return None

    def deposit(self, deposit_amount):
        if deposit_amount >= 0:
            self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 0:
            raise Exception (f"Insufficient funds to make a withdraw, balance: {self.balance}, withdraw: {withdraw_amount}")
        
        self.balance -= withdraw_amount
    
    def balance(self):
        return self.balance

    def print_account(self):
        print(f"Account ID: {self.id}\nBalance: {self.balance}\nDate Created {self.open_date}")

# new_account = Account("123456", 1000, datetime.datetime.now())
# new_account.print_account()

