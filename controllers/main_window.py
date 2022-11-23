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


        #set0 = QBarSet("Tesla")
        #set1 = QBarSet("Google")
        #set2 = QBarSet("Amazon")
        #set3 = QBarSet("Facebook")
        #set4 = QBarSet("WeChat")

        #set0.append([1, 2, 3,  4, 5, 6])
        #set1.append([5, 0, 0,  4, 0, 7])
        #set2.append([3, 5, 8, 13, 8, 5])
        #set3.append([5, 6, 7,  3, 4, 5])
        #set4.append([9, 7, 5,  3, 1, 2])

        #series = QPercentBarSeries()
        #series.append(set0)
        #series.append(set1)
        #series.append(set2)
        #series.append(set3)
        #series.append(set4)


       

        #sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        #self.chart_view.setSizePolicy(sizePolicy)
        #self.chart_view.setMinimumSize(QSize(0, 300))
        #self.widget.addWidget(self.chart_view, 0, 0,  9, 9)
        #self.ui.frame.setStyleSheet(u"background-color: transparent")

        #######################
        #self.graphicsView.setBackground('w')
        #bars = BarGraphItem(x=[1,2,3,4,5], height=[1,2,3,4,5], width=0.3)
        #item = QGraphicsEllipseItem(0, 0, 60, 40)
        #item.setPen(QPen(QColor("white")))
        #self.graphicsView.addItem(bars)
    
        #self.graphicsView = plot()
        #self.graphicsView.addItem(bars)
        #self.graphicsView.addItem(bars)

        #self.graphicsView.addLabel(text = "Hello ",row = 0 ,col =0 )

        #self.graphicsView.addPlot(row = 0 ,col =1 )
        #self.graphicsView.addViewBox(row = 1 ,col =0,colspan = 2 )


        #self.chart = QChart()
        #self.chart.addSeries(self.barSeries)
        #self.chart.addSeries(self.lineSeries)
        #self.chart.setTitle("Line and barchart example")

        #set0 = QBarSet("Parwiz")
        #set0 << 1 << 2 << 3 << 4 << 5 << 6

        #series = self.recipes_table = QPercentBarSeries()
        #series.append(set0)

        #set0 = QBarSet("Parwiz")
        #set1 = QBarSet("Bob")
        #set2 = QBarSet("Tom")
        #set3 = QBarSet("Logan")
        #set4 = QBarSet("Karim")
 
        #set0 << 1 << 2 << 3 << 4 << 5 << 6
        #set1 << 5 << 0 << 0 << 4 << 0 << 7
        #set2 << 3 << 5 << 8 << 13 << 8 << 5
        #set3 << 5 << 6 << 7 << 3 << 4 << 5
        #set4 << 9 << 7 << 5 << 3 << 1 << 2

        #series = QPercentBarSeries()
        #series.append(set0)



        #self.graphicsView = QChart()
        #self.graphicsView.addSeries(series)
        #self.graphicsView.setTitle("Percent Example")
        #self.graphicsView.setBackground('w')
        #self.graphicsView.setXRange(0, 5)
        #self.graphicsView.setYRange(0, 200)
        #self.graphicsView.plotItem.showGrid(x=True, y=True)
        #self.graphicsView.plotItem.setLabel('left', 'Piezas', units='pz')
        #self.graphicsView.plotItem.setLabel('bottom', 'Operadores')

        #self.x = [1, 2, 3]
        #self.y = [randint(0, 100) for i in range(3)]
        #pen = pg.mkPen(color=(255, 0, 0))
        #self.data_line =  self.graphicsView.plot(self.x, self.y, pen=pen)
        #self.graphicsView.plotItem.setLabel('right', 'Tiempo', units='min')
        #self.graphicsView.plotItem.setLabel('top', 'Tiempo', units='min')
        #self.graphicsView.plotItem.showAxis('top')
        #self.graphicsView.plotItem.showAxis('right')
        #self.graphicsView.plotItem.getAxis('right').setPen('r')
        #self.graphicsView.plotItem.getAxis('right').setLabel('Tiempo', units='min')

        #self.graphicsView.plotItem.getAxis('right').setStyle(tickTextOffset=10)
        #self.graphicsView.plotItem.getAxis('right').setWidth(50)
        
        #self.graphicsView.plotItem.getAxis('right').setHeight(50)
        #self.graphicsView.plotItem.getAxis('right').setTickSpacing(10, 5)
        #self.graphicsView.plotItem.getAxis('right').setTicks([[(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50'), (60, '60'), (70, '70'), (80, '80'), (90, '90'), (100, '100'), (110, '110'), (120, '120'), (130, '130'), (140, '140'), (150, '150'), (160, '160'), (170, '170'), (180, '180'), (190, '190'), (200, '200')]])
        #self.graphicsView.plotItem.getAxis('right').setTicks([[(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50'), (60, '60'), (70, '70'), (80, '80'), (90, '90'), (100, '100'), (110, '110'), (120, '120'), (130, '130'), (140, '140'), (150, '150'), (160, '160'), (170, '170'), (180, '180'), (190, '190'), (200, '200')]])
        #self.graphicsView.plotItem.getAxis('right').setTicks([[(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50'), (60, '60'), (70, '70'), (80, '80'), (90, '90'), (100, '100'), (110, '110'), (120, '120'), (130, '130'), (140, '140'), (150, '150'), (160, '160'), (170, '170'), (180, '180'), (190, '190'), (200, '200')]])

        #self.recipes_table.setColumnCount(10)

        #self.recipes_table.setColumnCount(9)
        #self.graphicsView = QGraphicsView(self)
        #self.graphicsView.backgroundBrush()
        #self.graphicsView.setObjectName("graphicsView")
        #self.graphicsView.setGeometry(0, 0, 1000, 1000)
        #self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 25);")
        #self.graphicsView.setFrameShape(QFrame.NoFrame)
        #self.graphicsView.setFrameShadow(QFrame.Plain)
        #self.graphicsView.setLineWidth(0)
        #self.graphicsView.setMidLineWidth(0)
        #self.graphicsView.)
        #

        # self.graphicsView = PlotWidget(self)
        #self.graphicsView.setMouseTracking(True)
        #self.graphicsView.viewport().installEventFilter(self)
        #self.graphicsView.setObjectName("graphicsView")
        #self.setCentralWidget(self.graphicsView)
        
        #self.graphicsView.plot([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10],4)
        
        column_labels = ("ID", "NOMBRE USUARIO","NOMBRE PROCESO", "NOMBRE MAQUINA", "NOMBRE PIEZA", "HORA INICIO", "HORA TERMINO", "NUMERO PIEZAS","PESO MERMA", "OBSERVACIONES ")
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
