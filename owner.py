import os
import csv

class Owner():

    def __init__(self, owner_id, last_name, first_name, address, city, state):
        self.owner_id = owner_id
        self.last_name = last_name 
        self.first_name = first_name        
        self.address = address
        self.city = city
        self.state = state

    def __str__(self):
        return(f'{self.last_name}, {self.first_name}')

    @classmethod
    def objects(cls):
        owners = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/owners.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                owners.append(Owner(**dict(row)))
            highest_owner_id = row.owner_id
        return owners, highest_owner_id

