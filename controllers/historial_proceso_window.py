from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QHeaderView, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.historial_proceso_window import MainWindow
from controllers.popoup_information import PopoupInformation
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from datetime   import datetime
from database.usuario import DBUsuario
from database.proceso import DBProceso
import pyqtgraph as pg
from pyqtgraph import plot,PlotWidget ,PlotItem, PlotDataItem, PlotCurveItem, GraphicsLayoutWidget,BarGraphItem
class MainWindowForm(QWidget,MainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent 
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        users = DBUsuario().select_name_usuario()
        users.insert(0,"Seleccione un usuario")
        self.comboBox_2.addItems(users)
        self.comboBox_2.currentIndexChanged.connect(self.set_data)
        self.comboBox_5.currentIndexChanged.connect(self.set_data_table)
        self.grafica01()

    def grafica01(self):
        bars = BarGraphItem(x=[1,2,3,4,5], height=[1,2,3,4,5], width=0.3, brush='r', pen='r', pxMode=False, name="Bar Graph", opts=None, connect='finite', stepMode=False, fillLevel=0, fillBrush=None, fillOutline=True, antialias=True)
        self.graphicsView_4.addItem(bars)

    def set_data_table(self):
        user_select = self.comboBox_2.currentText()
        usuario = DBUsuario(nombre=user_select,mode = "select")
        proceso_select = self.comboBox_5.currentText()
        proceso = DBProceso().select_historial(user_select ,proceso_select)
        
     
        print(proceso)

        self.populate_table(proceso)

    def populate_table(self, data):
   
        print(data)
        self.tableWidget.setRowCount(len(data))

        for (index_row , row) in enumerate(data):
            print(index_row)
            print(row)
            for (index_cell, cell) in enumerate(row):
                print("cell")
                print(cell)
                self.tableWidget.setItem(
                     index_row, index_cell, QTableWidgetItem(str(cell))
                )

    def set_data(self):
        user_select = self.comboBox_2.currentText()
        usuario = DBUsuario(nombre=user_select,mode = "select")
        print("user select")
        lista_procesos = DBProceso().select_procesos_user(usuario.id_usuario)
        print("##############################")
        print(lista_procesos)
        lista_procesos.insert(0,("Seleccione un proceso"))
        self.comboBox_5.addItems(lista_procesos)

    def config_table(self):
        column_labels = ("ID", "PROCESO","HORA DE INYECCION", "PESO MERMA")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,250)
        self.tableWidget.setColumnWidth(4,250)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)