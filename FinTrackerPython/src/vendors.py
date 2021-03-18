from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class VendorList:
    def __init__(self, home_window):
        self.vendor_list_file = "../Vendors/vendor_list.csv"
        self.home_window = home_window
        self.vendor_table = self.home_window.vendor_table
        self.add_vendor_btn = self.home_window.add_vendor_btn
        self.add_vendor_btn.clicked.connect(self.launchAddVendorForm)
        self.readInVendors()
        self.updateTable()

    def readInVendors(self):
        self.vendor_df = fileFunctions.readCSV(self.vendor_list_file)
        self.headers = list(self.vendor_df.columns)
    
    def launchAddVendorForm(self):
        #self.add_vendor_btn.setEnabled(False)
        self.add_form = forms.AddVendor(self)
        self.add_form.submit_signal.connect(self.updateTable)
        self.add_form.show()
    
    def addVendor(self, company_name="", address="", city="", state="", zipcode=""):
        new_vendor_dict = \
            {
                "company_name" : company_name,
                "address" : address,
                "city" : city,
                "state" : state,
                "zipcode" : zipcode
            }
        self.vendor_df = self.vendor_df.append(new_vendor_dict, ignore_index=True)
        return True
    
    def updateTable(self):
        tableFunctions.setRowCount(self.vendor_table, self.vendor_df.shape[0])
        tableFunctions.setColumnCount(self.vendor_table, self.vendor_df.shape[1])
        tableFunctions.setHeaders(self.vendor_table, self.headers)
        for r, row in self.vendor_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.vendor_table, r, c, item)
        fileFunctions.writeCSV(self.vendor_df, self.vendor_list_file)

    def getListOfNames(self):
        return fileFunctions.getColumnList(self.vendor_df, "company_name")