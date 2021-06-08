import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/accounts.csv")


class Account:
    def __init__(self, id, balance, open_date, owner=None):
        self.id = id
        if balance < 0:
            print("INSUFFICIENT FUNDS")
        self.balance = balance
        self.open_date = open_date

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
            print(f"Your current balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    @classmethod
    def get_all_accounts(cls):
        with open(path) as accounts_file:
            reader = csv.DictReader(accounts_file)
            accounts_list = []
            for row in reader:
                new_account = Account(int(row["id"]), int(
                    row["balance"]), row["open_date"])
                accounts_list.append(new_account)
        return accounts_list
