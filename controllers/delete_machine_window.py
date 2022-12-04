from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.delete_machine_window import DetailWindow
from database.proceso import DBProceso
from database.pieza import DBPieza
from database.maquina import DBMaquina 
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.popoup_information import PopoupInformation

class DeleteMachineWindow(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.comboBox.addItems(DBMaquina().select_name_maquinas_enabled())
        self.add_edit_button_3.clicked.connect(self.delete_machine)
        self.cancel_button.clicked.connect(self.close) 
        self.add_edit_button_3.clicked.connect(self.delete_machine)

    def delete_machine(self):
        print("delete machine")
        machine_delete = self.comboBox.currentText()
        print(machine_delete)
        DBMaquina(nombre = machine_delete).delete_maquina() 
        #self.comboBox.clear()
        #self.comboBox.addItems(DBProceso().select_name_maquina_enabled())
        self.close()
        PopoupInformation().show()