class VendorList:
    def __init__(self):

class Vendor:
    def init(self, company_name="", part_dict={}, address="", city="", zipcode="", active=True):
        self.company_name = company_name
        self.part_dict = part_dict
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.active = active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def createCSVString(self):
        csv_string =   self.company_name + "," + self.address + "," \
                     + self.city + "," + self.zipcode + "," + self.active + "\n"
        return csv_string