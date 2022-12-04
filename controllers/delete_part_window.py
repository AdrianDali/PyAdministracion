from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.delete_part_window import DetailWindow
from database.proceso import DBProceso
from database.pieza import DBPieza
from database.maquina import DBMaquina 
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi





class DeletePartWindow(QWidget, DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.comboBox.addItems(DBPieza().select_name_piezas())
        self.add_edit_button_3.clicked.connect(self.delete_part)
        self.cancel_button.clicked.connect(self.close)

    def closing(self):
        self.close()

    def delete_part(self):
        print("delete part")
        part_delete = self.comboBox.currentText()
        print(part_delete)
        DBPieza(nombre = part_delete).delete_pieza() 
        #self.comboBox.clear()
        #self.comboBox.addItems(DBPieza().select_name_pieza_enabled())
        self.closing()