from classes.bank import Bank
from calendar import monthrange
from datetime import datetime
import argparse


class Account():

    def __init__(self, id, name, balance, address, city, state):
        self.id = id
        self.name = name
        self.balance = balance
        self.address = address
        self.city = city
        self. state = state
    def new_account(self, id, balance):
        self.account_id = id
        self.balance = balance

        if balance < 0:
            raise Exception("Sorry, we are unable to open a new account! Please, make initial deposit.")
        else:
            return "Your new account was successfully created!"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Sorry, you don't have enough funds! Your balance is {self.balance}"
        else:
            self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance 
    
    def find(self, my_id):
        self.id = my_id
        accounts = Bank.all_accounts()
        for acct in accounts:
            if id in accounts:
                return acct


class SavingsAccount(Account):

    def __init__(self, name):
        self.name = name
        self.fee = 2
    
    def new_account(self, id, balance):
        self.account_id = id
        self.balance = balance

        if balance >= 10:
            return "Your new account was successfully created!"
        else:
            raise argparse.ArgumentTypeError("Sorry, we are unable to open a new account! Please, make initial deposit of at least $10")

            parser = argparse.ArgumentParser(description='must be greater or equal to 10')
            parser.add_argument('test', type=percentFloat)
            parser.parse_args()

    def withdraw(self, amount):
        if amount > (self.balance - self.fee - 10):
            return f"Sorry, you don't have enough funds! Your balance is {self.balance}"
        else:
            self.balance -= (amount - self.fee)
            return f"Your new balance is {self.balance}"

    def add_interest(self, rate):
        self.balance += (self.balance * 0.25)
        return self.balance

class CheckingAccount(Account):

    def __init__(self, name):
        self.name = name
        self.fee = 1

    def withdraw(self, amount):
        if amount > (self.balance - self.fee):
            return f"Sorry, you don't have enough funds! Your balance is {self.balance}"
        else:
            self.balance -= (amount - self.fee)
            return f"Your new balance is {self.balance}"
    
    def withdraw_using_check(self, amount):
        self.checks_count = 3
        self.overdraft = 10

        if amount > (self.balance + self.overdraft):
            return f"Sorry, you don't have enough funds! Your balance is {self.balance}"
        elif self.checks_count > 0 and amount <= (self.balance + self.overdraft):
            self.checks_count -= 1
            self.balance -= amount
            return f"Your new balance is {self.balance}"
        elif self.checks_count >= 0 and amount <= (self.balance + self.overdraft - 2):
            self.checks_count -= 1
            self.balance -= amount
            return f"Your new balance is {self.balance}"
    
    def reset_checks(self):
 
        given_date = datetime.today().date()
        first_day_of_month = given_date.replace(day=1)

        if given_date == first_day_of_month:
            self.checks_count = 3