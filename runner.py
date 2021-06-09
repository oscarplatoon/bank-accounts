from modules.account import Account
from modules.bank import Bank

test_account = Account(123,10,"23/11/2021")
print(test_account.get_balance())
print(test_account)

try:
    bad_account = Account(123, -500, "Date String")
except Exception as e:
    print(e)