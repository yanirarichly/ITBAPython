# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../assets/icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_select = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_select.setFont(font)
        self.label_select.setObjectName("label_select")
        self.gridLayout.addWidget(self.label_select, 0, 0, 1, 1)
        self.lineEdit_cc = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cc.setText("")
        self.lineEdit_cc.setObjectName("lineEdit_cc")
        self.gridLayout.addWidget(self.lineEdit_cc, 3, 0, 1, 1)
        self.pushButton_Unificar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Unificar.setObjectName("pushButton_Unificar")
        self.gridLayout.addWidget(self.pushButton_Unificar, 4, 0, 1, 1)
        self.label_c = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_c.setFont(font)
        self.label_c.setObjectName("label_c")
        self.gridLayout.addWidget(self.label_c, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 26))
        self.menubar.setObjectName("menubar")
        self.menuBases_Unidas = QtWidgets.QMenu(self.menubar)
        self.menuBases_Unidas.setObjectName("menuBases_Unidas")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setCheckable(False)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuBases_Unidas.addAction(self.actionAbrir)
        self.menubar.addAction(self.menuBases_Unidas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bases Unidas"))
        self.label_select.setText(_translate("MainWindow", "Seleccione archivos para unificar"))
        self.pushButton_Unificar.setText(_translate("MainWindow", "Unificar datos"))
        self.label_c.setText(_translate("MainWindow", "Columna en común:"))
        self.menuBases_Unidas.setTitle(_translate("MainWindow", "Archivo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
