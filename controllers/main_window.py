from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from PySide6.QtCore import Qt
from interface.main_window import MainWindow
from controllers.user_menu import UserMenuForm
from database.proceso import DBProceso
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
        self.config_table()
        self.set_table_data()

        self.new_recipe_button.clicked.connect(self.new_recipe)
        self.new_recipe_button_3.clicked.connect(self.machine_menu)
        self.new_recipe_button_4.clicked.connect(self.part_menu)
        self.view_button.clicked.connect(self.view_recipe)
        self.new_recipe_button_2.clicked.connect(self.graphics)

    def graphics(self):
        win = GraficasProduccionWindow()
        win.show()


    def view_recipe(self):
        win = ProcesoFiltradoWindow()
        win.show() 

    def new_recipe(self):
        win = UserMenuForm()
        win.show()

    def machine_menu(self):
        win = MachineMenuForm()
        win.show()

    def part_menu(self):
        win = PartMenuForm()
        win.show()



    def config_table(self):


        column_labels = ("ID", "NOMBRE USUARIO",
        "NOMBRE PROCESO", "NOMBRE MAQUINA", 
        "NOMBRE PIEZA", "HORA INICIO", "HORA TERMINO", 
        "NUMERO PIEZAS","PESO MERMA", "OBSERVACIONES ")
        self.recipes_table.setColumnCount(len(column_labels))
        self.recipes_table.setHorizontalHeaderLabels(column_labels)
        self.recipes_table.setColumnWidth(1, 200)
        self.recipes_table.setColumnWidth(2, 200)
        self.recipes_table.setColumnWidth(3, 200)
        self.recipes_table.setColumnWidth(4, 200)
        self.recipes_table.setColumnWidth(5, 200)
        self.recipes_table.setColumnWidth(6, 200)
        self.recipes_table.setColumnWidth(7, 200)
        self.recipes_table.setColumnWidth(8, 200)
        self.recipes_table.setColumnWidth(9, 200)
        self.recipes_table.verticalHeader().setDefaultSectionSize(50)
        self.recipes_table.setColumnHidden(0, True)
        self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    

    def populate_table(self, data):
        self.recipes_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            print(index_row)
            print(row)
            for (index_cell, cell) in enumerate(row):
                print("cell")
                print(cell)
                self.recipes_table.setItem(
                     index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #agregar los botones a la tabla
            #self.recipes_table.setCellWidget(
            #    index_row, 9, self.build_action_buttons()
            #)
    
    def set_table_data(self):
        usuario = DBProceso()
        usuario_list = usuario.select_all_procesos()
        print(usuario_list)
    
        self.populate_table(usuario_list)
