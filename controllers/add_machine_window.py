from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.add_machine_window import DetailWindow
from database.proceso import DBProceso
from database.maquina import DBMaquina
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.popoup_information import PopoupInformation


class PartMachineWindow(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.add_edit_button_3.clicked.connect(self.add_edit_button_clicked)
        self.cancel_button.clicked.connect(self.closee)

    def closee(self):
        self.close()


    def add_edit_button_clicked(self):

        new_machine = self.administrador_line_edit.text()

        print(new_machine)
        DBMaquina(mode="new",nombre = new_machine)
        PopoupInformation().show()
        self.close()