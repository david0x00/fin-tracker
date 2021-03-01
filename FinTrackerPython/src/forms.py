from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class AddEmployee(QWidget):
    def __init__(self, employee_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addEmployee.ui', self)
        self.employee_list = employee_list
        self.submit_employee_btn.clicked.connect(self.addEmployee)
    
    def addEmployee(self):
        self.employee_list.addEmployee()
