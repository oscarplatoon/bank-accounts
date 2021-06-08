import os
import csv
from owner import Owner
from account import Account

class Bank():

    @classmethod
    def objects(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/account_owners.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                accounts.append(Bank(**dict(row)))
            highest_acccount_id = row.AccountID

        return accounts,highest_acccount_id

    account_owners,highest_account_id = objects()
    accounts = Account.objects()
    owners, highest_owner_id = Owner.objects()


    



