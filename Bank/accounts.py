import random

class Bank:
    def __init__(self):
        pass

    class Account:
        def __init__(self, id, balance):
            self.id = id
            self.balance = balance
        
        def withdraw(self, amount):
            self.amount = amount
            if self.balance - self.amount <= 0:
                raise Exception("Transcaction cannot be completed due to insuficient funds")
            self.balance -= self.amount
            return self.balance


        def deposit(self, amount):
            self.amount = amount
            self.balance += self.amount
            return self.balance

        def create_account(self, balance):
            self.id = random.randint(100-999)
            if balance > 0:
                self.balance = balance
            else:
                raise Exception("You will need to deposit a posative amount of money to open and account")
