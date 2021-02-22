class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        uic.loadUi('./UserInterfaces/homeWindow.ui', self)
        self.show()

    def closeEvent(self, event):
        self.closingTasks()
        super(HomeWindow, self).closeEvent(event)
    
    def closingTasks(self):
        print("Closing...")
        #self.saveSettings()
