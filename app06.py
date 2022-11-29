from pyqtgraph.opengl import GLViewWidget
import pyqtgraph.opengl as gl
from PyQt5.QtGui import QColor
from pyqtgraph.Qt import QtCore, QtGui ,QtWidgets
import sys

class GLView(GLViewWidget):
    """
    I have implemented my own GLViewWidget
    """
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintGL(self, *args, **kwds):
        # Call parent's paintGL()
        GLViewWidget.paintGL(self, *args, **kwds)

        # select font
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPixelSize(21)
        font.setBold(True)

        title_str = 'Screen Coordinates'
        metrics = QtGui.QFontMetrics(font)
        m = metrics.boundingRect(title_str)
        width = m.width()
        height = m.height()

        # Get window dimensions to center text
        scrn_sz_width = self.size().width()
        scrn_sz_height = self.size().height()

        # Render text with screen based coordinates
        self.qglColor(QColor(255,255,0,255))
        self.renderText((scrn_sz_width-width)/2, height+5, title_str, font)

        # Render text using Axis-based coordinates
        self.qglColor(QColor(255, 0, 0, 255))
        self.renderText(0, 0, 0, 'Axis-Based Coordinates')


if __name__ == '__main__':
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    w = GLView()
    w.resize(800, 800)
    w.show()
    w.setWindowTitle('Earth 3D')
    w.setCameraPosition(distance=20)
    g = gl.GLGridItem()
    w.addItem(g)

    while w.isVisible():
        app.processEvents()