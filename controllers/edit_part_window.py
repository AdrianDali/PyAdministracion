from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.edit_part_window import DetailWindow
#from database.maquina import DBMaquina
from database.pieza import DBPieza
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.popoup_information import PopoupInformation


class EditPartWindow(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        datos = DBPieza().select_name_piezas()
        datos.insert(0,"Seleccione una pieza")
        self.comboBox.addItems(datos)
        self.comboBox.currentIndexChanged.connect(self.set_data)
        self.cancel_button.clicked.connect(self.cancel)
        self.add_edit_button_3.clicked.connect(self.edit_part)

    def edit_part(self):
        new_part = self.administrador_line_edit.text()
        self.pieza.update_pieza(name = new_part)
        PopoupInformation().show()
        self.close()


    def cancel(self):
        self.close()

    def set_data(self):
        part_select = self.comboBox.currentText()
        self.pieza = DBPieza(mode = "select", nombre = part_select)
        self.pieza.select_name_piezas()
        print(self.pieza.nombre)
        self.administrador_line_edit.setText(self.pieza.nombre)


    