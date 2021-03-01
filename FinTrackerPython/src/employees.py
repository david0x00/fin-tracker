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
        self.setupTable()
        self.updateTable()

    def readInEmployees(self):
        self.employee_df = fileFunctions.readCSV(self.employee_list_file)
        self.headers = list(self.employee_df.columns)
    
    def launchAddEmployeeForm(self):
        self.add_form = forms.AddEmployee()
        self.add_form.show()
    
    def addEmployee(self, last_name="", first_name="", address="", city="", state="", zipcode="", ssn="", withholdings=0, salary=0):
    
    def setupTable(self):
        tableFunctions.setRowCount(self.employee_table, self.employee_df.shape[0])
        tableFunctions.setColumnCount(self.employee_table, self.employee_df.shape[1])
        tableFunctions.setHeaders(self.employee_table, self.headers)
    
    def updateTable(self):
        for r, row in self.employee_df.iterrows():
            for c, item in enumerate(row):
                tableFunctions.setItem(self.employee_table, r, c, item)

class Employee:
    def init(self, last_name="", first_name="", address="", city="", state="", zipcode="", ssn="", withholdings=0, salary=0, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.ssn = ssn
        self.withholdings = withholdings
        self.salary = salary
        self.date_added = date_added
        self.active = active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def createCSVString(self):
        csv_string =   self.last_name + "," + self.first_name + "," + self.address + "," \
                     + self.city + "," + self.state + "," + self.zipcode + "," + self.ssn + "," \
                     + self.withholdings + "," + self.salary + "," + self.date_added + "," + self.active + "\n"
        return csv_string