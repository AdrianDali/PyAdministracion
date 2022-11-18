import sys 
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg 
import numpy as np 

app = QApplication(sys.argv)
win = pg.plot()

x = np.arange(2)
y1 = np.sin(x)
y2 = 1.1 * np.sin(x+1)
y3 = 1.2 * np.sin(x+2)

bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
#bg2 = pg.BarGraphItem(x=x+0.33, height=y2, width=0.3, brush='g')
#bg3 = pg.BarGraphItem(x=x+0.66, height=y3, width=0.3, brush='b')

win.addItem(bg1)
#win.addItem(bg2)
#win.addItem(bg3)

class BarGraph(pg.BarGraphItem):
    def mouseClickEvent(self, event):
        print("clicked on")


status = app.exec_()
sys.exit(status)
