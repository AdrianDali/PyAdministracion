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
        

    def grafica01(self):
        axis = pg.DateAxisItem(orientation='bottom',tickFont=10,spacing=100,utcOffset=0,autoExpandTextSpace=True,showValues=True,showLastLabel=True) 
        self.graphicsView_4.setAxisItems({"bottom": axis})
        self.graphicsView_4.showGrid(x=True, y=True)
        self.graphicsView_4.setLabel('left', "Piezas")
        #etiqueta tiempo 
        self.graphicsView_4.setLabel('bottom', "hora")
        self.graphicsView_4.setMouseEnabled(x=False, y=False)
        self.graphicsView_4.addLegend()

        hora = DBProceso().select_hora_historial(self.comboBox_2.currentText(),self.comboBox_5.currentText())
        hora02 = []
        j =0
        for h in hora:
            ti = hora[j]
            tf = ti[0]
            nf = str(tf)
            j = j + 1 
            hora_completa = "2018-02-02 " + nf 
            hora02.append(datetime.strptime(hora_completa,"%Y-%m-%d %H:%M:%S"))
        i =0
        lista_piezas = [] 
        for h in hora:
            i = i+1
            lista_piezas.append(i)

        print("HORA02")

        print(hora02)
        
        self.graphicsView_4.clear()
        self.graphicsView_4.addItem(PlotCurveItem(x = [x.timestamp() for x in hora02], y = lista_piezas, pen = 'r'))
        



    def set_data_table(self):
        user_select = self.comboBox_2.currentText()
        usuario = DBUsuario(nombre=user_select,mode = "select")
        proceso_select = self.comboBox_5.currentText()
        proceso = DBProceso().select_historial(user_select ,proceso_select)
        
     
        #print(proceso)

        self.populate_table(proceso)
        self.grafica01()

    def populate_table(self, data):
   
        #print(data)
        self.tableWidget.setRowCount(len(data))

        for (index_row , row) in enumerate(data):
            #print(index_row)
            #print(row)
            for (index_cell, cell) in enumerate(row):
                #print("cell")
                #print(cell)
                self.tableWidget.setItem(
                     index_row, index_cell, QTableWidgetItem(str(cell))
                )

    def set_data(self):
        lista_procesos = []
        user_select = self.comboBox_2.currentText()
        usuario = DBUsuario(nombre=user_select,mode = "select")
        lista_procesos = DBProceso().select_procesos_user(usuario.id_usuario)

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