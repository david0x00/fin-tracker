from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import uic
import fileFunctions

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

class BuildRobots(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, inventory, product_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/buildRobots.ui', self)
        self.inventory = inventory
        self.product_list = product_list
        self.product_cb.addItems(self.product_list)
        self.submit_btn.clicked.connect(self.buildRobots)
    
    def buildRobots(self):
        product = self.product_cb.currentText()
        try:
            quantity = int(self.quantity_le.text())
        except ValueError:
            quantity = 0

        success = self.inventory.buildRobots(product=product, quantity=quantity)

        if success == True:
            self.submit_signal.emit()
            self.close()

class SellRobots(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, inventory, product_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/sellRobots.ui', self)
        self.inventory = inventory
        self.product_list = product_list
        self.product_cb.addItems(self.product_list)
        self.submit_btn.clicked.connect(self.sellRobots)
    
    def sellRobots(self):
        product = self.product_cb.currentText()
        try:
            quantity = int(self.quantity_le.text())
        except ValueError:
            quantity = 0

        success = self.inventory.sellRobots(product=product, quantity=quantity)

        if success == True:
            self.submit_signal.emit()
            self.close()

class PurchaseParts(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, inventory, parts_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/purchaseParts.ui', self)
        self.inventory = inventory
        self.parts_list = parts_list
        self.parts_cb.addItems(self.parts_list)
        self.quantity_le.textChanged.connect(self.calculateCost)
        self.parts_cb.activated.connect(self.calculateCost)
        self.submit_btn.clicked.connect(self.purchaseParts)
    
    def calculateCost(self):
        try:
            quantity = int(self.quantity_le.text())
            idx = self.parts_cb.currentIndex()
            unit_price = self.inventory.inventory_df.unit_price[idx]
            total_cost = unit_price * quantity
            self.total_cost_label.setText(fileFunctions.formatCurrency(total_cost))
        except ValueError:
            self.total_cost_label.setText(fileFunctions.formatCurrency(0))
    
    def purchaseParts(self):
        part_num = self.parts_cb.currentIndex()

        try:
            quantity = int(self.quantity_le.text())
        except ValueError:
            quantity = 0

        success = self.inventory.purchaseParts(part_num=part_num, quantity=quantity)

        if success == True:
            self.submit_signal.emit()

class Payroll(QWidget):
    submit_signal = pyqtSignal()
    
    def __init__(self, inventory, product_list):
        super().__init__()
        uic.loadUi('./UserInterfaces/sellRobots.ui', self)
        self.inventory = inventory
        self.product_list = product_list
        self.product_cb.addItems(self.product_list)
        self.submit_btn.clicked.connect(self.sellRobots)
    
    def sellRobots(self):
        product = self.product_cb.currentText()
        try:
            quantity = int(self.quantity_le.text())
        except ValueError:
            quantity = 0

        success = self.inventory.sellRobots(product=product, quantity=quantity)

        if success == True:
            self.submit_signal.emit()
            self.close()