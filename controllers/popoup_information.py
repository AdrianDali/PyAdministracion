from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.popoup_information import DetailWindow
#from controllers.user_menu import UserMenuForm
#from database.proceso import DBProceso
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi


class PopoupInformation(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.add_edit_button_3.clicked.connect(self.add_user)

    def add_user(self):
        self.close()