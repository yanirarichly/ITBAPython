from src.ui.myWindow import *
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox, QMessageBox, QFileDialog, QApplication
from src.app import *
from PyQt5 import QtGui

import pandas as pd
import sys

app = QApplication(sys.argv)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icono.ico"))
        self.column = ""
        self.pushButton_Unificar.clicked.connect(self.get_column)
        self.actionAbrir.triggered.connect(self.get_file)
        self.contador = 0
        self.archivo = []

    def get_file(self):
        self.nombre = QFileDialog.getOpenFileNames(self, "Abrir Archivo", "", "(*.xlsx)")
        texto = "Archivos selccionados:" + "\n"
        for x in (self.nombre[0]):
            self.contador = self.contador + 1
            texto = texto + x + "\n"
            self.label_select.setText(texto)
        if self.contador < 2:
            self.widgetO = QMessageBox(
                QMessageBox.Warning,
                "Atención",
                "Seleccione más de un archivo",
                QMessageBox.Ok
            )
            self.widgetO.show()
            self.contador = 0

    def get_column(self):
        self.column = self.get_text()
        self.backend()

    def get_text(self):
        text = self.lineEdit_cc.text()
        text_split = text.split(" ")
        return text_split

    def backend(self):
        j = 0
        while self.contador > j:
            sheet = pd.read_excel(self.nombre[0][j])
            sheet = sheet.drop_duplicates()
            y = 0
            while y < len(self.column):
                if not self.column[y] in sheet.columns:
                    self.widgetE = QMessageBox(
                        QMessageBox.Critical,
                        "Error",
                        "La/s columna/s seleccionada/s no se encuentra/n en todos los archivos",
                        QMessageBox.Ok
                    )
                    self.widgetE.show()
                    return 0
                y = y + 1
                self.archivo.append(sheet)
                j = j + 1

        if self.contador == 2:
            union = pd.merge(self.archivo[0], self.archivo[1], on=self.column)
            union = union.drop_duplicates()
            union.fillna("-", inplace=True)
            union.to_excel("listas_unificadas.xlsx")
            self.widgetInfo = QMessageBox(
                QMessageBox.Information,
                "Operación exitosa",
                "Sus bases de datos fueron unificadas correctamente",
                QMessageBox.Ok
            )
            self.widgetInfo.show()
            self.contador = 0

        elif self.contador > 2:
            union = pd.merge(self.archivo[0], self.archivo[1], on=self.column)
            union = union.drop_duplicates()
            union.fillna("-", inplace=True)

        i = 2
        while self.contador > i:
            union = pd.merge(union, self.archivo[i], on=self.column)
            union = union.drop_duplicates()
            union.fillna("-", inplace=True)
            i = i + 1
            if self.contador > 2:
                union.to_excel("listas_unificadas.xlsx")
                self.widgetInfo = QMessageBox(
                    QMessageBox.Information,
                    "Operación exitosa",
                    "Sus bases de datos fueron unificadas correctamente",
                    QMessageBox.Ok
                )
                self.widgetInfo.show()
                self.contador = 0
