# Python modules
import sys

# Project Modules
from src.ui.myWindow import *
from src.myWindow import MyWindow

def main():
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QtGui.QIcon(r"assets\cebraicono.jpg"))
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
