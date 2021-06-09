from modules.account import Account
from modules.bank import Bank

test_account = Account(123,10,"23/11/2021")
print(test_account.get_balance())
print(test_account)

try:
    test_account.withdraw(100)
except Exception as e:
    print(e)