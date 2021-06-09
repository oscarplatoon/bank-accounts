from modules.account import Account
from modules.owner import Owner

class AccountInterface():
    def __init__(self):
        self.accounts = Account.all_accounts()
        self.owners = Owner.all_owners()
        self.run()

    def run(self):

        while True:
            input = self.menu()
            if input == 1:
                self.view_owners()
            elif input == 2:
                self.view_accounts()
            elif input == 3:
                self.make_withdrawal()
            elif input == 4:
                self.make_deposit()
            elif input == 5:
                self.find_account()
            elif input == 6:
                break
    
    def menu(self):
        return int(input("1. View Owners\n2. View Accounts\n3. Make Withdrawal\n4. Make Deposit\n5. Find Account\n6. Quit\n> "))
    
    def view_owners(self):
        for owner in self.owners:
            owner.print_owner()
    
    def view_accounts(self):
        for account in self.accounts:
            account.print_account()

    def make_withdrawal(self):
        pass

    def make_deposit(self):
        pass

    def find_account(self):
        id = int(input("Enter account ID: "))
        account = Account.find(id, self.accounts)
        account.print_account()