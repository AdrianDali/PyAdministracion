from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.delete_user_window import DetailWindow

#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi

from database.usuario import DBUsuario
from controllers.popoup_information import PopoupInformation

class DeleteUserWindowForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.comboBox.addItems(DBUsuario().select_name_usuario_enabled())
        self.add_edit_button_3.clicked.connect(self.delete_user)
        self.cancel_button.clicked.connect(self.close)

    def closing(self):
        self.close()

    def delete_user(self):
        print("delete user")
        user_delete = self.comboBox.currentText()
        print(user_delete)
        DBUsuario(nombre = user_delete).delete_usuario() 
        #self.comboBox.clear()
        #self.comboBox.addItems(DBUsuario().select_name_usuario_enabled())
        self.closing()
        PopoupInformation().show()
        