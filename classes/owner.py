from classes.account import Account

class Owner():

    def __init__(self, name):
        self.name = name
    
    def store_accounts(self, id, name, address):
        self.owner_id = id
        self.name = name
        self.address = address
        self.owners = []
        owner = {id: self.id, name: self.name, address: self.address}
        self.owners.append(owner)