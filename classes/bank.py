import csv
import os

class Bank():
    
    def __init__(self,  id, name, balance, address, city, state):
        self.id = id
        self.name = name
        self.balance = balance
        self.address = address
        self.city = city
        self. state = state

    @classmethod
    def all_accounts(cls):
        acct_holders = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/accounts.csv")

        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                acct_holders.append(Account(**dict(row)))
        return acct_holders