from PyQt5.QtCore import pyqtSignal, pyqtSlot
import fileFunctions
import tableFunctions
import forms

class EmployeeList:
    def __init__(self, employee_table, add_employee_btn):
        self.employee_list_file = "../Employees/employee_list.csv"
        self.employee_table = employee_table
        self.add_employee_btn = add_employee_btn
        self.add_employee_btn.clicked.connect(self.launchAddEmployeeForm)
        self.readInEmployees()
        self.updateTable()

    def readInEmployees(self):
        self.employee_df = fileFunctions.readCSV(self.employee_list_file)
        self.headers = list(self.employee_df.columns)
    
    def launchAddEmployeeForm(self):
        #self.add_employee_btn.setEnabled(False)
        self.add_form = forms.AddEmployee(self)
        self.add_form.submit_signal.connect(self.updateTable)
        self.add_form.show()
    
    def addEmployee(self, last_name="", first_name="", address="", city="", state="", zipcode="", ssn="", withholdings=0, salary=0):
        new_employee_dict = \
            {
                "last_name" : last_name,
                "first_name" : first_name,
                "address" : address,
                "city" : city,
                "state" : state,
                "zipcode" : zipcode,
                "ssn" : ssn,
                "salary" : salary,
                "withholdings" : withholdings
            }
        self.employee_df = self.employee_df.append(new_employee_dict, ignore_index=True)
        return True
    
    def updateTable(self):
        tableFunctions.setRowCount(self.employee_table, self.employee_df.shape[0])
        tableFunctions.setColumnCount(self.employee_table, self.employee_df.shape[1])
        tableFunctions.setHeaders(self.employee_table, self.headers)
        for r, row in self.employee_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.employee_table, r, c, item)
        fileFunctions.writeCSV(self.employee_df, self.employee_list_file)