from .account import Account

# Create a Bank class which will contain your Account class and any future bank account logic.

class Bank():
    def __init__(self):
        self.accounts = [Account()]