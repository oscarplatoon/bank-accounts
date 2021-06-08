from bank import Bank
from interface import Interface
import random




id = random.randint(100000,999999)
initial_balance = float(input(f'What is the initial deposit amount?\t'))
test_account = Bank.Account(id, initial_balance)

print(test_account.id)
print(test_account.owner)


print(test_account.view_balance())
print(test_account.withdrawal(600))
print(test_account.deposit(200))

print(test_account.withdrawal(800))