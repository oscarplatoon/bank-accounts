import csv, os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "support/accounts.csv")

class Account:
    # id
    # balance
    # withdraw(): takes in amt withdrawn, returns updated <balance>
    # deposit():  takes in amt deposited, returns updated <balance>
    # getbalance(): returns balance
    
    def __init__(self, id, balance, date):
        try:
            balance = int(balance)
            if balance < 0:
                raise Exception("Can't open account with a negative balance.")
            self.id = id
            self.balance = balance
            self.date = date
        except Exception as message:
            print(message)
            return None

    def __str__(self):
        return f"Account: id {self.id}, balance C{self.balance}, date opened {self.date}"

    #The withdraw method does not allow the account to go negative - it should output a warning message 
    #and return the original un-modified balance
    def withdraw(self, amount):
        new_bal = self.balance - amount
        if new_bal < 0:
            print("Cannot withdraw that much money. Your account was unchanged.")
            return self.balance
        self.balance -= amount
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance
        
    #returns a collection of Account instances, representing all of the Accounts described in the CSV.
    # See below for the CSV file specifications
    @classmethod
    def all_accounts(self):
        with open(path) as f:
           reader = csv.reader(f)
           account_list = []
           for line in reader:
              #Print each line as arrays
              #    def __init__(self, id, balance, date):
              account_list.append(Account(line[0], line[1], line[2]))
        return account_list
        
    # returns an instance of Account where the value of the id field in the CSV matches the passed parameter
    @classmethod
    def find(self, id):
        id = str(id)
        account_list = Account.all_accounts()
        for x in account_list:
            if x.id == id:
                return x
        return None

#Driver code
#print( Account.find(1217))
#testme = Account(1, -1, 1)