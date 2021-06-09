from modules.account import Account
from modules.bank import Bank
from modules.owner import Owner
from modules.savings_account import SavingsAccount

b = Bank()
accounts = b.load_accounts()

a_found = b.find_account_by_id(15152)
print(a_found)

try:
    sa = SavingsAccount(1, 20, "")
    sa.withdraw(10)
except Exception as e:
    print(e)