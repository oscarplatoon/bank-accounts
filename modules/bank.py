
from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.get_all_accounts()
        
    def all_accounts(self):
        return self.accounts
    
    def find_account_with_id(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
            else:
                print(f"{id} not found")
                return None
    
    
test = Bank("test")
print(test.find_account_with_id(1))