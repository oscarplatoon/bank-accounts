from modules.account import Account
from modules.bank import Bank

# a = None
# try: # attempt to execute
#     a = Account(1, -500, "")
#     a.withdraw(1000)
# except ValueError as e: # handle any raised exceptions
#     print(e) 
# else: # will ONLY execute if the try block succeed
#     print("Your balance", a.check_balance())
# finally: # will ALWAYS execute
#     if a is not None:
#         a.deposit(200)


b = Bank()
accounts = b.load_accounts()
# if accounts is not None:
#     for a in accounts:
#         print(a)

a_found = b.find_account_by_id(15152)
print(a_found)