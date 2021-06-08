
from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.get_all_accounts()
    
    
    
test = Bank("test")