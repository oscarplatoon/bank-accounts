from .account import Account
class CheckingAccount(Account):
    def __init__(self, id, balance, open_date, owner, check_use = 0):
        super().__init__(id, balance, open_date, owner=owner)
        self.check_use = check_use
    
    def withdraw(self, amount):
        if self.balance - amount - 100 < 0:
            raise ValueError("Insufficient Funds to cover withdrawal fee and withdrawal amount")
        self.balance -= 100
        return super().withdraw(amount)

    def withdraw_using_check(self, amount):
        if self.balance - amount < -1000:
            raise ValueError("Exceeds overdraft limit of -$10.00")