class Account:
    
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount
        
    def get_balance(self):
        return self.balance
    

new_account = Account(23, 500)
new_account.deposit(100)
new_account.get_balance()
    
    