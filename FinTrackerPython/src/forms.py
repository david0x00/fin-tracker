from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import uic

class AddEmployee(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, employee_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addEmployee.ui', self)
        self.employee_list = employee_list
        self.submit_employee_btn.clicked.connect(self.addEmployee)
    
    def addEmployee(self):
        last_name = self.last_name_le.text()
        first_name = self.first_name_le.text()
        address = self.address_le.text()
        city = self.city_le.text()
        state = self.state_le.text()
        zipcode = self.zipcode_le.text()
        ssn = self.ssn_le.text()
        withholdings = self.withholdings_le.text()
        salary = self.salary_le.text()
        new_add = self.employee_list.addEmployee(last_name=last_name, first_name=first_name, address=address,
                                        city=city, state=state, zipcode=zipcode, ssn=ssn,
                                        withholdings=withholdings, salary=salary)
        if new_add == True:
            self.submit_signal.emit()
            self.close()
        
