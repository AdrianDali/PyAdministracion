from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.add_edit_user_window import DetailWindow
from controllers.popoup_information import PopoupInformation
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario


class AddEditUserWindowForm(QWidget,DetailWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent 
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.add_edit_button_3.clicked.connect(self.add_user)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self):
        self.close()


    def add_user(self):
        new_name = self.administrador_line_edit.text()
        date = self.dateEdit.text()
        slices = date.split("/")
        new_date = slices[2] + "-" + slices[1] + "-" + slices[0]

        print("add user")
        DBUsuario(mode = "new", nombre = new_name, fecha_nacimiento = new_date)
        
        #self.parent.set_table_data()
        PopoupInformation().show()
        
        self.close()