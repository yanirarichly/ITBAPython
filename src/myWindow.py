"""
Este programa puede unificar bases de datos .xlsx contenidas en una misma carpeta
"""
from src.ui.myWindow import *
from PyQt5.QtWidgets import QWidget, QDialog, QComboBox, QMessageBox, QFileDialog, QApplication
from src.app import *
from PyQt5 import QtGui

import pandas as pd
import sys

app = QApplication(sys.argv)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

#Esta función define la interfaz e inicializa algunas variables clave
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icono.ico"))
        self.column = ""
        self.pushButton_Unificar.clicked.connect(self.get_column)
        self.actionAbrir.triggered.connect(self.get_file)
        self.archivo = []

#Esta función obtiene la ruta de los archivos a unificar y la muestra en pantalla
    def get_file(self):
        self.nombre = QFileDialog.getOpenFileNames(self, "Abrir Archivo", "", "(*.xlsx)")
        self.contador = 0
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

#get_column y get_text funcionan juntas para que el texto que introduce el usuario como columna comun sea key de la unificación posterior
    def get_column(self):
        self.column = self.get_text()
        self.backend()

    def get_text(self):
        text = self.lineEdit_cc.text()
        text_split = text.split(" ")
        return text_split

#Esta función unifica los archivos seleccionados
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
            self.exito()

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
                self.exito()

    """
    Esta función muestra un mensaje de éxito si se logra la unificación y
    reinicia las variables clave del inicio por si se quiere realizar otra operación
    """
    def exito(self):
        self.widgetInfo = QMessageBox(
            QMessageBox.Information,
            "Operación exitosa",
            "Sus bases de datos fueron unificadas correctamente",
            QMessageBox.Ok
        )
        self.widgetInfo.show()
        self.archivo = []