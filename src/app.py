# Python modules
import sys

# Project Modules
from src.ui.myWindow import *
from src.myWindow import MyWindow

def main():
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
