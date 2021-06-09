from .account import Account
from .owner import Owner
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/account_owners.csv")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.objects()
        self.owners = Owner.objects()

    def __str__(self):
        return f"--------\n{self.name}\n----------"

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
                        if owner.id == int(value["owner_id"]):
                            account.owner = owner
                            # print(f"account owner: {account.owner.first_name}")

    @classmethod
    def get_all_account_owners(cls):
        with open(path) as account_owners_file:
            reader = csv.DictReader(account_owners_file)
            account_owners_list = []
            for row in reader:
                new_account_owner = dict(row)
                account_owners_list.append(new_account_owner)
        return account_owners_list