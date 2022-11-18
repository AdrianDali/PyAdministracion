from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.edit_user_window import DetailWindow
from controllers.popoup_information import PopoupInformation
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario


class EditUserWindowForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.comboBox.addItems(DBUsuario().select_name_usuario_enabled())
        self.add_edit_button_3.clicked.connect(self.edit_user)
        self.comboBox.currentIndexChanged.connect(self.set_data)
        self.cancel_button.clicked.connect(self.cancel)

    def cancel(self):
        self.close()

    def set_data(self):
        user_select = self.comboBox.currentText()
        print("user select")
        print(user_select)
        self.user = DBUsuario(mode = "select", nombre = user_select)
        self.user.select_usuario_info()
        print(self.user.nombre)
        print(self.user.fecha_nacimiento)
        self.administrador_line_edit.setText(self.user.nombre)
        self.dateEdit.setDate(self.user.fecha_nacimiento)
        print("Sda")

    def edit_user(self):
        new_name = self.administrador_line_edit.text()
        date = self.dateEdit.text()
       
        print("edit self.user")
        slices = date.split("/")
        new_date = slices[2] + "-" + slices[1] + "-" + slices[0]
        self.user.update_usuario(name = new_name, date = new_date)
        print(new_name)
        print(new_date)
        PopoupInformation().show()
        
        self.close()



    