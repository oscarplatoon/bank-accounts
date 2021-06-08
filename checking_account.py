from account import Account

class CheckingAccount(Account):
    fee = 1

    # Call the parent Account initializer; no special rules for Checking
    def __init__(self, id, balance, date):
        self.checks = 0
        super().__init__( id, balance, date)

    def withdraw(self, amount):
        amount += CheckingAccount.fee
        new_bal = self.balance - amount
        if new_bal < 0:
            print("Cannot withdraw that much money. Your account was unchanged.")
            return self.balance
        self.balance -= amount
        return self.balance

    #withdraw_using_check(amount): The input amount gets taken out of the account as a result of a check withdrawal.
    #Returns the updated account balance.
    #Allows the account to go into overdraft up to -$10 but not any lower
    #The user is allowed three free check uses in one month, but any subsequent use adds a $2 transaction fee
    def withdraw_using_check(self, amount):
        pass
    
    #reset_checks(): Resets the number of checks used to zero
    def reset_checks(self):
        self.checks = 0
        
        
        