from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from PySide6.QtCore import Qt
from interface.proceso_busqueda_window import MainWindow
from controllers.user_menu import UserMenuForm
from database.proceso import DBProceso
from database.usuario import DBUsuario
from database.pieza import DBPieza
from database.maquina import DBMaquina
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from controllers.user_menu import UserMenuForm 
from controllers.machine_menu import MachineMenuForm
from controllers.part_menu import PartMenuForm
from controllers.historial_proceso_window import MainWindowForm as historialProcesoWindow
from random import randint 
from PyQt5.QtGui import QPainter
#from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis,QBarSet,QPercentBarSeries
#from pyqtgraph.opengl import GLViewWidget
from pyqtgraph import plot,PlotWidget ,PlotItem, PlotDataItem, PlotCurveItem, GraphicsLayoutWidget,BarGraphItem


class MainWindowForm(QWidget,MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        self.set_table_data()

        datos_usuario  = DBUsuario().select_name_usuario() 
        datos_usuario.insert(0, "Seleccione un usuario") 
        self.comboBox.addItems(datos_usuario)

        datos_maquina  = DBMaquina().select_name_maquinas()
        datos_maquina.insert(0, "Seleccione una maquina")
        self.comboBox_2.addItems(datos_maquina)

        datos_pieza  = DBPieza().select_name_piezas()
        datos_pieza.insert(0, "Seleccione una pieza")
        self.comboBox_3.addItems(datos_pieza)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_user_changed)
        self.comboBox_2.currentIndexChanged.connect(self.on_combobox_machine_changed)
        self.comboBox_3.currentIndexChanged.connect(self.on_combobox_part_changed)
        self.new_recipe_button_3.clicked.connect(self.historial_window)
        #self.new_recipe_button.clicked.connect(self.new_recipe)
        #self.new_recipe_button_3.clicked.connect(self.machine_menu)
        #self.new_recipe_button_4.clicked.connect(self.part_menu)

    def historial_window(self):
        win = historialProcesoWindow()
        win.show()

    def on_combobox_user_changed(self):
        user = self.comboBox.currentText()
        print(user)
        machine = self.comboBox_2.currentText()
        print(machine)
        part = self.comboBox_3.currentText()
        print(part)
        self.populate_table(DBProceso().filter_procesos(user,machine,part))
        
    def on_combobox_machine_changed(self):
        user = self.comboBox.currentText()
        print(user)
        machine = self.comboBox_2.currentText()
        print(machine)
        part = self.comboBox_3.currentText()
        print(part) 
        self.populate_table(DBProceso().filter_procesos(user,machine,part))

    def on_combobox_part_changed(self):
        user = self.comboBox.currentText()
        print(user)
        machine = self.comboBox_2.currentText()
        print(machine)
        part = self.comboBox_3.currentText()
        print(part)
        self.populate_table(DBProceso().filter_procesos(user,machine,part))

            

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
        
        column_labels = ("ID", "NOMBRE USUARIO","NOMBRE PROCESO", "NOMBRE MAQUINA", "NOMBRE PIEZA", "HORA INICIO", "HORA TERMINO", "NUMERO PIEZAS","PESO MERMA", "OBSERVACIONES", "PIEZAS NETO")
        self.recipes_table.setColumnCount(len(column_labels))
        self.recipes_table.setHorizontalHeaderLabels(column_labels)
        self.recipes_table.setColumnWidth(1, 150)
        self.recipes_table.setColumnWidth(2, 150)
        self.recipes_table.setColumnWidth(3, 150)
        self.recipes_table.setColumnWidth(4, 150)
        self.recipes_table.setColumnWidth(5, 150)
        self.recipes_table.setColumnWidth(6, 150)
        self.recipes_table.setColumnWidth(7, 150)
        self.recipes_table.setColumnWidth(8, 150)
        self.recipes_table.setColumnWidth(9, 150)
        self.recipes_table.setColumnWidth(10,150)
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