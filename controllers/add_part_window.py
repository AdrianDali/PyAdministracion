from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.add_part_window import DetailWindow
from database.proceso import DBProceso
from database.pieza import DBPieza
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.popoup_information import PopoupInformation


class AddPartWindowForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.add_edit_button_3.clicked.connect(self.add_part)
        self.cancel_button.clicked.connect(self.cancel) 
    
    def cancel(self):
        self.close()

    def add_part(self):
        new_part = self.administrador_line_edit.text()
        DBPieza(mode = "new", nombre = new_part)
        self.close()
        PopoupInformation().show()