from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QLineEdit, QMessageBox, QWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QThread, QObject, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5 import uic
import employees

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        uic.loadUi('./UserInterfaces/homeWindow.ui', self)
        self.employee_list = employees.EmployeeList(self.employee_table, self.add_employee_btn)
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
        
