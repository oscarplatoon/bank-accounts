import unittest
from modules.account import Account
from modules.bank import Bank

class TestBank(unittest.TestCase):
    pass

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.test_account = Account(123, 500, "Date String")
        self.withdrawal_amount = 100
        self.deposit_amount = 100

    def test_initial_balance(self):
        self.assertEqual(self.test_account.get_balance(), 500)

    def test_simple_withdraw(self):
        new_balance = self.test_account.withdraw(self.withdrawal_amount)
        self.assertEqual(new_balance, 400)

    def test_simple_deposit(self):
        new_balance = self.test_account.deposit(self.deposit_amount)
        self.assertEqual(new_balance, 600)

    # WIP Research how to test Raise Exception Syntax
    # def test_account_creation_error(self):
    #     self.failUnlessRaises(Exception("ArgumentError"), Account(123,-1,"Date String"))

class TestOwner(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()