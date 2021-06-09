import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/owners.csv")


class Owner:
    def __init__(self, id, last_name, first_name, street_address, city, state):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state

    @classmethod
    def all_owners(cls):
        with open(path) as owners_file:
            reader = csv.DictReader(owners_file)
            owners_list = []
            for row in reader:
                new_owner = cls(
                    int(row["id"]), 
                    row["last_name"], 
                    row["first_name"],    
                    row["street_address"],
                    row["city"], 
                    row["state"]
                    )
                owners_list.append(new_owner)
        return owners_list