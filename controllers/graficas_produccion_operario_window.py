from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from PySide6.QtCore import Qt
from interface.main_window import MainWindow
from controllers.user_menu import UserMenuForm
from database.proceso import DBProceso
from database.usuario import DBUsuario
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from controllers.user_menu import UserMenuForm 
from controllers.machine_menu import MachineMenuForm
from controllers.part_menu import PartMenuForm
from controllers.graficas_produccion_window import MainWindowForm as GraficasProduccionWindow
from controllers.proceso_filtrado_window import MainWindowForm as ProcesoFiltradoWindow
from random import randint 
from PyQt5.QtGui import QPainter
from pyqtgraph import plot,PlotWidget ,PlotItem, PlotDataItem, PlotCurveItem, GraphicsLayoutWidget,BarGraphItem


class MainWindowForm(QWidget,MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        lista_nombres = DBUsuario().select_name_usuario()
        lista_nombres.insert(0, "Selecciona un usuario")
        self.comboBox.insert(lista_nombres)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_user_changed)

    def on_combobox_user_changed(self):
        user = self.comboBox.currentText()
        print(user)

