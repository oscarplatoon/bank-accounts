import os
import csv
from owner import Owner

class Account():


    def withdrawal(self, amount):
        try:
            if self.balance - amount <0:
                raise Exception()
            self.balance -= amount
            return self.balance
        except:
            print('\nError: Amount will cause balance to go negative\n')
            return(self.balance)
        

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def view_balance(self):
        return self.balance

    @classmethod
    def objects(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/accounts.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                accounts.append(Account(**dict(row)))
        return accounts