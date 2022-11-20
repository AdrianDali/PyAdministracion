from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.edit_machine_window import DetailWindow
from database.maquina import DBMaquina
from database.pieza import DBPieza
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.popoup_information import PopoupInformation


class EditMachineWindow(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.comboBox.addItems(DBMaquina().select_name_maquinas_enabled())
        self.comboBox.currentIndexChanged.connect(self.set_data)
        self.cancel_button.clicked.connect(self.cancel)
        self.add_edit_button_3.clicked.connect(self.edit_machine)

    def edit_machine(self):
        new_machine = self.administrador_line_edit.text()
        self.machine.update_maquina(name = new_machine)
        PopoupInformation().show()
        self.close()


    def cancel(self):
        self.close()

    def set_data(self):
        machine_select = self.comboBox.currentText()
        self.machine = DBMaquina(mode = "select", nombre = machine_select)
        self.machine.select_maquina_info()
        print(self.machine.nombre)
        self.administrador_line_edit.setText(self.machine.nombre)


    