import unittest
from modules.account import Account

class TestBank(unittest.TestCase):
    pass

class TestAccount(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self):
        self.test_account = Account(123, 500, "Date String")
        self.withdrawal_amount = 100

    def tearDown(self):
        del self.test_account

    def test_initial_balance(self):

        self.assertEqual(self.test_account.get_balance(), 500)

    def test_simple_withdraw(self):
        new_balance = self.test_account.withdraw(self.withdrawal_amount)
        self.assertEqual(new_balance, 400)

class TestOwner(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()