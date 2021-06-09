from .account import Account

class SavingsAccount(Account):
    def __init__(self, id, balance, open_date, owner):
        super().__init__(id, balance, open_date, owner=owner)
        if self.balance < 1000:
            raise ValueError("Balance insufficient for savings account!")

    def withdraw(self, amount):
        if balance - 200 < 1000:
            raise ValueError("Insufficient Funds for this Withdrawal.")
        self.balance -= 2
        return super().withdraw(amount)

    def add_interest(self, rate):
        self.balance = self.balance * (rate/100)
        return self.balance