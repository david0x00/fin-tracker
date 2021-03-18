from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class CustomerList:
    def __init__(self, home_window):
        self.customer_list_file = "../Customers/customer_list.csv"
        self.home_window = home_window
        self.customer_table = self.home_window.customer_table
        self.add_customer_btn = self.home_window.add_customer_btn
        self.add_customer_btn.clicked.connect(self.launchAddCustomerForm)
        self.readInCustomers()
        self.updateTable()

    def readInCustomers(self):
        self.customer_df = fileFunctions.readCSV(self.customer_list_file)
        self.headers = list(self.customer_df.columns)
    
    def launchAddCustomerForm(self):
        #self.add_customer_btn.setEnabled(False)
        self.add_form = forms.AddCustomer(self)
        self.add_form.submit_signal.connect(self.updateTable)
        self.add_form.show()
    
    def addCustomer(self, last_name="", first_name="", address="", city="", state="", zipcode=""):
        new_customer_dict = \
            {
                "last_name" : last_name,
                "first_name" : first_name,
                "address" : address,
                "city" : city,
                "state" : state,
                "zipcode" : zipcode
            }
        self.customer_df = self.customer_df.append(new_customer_dict, ignore_index=True)
        return True
    
    def updateTable(self):
        tableFunctions.setRowCount(self.customer_table, self.customer_df.shape[0])
        tableFunctions.setColumnCount(self.customer_table, self.customer_df.shape[1])
        tableFunctions.setHeaders(self.customer_table, self.headers)
        for r, row in self.customer_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.customer_table, r, c, item)
        fileFunctions.writeCSV(self.customer_df, self.customer_list_file)