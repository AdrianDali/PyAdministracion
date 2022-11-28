from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from PySide6.QtCore import Qt
from interface.graficas_produccion_window import DetailWindow
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
from controllers.proceso_filtrado_window import MainWindowForm as ProcesoFiltradoWindow
from random import randint 
from PyQt5.QtGui import QPainter
#from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis,QBarSet,QPercentBarSeries
#from pyqtgraph.opengl import GLViewWidget
from pyqtgraph import plot,PlotWidget ,PlotItem, PlotDataItem, PlotCurveItem, GraphicsLayoutWidget,BarGraphItem
from datetime import datetime, date 

class MainWindowForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.comboBox_3.addItems(["Dia","Semana","Mes"])
        self.comboBox_2.addItems(["Dia","Semana","Mes"])
        self.comboBox_4.addItems(["Dia","Semana","Mes"])
        self.comboBox.addItems(["Dia","Semana","Mes"])
        #self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10],4)
        ###########Aqui se crea el grafico de barras#######
        #bars = BarGraphItem(x=[1,2,3,4,5], height=[1,2,3,4,5], width=0.3)
        #self.graphicsView.addItem(bars)
        #################################################
        ##########Aui se crea grafica lineal#################
        #info = DBProceso.select_piezas_neto_fecha(self)
        #print("@@@@@@@@@@@@@@@@@@@")
        #print(info)
        self.grafica01()
        self.grafica02()
        self.grafica03()
        self.grafica04()


    def grafica04(self):
        axis = pg.DateAxisItem(orientation='bottom',tickFont=10,spacing=100,utcOffset=0,autoExpandTextSpace=True,showValues=True,showLastLabel=True)      
        #self.line = pg.PlotCurveItem(clear=True, pen="g")
        #self.graphicsView.addItem(self.line)
        self.graphicsView_4.setAxisItems({"bottom": axis})
        self.graphicsView_4.showGrid(x=True, y=True)
        #etiqueta nombre prouccion
        self.graphicsView_4.setLabel('left', "Piezas")
        #etiqueta tiempo 
        self.graphicsView_4.setLabel('bottom', "Dia")
        self.graphicsView_4.setMouseEnabled(x=False, y=False)
        list_x = [ 
        datetime(2022, 10, 2),
        datetime(2022, 10, 10),
        datetime(2022, 10, 4),
        datetime(2022, 10, 5),
        datetime(2022, 10, 6),
        datetime(2022, 10, 7),
        datetime(2022, 10, 8),
        datetime(2022, 10, 9),
        datetime(2022, 10, 10),
        datetime(2022, 10, 11),
        datetime(2022, 10, 12),
        datetime(2022, 10, 13),
        datetime(2022, 10, 14),
        datetime(2022, 10, 15),
        datetime(2022, 10, 16),
        datetime(2022, 10, 17),
        datetime(2022, 10, 18),
        datetime(2022, 10, 19),
        datetime(2022, 10, 20),
        datetime(2022, 10, 21),
        datetime(2022, 10, 22),
        datetime(2022, 10, 23),
        datetime(2022, 10, 24),
        datetime(2022, 10, 25),
        datetime(2022, 10, 26),
        datetime(2022, 10, 27),
        datetime(2022, 10, 28),
        datetime(2022, 10, 29),
        datetime(2022, 10, 30),
        ]
        self.graphicsView_4.addLegend()
        list_y = [ 150,111, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100] 
        
        list_yy = [ 250,311, 400, 800 , 200, 150, 400, 900 , 100, 150,500, 800 , 100, 550, 200, 900 , 100, 250, 200, 300 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100] 
        users_name = DBUsuario.select_name_usuario(self)
        lista_colores = ["red", "white", "green", "blue", "yellow", "black", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta", "darkRed", "darkGreen", "darkBlue", "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray"]
        print(users_name)

        i= 0
        for user in users_name:
            lista_piezas = []
            for list in list_x:
                users_piezas_neto = DBProceso.select_piezas_neto_fecha_user(self,day = str(list), user = user)
                lista_piezas.append(users_piezas_neto)
            print("Usuario: "  + user + " Fecha: " + str(list)  + "  Piezas neto: "  + str(lista_piezas))
                
            self.graphicsView_4.addItem(PlotCurveItem(x = [x.timestamp() for x in list_x], y = lista_piezas, pen = lista_colores[i], name = user[0]))
            i = i + 1

    
    def grafica03(self):
        axis = pg.DateAxisItem(orientation='bottom',tickFont=10,spacing=100,utcOffset=0,autoExpandTextSpace=True,showValues=True,showLastLabel=True)      
        #self.line = pg.PlotCurveItem(clear=True, pen="g")
        #self.graphicsView.addItem(self.line)
        self.graphicsView_3.setAxisItems({"bottom": axis})
        self.graphicsView_3.showGrid(x=True, y=True)
        #etiqueta nombre prouccion
        self.graphicsView_3.setLabel('left', "Peso(gr)")
        #etiqueta tiempo 
        self.graphicsView_3.setLabel('bottom', "Dia")
        self.graphicsView_3.setMouseEnabled(x=False, y=False)
        list_x = [datetime(2018, 3, 2),
        datetime(2018, 3, 3),
        datetime(2018, 3, 4),
        datetime(2018, 3, 5),
        datetime(2018, 3, 6),
        datetime(2018, 3, 7),
        datetime(2018, 3, 8),
        datetime(2018, 3, 9),
        datetime(2018, 3, 10),
        datetime(2018, 3, 11),
        datetime(2018, 3, 12),
        datetime(2018, 3, 13),
        datetime(2018, 3, 14),
        datetime(2018, 3, 15),
        datetime(2018, 3, 16),
        datetime(2018, 3, 17),
        datetime(2018, 3, 18),
        datetime(2018, 3, 19),
        datetime(2018, 3, 20),
        datetime(2018, 3, 21),
        datetime(2018, 3, 22),
        datetime(2018, 3, 23),
        datetime(2018, 3, 24),
        datetime(2018, 3, 25),
        datetime(2018, 3, 26),
        datetime(2018, 3, 27),
        datetime(2018, 3, 28),
        datetime(2018, 3, 29),
        datetime(2018, 3, 30),]

        self.graphicsView_3.addLegend()
        proceso = DBProceso() 
        lista_grafica = []
        for i in range(29):
            lista_grafica.append(proceso.select_peso_fecha(i))
            print("PRCOSEOSDASODASD")
        
        list_y = [100, 150, 200, 800]
        line=PlotCurveItem(x=[x.timestamp() for x in list_x],y=lista_grafica,pen='r',name="Peso(gr)")
        self.graphicsView_3.addItem(line)
        
        ####################################################


    def grafica02(self):
        axis = pg.DateAxisItem(orientation='bottom',tickFont=10,spacing=100,utcOffset=0,autoExpandTextSpace=True,showValues=True,showLastLabel=True)      
        #self.line = pg.PlotCurveItem(clear=True, pen="g")
        #self.graphicsView.addItem(self.line)   
        self.graphicsView_2.setAxisItems({"bottom": axis})
        self.graphicsView_2.showGrid(x=True, y=True)
        #etiqueta nombre prouccion
        self.graphicsView_2.setLabel('left', "Peso(gr)")
        #etiqueta tiempo 
        self.graphicsView_2.setLabel('bottom', "Dia")
        self.graphicsView_2.setMouseEnabled(x=False, y=False)
        list_x = [ 
        datetime(2018, 3, 2),
        datetime(2018, 3, 3),
        datetime(2018, 3, 4),
        datetime(2018, 3, 5),
        datetime(2018, 3, 6),
        datetime(2018, 3, 7),
        datetime(2018, 3, 8),
        datetime(2018, 3, 9),
        datetime(2018, 3, 10),
        datetime(2018, 3, 11),
        datetime(2018, 3, 12),
        datetime(2018, 3, 13),
        datetime(2018, 3, 14),
        datetime(2018, 3, 15),
        datetime(2018, 3, 16),
        datetime(2018, 3, 17),
        datetime(2018, 3, 18),
        datetime(2018, 3, 19),
        datetime(2018, 3, 20),
        datetime(2018, 3, 21),
        datetime(2018, 3, 22),
        datetime(2018, 3, 23),
        datetime(2018, 3, 24),
        datetime(2018, 3, 25),
        datetime(2018, 3, 26),
        datetime(2018, 3, 27),
        datetime(2018, 3, 28),
        datetime(2018, 3, 29),
        datetime(2018, 3, 30),
        ]
        self.graphicsView_2.addLegend()
        list_y = [ 150,111, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100] 
        
        list_yy = [ 250,311, 400, 800 , 200, 150, 400, 900 , 100, 150,500, 800 , 100, 550, 200, 900 , 100, 250, 200, 300 , 100, 150, 200, 800 , 100, 150, 200, 800 , 100] 
        users_name = DBUsuario.select_name_usuario(self)
        lista_colores = ["red", "white", "green", "blue", "yellow", "black", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta", "darkRed", "darkGreen", "darkBlue", "darkCyan", "darkMagenta", "darkYellow", "darkGray", "lightGray"]
        print(users_name)

        i= 0
        for user in users_name:
            lista_piezas = []
            for list in list_x:
                users_piezas_neto = DBProceso.select_peso_neto_fecha_user(self,day = str(list), user = user)
                lista_piezas.append(users_piezas_neto)
            print("Usuario: "  + user + " Fecha: " + str(list)  + "   PESO NETO: "  + str(lista_piezas))
                
            self.graphicsView_2.addItem(PlotCurveItem(x = [x.timestamp() for x in list_x], y = lista_piezas, pen = lista_colores[i], name = user[0]))
            i = i + 1
    


    def grafica01(self):
        axis = pg.DateAxisItem(orientation='bottom',tickFont=10,spacing=100,utcOffset=0,autoExpandTextSpace=True,showValues=True,showLastLabel=True)      
        #self.line = pg.PlotCurveItem(clear=True, pen="g")
        #self.graphicsView.addItem(self.line)
        self.graphicsView.setAxisItems({"bottom": axis})
        self.graphicsView.showGrid(x=True, y=True)
        #etiqueta nombre prouccion
        self.graphicsView.setLabel('left', "Produccion")
        #etiqueta tiempo 
        self.graphicsView.setLabel('bottom', "Dia")
        self.graphicsView.setMouseEnabled(x=False, y=False)
        list_x = [datetime(2018, 3, 2),
        datetime(2018, 3, 3),
        datetime(2018, 3, 4),
        datetime(2018, 3, 5),
        datetime(2018, 3, 6),
        datetime(2018, 3, 7),
        datetime(2018, 3, 8),
        datetime(2018, 3, 9),
        datetime(2018, 3, 10),
        datetime(2018, 3, 11),
        datetime(2018, 3, 12),
        datetime(2018, 3, 13),
        datetime(2018, 3, 14),
        datetime(2018, 3, 15),
        datetime(2018, 3, 16),
        datetime(2018, 3, 17),
        datetime(2018, 3, 18),
        datetime(2018, 3, 19),
        datetime(2018, 3, 20),
        datetime(2018, 3, 21),
        datetime(2018, 3, 22),
        datetime(2018, 3, 23),
        datetime(2018, 3, 24),
        datetime(2018, 3, 25),
        datetime(2018, 3, 26),
        datetime(2018, 3, 27),
        datetime(2018, 3, 28),
        datetime(2018, 3, 29),
        datetime(2018, 3, 30),]
        self.graphicsView.addLegend()

        proceso = DBProceso() 
        lista_grafica = []
        for i in range(29):
            lista_grafica.append(proceso.select_piezas_neto_fecha(i))
            print("PRCOSEOSDASODASD")
        
        list_y = [100, 150, 200, 800]
        line=PlotCurveItem(x=[x.timestamp() for x in list_x],y=lista_grafica,pen='r',name="Piezas Netas",symbol='o',symbolPen='r',symbolBrush=0.2,symbolSize=5)
        #line.addLegend()
        self.graphicsView.addItem(line)
        
        ####################################################
        
        