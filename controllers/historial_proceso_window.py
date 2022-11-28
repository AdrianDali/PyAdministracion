from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.historial_proceso_window import MainWindow
from controllers.popoup_information import PopoupInformation
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario


class MainWindowForm(QWidget,MainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent 
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()

    def config_table(self):
        column_labels = ("ID","NOMBRE", "HORA DE INYECCION", "PESO MERMA")
        
