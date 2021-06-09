import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/accounts.csv")

class Account:
    def __init__(self, id, balance, open_date, owner=None):
        self.id = id
        self.balance = balance
        if balance < 0:
            raise Exception("ArgumentError")
        self.open_date = open_date
        self.owner = owner

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            raise Exception("INSUFFICIENT FUNDS")
            print(f"Your current balance is ${self.balance}.")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance

    @classmethod
    def objects(cls):
        with open(path) as accounts_file:
            reader = csv.DictReader(accounts_file)
            accounts_list = []
            for row in reader:
                new_account = Account(int(row["id"]), int(
                    row["balance"]), row["open_date"])
                accounts_list.append(new_account)
        return accounts_list
