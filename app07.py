import sys
from math import sin
from threading import Thread
from time import sleep

from PyQt5.QtCore import pyqtSignal, QPointF
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg


class MovingLabelPlot(pg.PlotDataItem):
    sig_new_data = pyqtSignal(list, list)
    data_label = None

    def __init__(self, parent, *args, **kargs):
        self.parent = parent
        super().__init__(*args, **kargs)
        # Connect sig_new_data to setData method
        self.sig_new_data.connect(self.setData)
        # Create our data_label
        self.data_label = pg.TextItem(color="white", fill="gray")
        self.data_label.plotted = False

    def setData(self, *args, **kargs):
        if self.data_label is not None:
            # Check if data_label was already plotted
            if not self.data_label.plotted:
                # Add data_label into scene
                self.scene().addItem(self.data_label)
                self.data_label.plotted = True
            # Get view box
            vb = self.getViewBox()
            # Map last x and y point from view to scene coordinates (pixels)
            scene_pos = vb.mapViewToScene(QPointF(args[0][-1], args[1][-1]))
            # Set label text
            self.data_label.setText(f"+  {round(args[1][-1], 5)}")
            label_rect = self.data_label.boundingRect()
            # Set position of the label to the right and mapped y position
            self.data_label.setPos(self.parent.width() - label_rect.width(),
                                   scene_pos.y() - label_rect.height() / 2)
        super().setData(*args, **kargs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    running = True

    plot_widget = pg.PlotWidget()
    plot_curve = MovingLabelPlot(parent=plot_widget)
    plot_widget.showAxis('right')
    plot_widget.addItem(plot_curve)


    def update_data():
        """Generate sin signal and update plot"""
        x, y = [], []
        index = 0
        while running:
            x.append(index)
            y.append(sin(index * 0.025))
            plot_curve.sig_new_data.emit(y, x)
            index += 1
            sleep(0.01)


    # Start data generator
    Thread(target=update_data).start()
    plot_widget.show()
    app.exec()
    running = False