
class CustomerList:
    def __init__(self):

class Customer:
    def init(self, last_name="", first_name="", address="", city="", state="", zipcode="", active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.active = active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def createCSVString(self):
        csv_string =   self.last_name + "," + self.first_name + "," + self.address + "," \
                     + self.city + "," + self.state + "," + self.zipcode + "," + self.active + "\n"
        return csv_string