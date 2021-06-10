from .account import Account


class SavingsAccount(Account):
    minimum_balance = 10
    withdraw_fee = 2
    
    # def __init__(self, id, balance, open_date, owner = None):
    def __init__(self, id, balance, open_date, owner = None):
        # self.balance = balance
        # if int(self.balance) < 10:
        #     raise Exception("Invalid Balance!  Savings Account balance must be no less than $10.00.")
        # super().__init__(self, id, balance, open_date)
        super().__init__(id, balance, open_date, owner = owner)
        
        if balance < self.minimum_balance:
            raise ValueError(f"Invalid Balance!  Savings Account balance must be no less than ${self.minimum_balance}.")
        
        
        
    def withdrawal_fee(self, amount):
        return super().withdraw(amount, fee = self.withdraw_fee)
        # if self.balance - amount - self.withdraw_fee < self.miniumum_balance:
        #     raise ValueError("Cannot withdraw amount specified.")
        
        # self.balance = self.balance - amount
        # return self.balance
        # super().withdraw(amount)
        
        
        
       
        
        
           
            
            
      
        
            
            
test_account = SavingsAccount(44, 12, "06/08/2021")
print(test_account)
