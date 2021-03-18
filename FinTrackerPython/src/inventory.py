from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class Inventory:
    def __init__(self, home_window):
        self.part_list_file = "../Inventory/part_list.csv"
        self.home_window = home_window
        self.inventory_table = self.home_window.inventory_table
        self.add_part_btn = self.home_window.add_part_btn
        self.vendor_list = self.home_window.vendor_list
        self.add_part_btn.clicked.connect(self.launchAddPartForm)
        self.readInParts()
        self.updateTable()

    def readInParts(self):
        self.inventory_df = fileFunctions.readCSV(self.part_list_file)
        self.headers = list(self.inventory_df.columns)
    
    def launchAddPartForm(self):
        #self.add_part_btn.setEnabled(False)
        vendor_name_list = self.vendor_list.getListOfNames()
        self.add_form = forms.AddPart(self, vendor_name_list)
        self.add_form.submit_signal.connect(self.updateTable)
        self.add_form.show()
    
    def addPart(self, part_name="", part_number="", unit_price="", vendor=""):
        new_part_dict = \
            {
                "part_name" : part_name,
                "part_number" : part_number,
                "unit_price" : unit_price,
                "vendor" : vendor
            }
        self.inventory_df = self.inventory_df.append(new_part_dict, ignore_index=True)
        return True
    
    def updateTable(self):
        tableFunctions.setRowCount(self.inventory_table, self.inventory_df.shape[0])
        tableFunctions.setColumnCount(self.inventory_table, self.inventory_df.shape[1])
        tableFunctions.setHeaders(self.inventory_table, self.headers)
        for r, row in self.inventory_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.inventory_table, r, c, str(item))
        fileFunctions.writeCSV(self.inventory_df, self.part_list_file)