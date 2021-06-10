from classes.account import Account
from classes.bank import Bank
from classes.owner import Owner

# bank = Bank("JP Morgan Chase", id, name, balance, address, city, state))

while True:
    home_page = input("\n1. Open an Account\n2. Deposit\n3. Withdraw\n4. Login\n5. EXIT\n")

    if home_page == '1':
        reg_info = {}
        reg_info.id = int(input("Enter and id "))
        reg_info.balance = int(input("Enter amount of inital deposit "))
        reg_info.lastname = str(input("Enter your last name "))
        reg_info.firstname = str(input("Enter your first name "))
        reg_info.address = input("Enter your house number and street address ")
        reg_info.city = input("Enter your city ")
        reg_info.state = input("Enter state ")
        name = [reg_info.lastname, reg_info.firstname]
        name.join(" ")
        address = [name, reg_info.address, reg_info.city, reg_info.state]
        address.join(',')

        Account.new_account(reg_info.id, reg_info.balance, reg_info.name, address)
        Owner.store_accounts(reg_info.id, reg_info.name, address)
    elif home_page == '2':
        amount = int(input("Enter deposit amount "))
        Account.deposit(amount)
    elif home_page == '3':
        amount = int(input("Enter withdrawal amount "))
        Account.withdraw(amount)
    elif home_page == '4':
        my_id = input("Enter your id ")
        Account.find(my_id)
    elif home_page == '5':
        break