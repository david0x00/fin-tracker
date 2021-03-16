from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QLineEdit, QMessageBox, QWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QThread, QObject, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5 import uic
import employees
import vendors
import customers
import inventory

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        uic.loadUi('./UserInterfaces/homeWindow.ui', self)
        self.employee_list = employees.EmployeeList(self.employee_table, self.add_employee_btn)
        self.vendor_list = vendors.VendorList(self.vendor_table, self.add_vendor_btn)
        self.customer_list = customers.CustomerList(self.customer_table, self.add_customer_btn)
        self.inventory = inventory.Inventory(self.inventory_table, self.add_part_btn, self.vendor_list)
        self.initializeScreens()
        self.show()

    def initializeScreens(self):
        pass

    def closeEvent(self, event):
        self.closingTasks()
        super(HomeWindow, self).closeEvent(event)
    
    def closingTasks(self):
        print("Closing...")
        #self.saveSettings()
        
