# ### Optional:
# - Create an `Owner` class which will store information about those who own the `Accounts`.
#   - This should have info like name and address and any other identifying information that an account owner would have.
import csv
import os

class Owner:
    def __init__(self, id, last_name, first_name, street_address, city, state):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state = state

    def print_owner(self):
        print(f"Name: {self.first_name} {self.last_name}\nAddress: {self.street_address}, {self.city}, {self.state}")

    @classmethod
    def all_owners(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../support/owners.csv")
        owners = []

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                owners.append(Owner(*(row)))
                
        return owners
