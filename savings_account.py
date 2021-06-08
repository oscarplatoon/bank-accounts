from account import Account

class SavingsAccount(Account):
    min_balance = 10
    fee = 2
    
    def __init__(self, id, balance, date):
        #The initial balance cannot be less than $10. If it is, this will raise an ArgumentError
        if balance < SavingsAccount.min_balance:
            raise ValueError("Savings account balance must be at least $10.")
        super().__init__( id, balance, date)
        
    def withdraw(self, amount):
        amount += SavingsAccount.fee
        new_bal = self.balance - amount
        if new_bal < SavingsAccount.min_balance:
            print("Cannot withdraw that much money. Your account was unchanged.")
            return self.balance
        self.balance -= amount
        return self.balance


# add_interest(rate): Calculate the interest on the balance and add the interest to the balance. 
# Return the interest that was calculated and added to the balance (not the updated balance).
    def add_interest(self, rate):
        # Takes in <rate>, a percentage like "0.25"
        # Adds "0.25" percent interest to <balance> (Updates <balance>)
        # Returns added interest
        new_interest = self.balance * rate / 100
        self.deposit(new_interest)
        return new_interest
        
# new_acct = SavingsAccount(1,20,1)
# print("Withdrawing $5: New balance is")
# new_bal = new_acct.withdraw(5)
# print("Adding 0.25% interest")
# new_interest = new_acct.add_interest(0.25)
# print(new_interest)
# print(new_acct.get_balance())
