from modules.account import Account
from modules.bank import Bank

try: # attempt to execute
    a = Account(1, 500)
    a.withdraw(1000)
except ValueError as e: # handle any raised exceptions
    print(e) 
else: # will ONLY execute if the try block succeed
    print("Your balance", a.check_balance())
finally: # will ALWAYS execute
    a.deposit(200)

print("donuts are yummy")
