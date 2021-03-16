from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import uic

class AddEmployee(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, employee_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addEmployee.ui', self)
        self.employee_list = employee_list
        self.submit_btn.clicked.connect(self.addEmployee)
    
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
        
class AddCustomer(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, customer_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addCustomer.ui', self)
        self.customer_list = customer_list
        self.submit_btn.clicked.connect(self.addCustomer)
    
    def addCustomer(self):
        last_name = self.last_name_le.text()
        first_name = self.first_name_le.text()
        address = self.address_le.text()
        city = self.city_le.text()
        state = self.state_le.text()
        zipcode = self.zipcode_le.text()
        new_add = self.customer_list.addCustomer(last_name=last_name, first_name=first_name, address=address,
                                        city=city, state=state, zipcode=zipcode)
        if new_add == True:
            self.submit_signal.emit()
            self.close()
        
class AddVendor(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, vendor_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addVendor.ui', self)
        self.vendor_list = vendor_list
        self.submit_btn.clicked.connect(self.addVendor)
    
    def addVendor(self):
        company_name = self.company_name_le.text()
        address = self.address_le.text()
        city = self.city_le.text()
        state = self.state_le.text()
        zipcode = self.zipcode_le.text()
        new_add = self.vendor_list.addVendor(company_name=company_name, address=address,
                                        city=city, state=state, zipcode=zipcode)
        if new_add == True:
            self.submit_signal.emit()
            self.close()

class AddPart(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, part_list, vendor_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/addPart.ui', self)
        self.part_list = part_list
        self.vendor_list = vendor_list
        self.vendor_cb.addItems(self.vendor_list)
        self.submit_btn.clicked.connect(self.addPart)
    
    def addPart(self):
        part_name = self.part_name_le.text()
        part_number = self.part_number_le.text()
        unit_price = self.unit_price_le.text()
        vendor = self.vendor_cb.currentText()

        new_add = self.part_list.addPart(part_name=part_name, part_number=part_number, unit_price=unit_price,
                                         vendor=vendor)
        if new_add == True:
            self.submit_signal.emit()
            self.close()