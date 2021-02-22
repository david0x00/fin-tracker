import sys
from windows import HomeWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launch_window = HomeWindow()
    sys.exit(app.exec_())