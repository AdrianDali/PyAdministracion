from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from PySide6.QtCore import Qt
from interface.graficas_produccion_window import DetailWindow
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
from controllers.proceso_filtrado_window import MainWindowForm as ProcesoFiltradoWindow
from random import randint 
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis,QBarSet,QPercentBarSeries
#from pyqtgraph.opengl import GLViewWidget
from pyqtgraph import plot,PlotWidget ,PlotItem, PlotDataItem, PlotCurveItem, GraphicsLayoutWidget,BarGraphItem


class MainWindowForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.comboBox_3.addItems(["Dia","Semana","Mes"])
        self.comboBox_2.addItems(["Dia","Semana","Mes"])
        self.comboBox_4.addItems(["Dia","Semana","Mes"])
        self.comboBox_5.addItems(["Dia","Semana","Mes"])

        #self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10],4)

        ###########Aqui se crea el grafico de barras#######
        #bars = BarGraphItem(x=[1,2,3,4,5], height=[1,2,3,4,5], width=0.3)
        #self.graphicsView.addItem(bars)
        #################################################
        ##########Aui se crea grafica lineal#################
        
        axis = pg.DateAxisItem(orientation='bottom')
        
        self.line = pg.PlotCurveItem(clear=True, pen="g")
        self.graphicsView.addItem(self.line)
        self.graphicsView.setAxisItems({"bottom": axis})
        self.graphicsView.showGrid(x=True, y=True)
        #etiqueta nombre prouccion
        self.graphicsView.setLabel('left', "Produccion")
        #etiqueta tiempo 
        self.graphicsView.setLabel('bottom', "Tiempo")

        self.graphicsView.setMouseEnabled(x=True, y=True)
        self.graphicsView.setRange(xRange=[0, 0], yRange=[0, 1500], padding=0)
        self.graphicsView.setLimits(xMin=0, xMax=210000, yMin=0, yMax=1000)

        #self.graphicsView.setDownsampling(mode='peak')

        #self.graphicsView.setAxisItems({'bottom': TimeAxisItem(orientation='bottom')})

        #self.graphicsView 
        #line=PlotCurveItem([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10],4)
        #self.graphicsView.addItem(pg.PlotCurveItem( [1,2],[1,2],pen='r'))
        
        ####################################################
        