# Create an Account class which should have the following functionality:
from .modules import Owner

class Account():
    # A new account should be created with an ID and an initial balance
    # A new account cannot be created with initial negative balance - this should raise an Exception (leverage those Googling skills!)
    def __init__(self, id, balance, owner = None):
        
        if id == 666:
            raise Exception("Bad account number")
        self.id = id

        if balance < 0:
            raise ValueError("Invalid balance! Please set a positive amount")
        self.balance = balance

        self.owner = owner

    def set_owner(self, owner):
        if self.owner is not None:
            raise Exception("Can not change an owner once one has been set")
        self.owner = owner

    # Should have a withdraw method that accepts a single parameter which represents the amount of money that will be withdrawn. This method should return the updated account balance.
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Can not withdraw amount specified.")

        self.balance = self.balance - amount
        return self.balance

    # Should have a deposit method that accepts a single parameter which represents the amount of money that will be deposited. This method should return the updated account balance.
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    # Should be able to access the current balance of an account at any time.
    def get_balance(self):
        return self.balance