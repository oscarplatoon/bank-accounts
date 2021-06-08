from types import CoroutineType
from bank import Bank
from account import Account
from owner import Owner

class Interface():

    def run(self):
        while True:
            response = input(f'\nWhat would you like to do?\n1. Login\n2. Create new Account\n')
            
            if response == '1':
                id = input(f'Enter account id:\t')

            elif response == '2':
                Owner.highest_owner_id += 1
                owner_id = Owner.highest_owner_id
                last_name = input(f'Enter last name:\t')
                first_name = input(f'Enter first name:\t')
                address = input(f'Enter address:\t')
                city = input(f'Enter city:\t')
                state = input(f'Enter state:\t')
                self.Bank.owners.append({
                    'owner_id'      : owner_id,
                    'last_name'     : last_name,
                    'first_name'    :first_name,
                    'address'       :address,
                    'city'          :city,
                    'state'         :state
                })



            response = input(f'\nWhat would you like to do?\n1. View Balance\n2. Withdrawal\n3. Deposit\n4. Quit\n5. View Admin Info')

            if response == '1':
                pass
            elif response == '2':
                self.view_balance()
                
            elif response == '3':
                pass
            elif response == '4':
                pass
            elif response == '5':
                pass
            else:
                print(f'\nInvalid Input\n')


        

