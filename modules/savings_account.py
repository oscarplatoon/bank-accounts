from account import Account


class SavingsAccount(Account):
    
    def __init__(self, id, balance, open_date, owner = None):
        self.balance = balance
        if int(self.balance) < 10:
            raise Exception("Argument Error")
    
        
        super().__init__(self, id, balance, open_date)
        #  print("stops here")
        
        
           
            
            
      
        
            
            
test_account = SavingsAccount(44, 12, "06/08/2021")
print(test_account)
