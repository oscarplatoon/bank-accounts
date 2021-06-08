import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/account_owners.csv")

from owner import Owner
from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.get_all_accounts()
        self.owners = Owner.get_all_owners()
        
    def all_accounts(self):
        return self.accounts
    
    def find_account_with_id(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
            else:
                print(f"{id} not found")
                return None
            
    def assign_owner_to_account(self):
        account_owner_id = Bank.get_all_account_owners()
        for value in account_owner_id:
            for account in self.accounts:
                if int(account.id) == int(value["account_id"]):
                    for owner in self.owners:
                        print(f"owner: {owner}")
                        if owner.id == int(value["owner_id"]):
                            account.owner = owner
                            print(f"account owner: {account.owner.first_name}")
                            
    @classmethod
    def get_all_account_owners(cls):
        with open(path) as account_owners_file:
            reader = csv.DictReader(account_owners_file)
            account_owners_list = []
            for row in reader:
                new_account_owner = dict(row)
                account_owners_list.append(new_account_owner)
        return account_owners_list
        
            

    
    
test = Bank("test")
test.assign_owner_to_account()
# print(test.find_account_with_id(1212))
# print(Bank.get_all_account_owners())