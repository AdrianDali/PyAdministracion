from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.delete_machine_window import DetailWindow
from database.proceso import DBProceso
from database.pieza import DBPieza
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi


class DeleteMachineWindow(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)