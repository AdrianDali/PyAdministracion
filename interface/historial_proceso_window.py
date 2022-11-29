# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historial_proceso_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1460, 567)
        MainWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(245, 240, 225);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #1e3d59;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../../pys6-recipes-organizer/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../../pys6-recipes-organizer/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../../pys6-recipes-organizer/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 21, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_4.addWidget(self.top_bar_frame)

        self.action_bar_frame = QFrame(self.content_frame)
        self.action_bar_frame.setObjectName(u"action_bar_frame")
        self.action_bar_frame.setMinimumSize(QSize(0, 39))
        self.action_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.action_bar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.action_bar_frame_6 = QFrame(self.action_bar_frame)
        self.action_bar_frame_6.setObjectName(u"action_bar_frame_6")
        self.action_bar_frame_6.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_6.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.action_bar_frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.title_label_5 = QLabel(self.action_bar_frame_6)
        self.title_label_5.setObjectName(u"title_label_5")
        self.title_label_5.setFont(font)
        self.title_label_5.setStyleSheet(u"color: black;")

        self.horizontalLayout_9.addWidget(self.title_label_5)

        self.comboBox_2 = QComboBox(self.action_bar_frame_6)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_9.addWidget(self.comboBox_2)


        self.horizontalLayout_2.addWidget(self.action_bar_frame_6)

        self.action_bar_frame_10 = QFrame(self.action_bar_frame)
        self.action_bar_frame_10.setObjectName(u"action_bar_frame_10")
        self.action_bar_frame_10.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_10.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.action_bar_frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.title_label_6 = QLabel(self.action_bar_frame_10)
        self.title_label_6.setObjectName(u"title_label_6")
        self.title_label_6.setFont(font)
        self.title_label_6.setStyleSheet(u"color: black;")

        self.horizontalLayout_13.addWidget(self.title_label_6)

        self.comboBox_5 = QComboBox(self.action_bar_frame_10)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_13.addWidget(self.comboBox_5)


        self.horizontalLayout_2.addWidget(self.action_bar_frame_10)


        self.verticalLayout_4.addWidget(self.action_bar_frame)

        self.tableWidget = QTableWidget(self.content_frame)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.graphicsView_4 = PlotWidget(self.content_frame)
        self.graphicsView_4.setObjectName(u"graphicsView_4")

        self.verticalLayout_4.addWidget(self.graphicsView_4)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Historial Proceso", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.title_label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre Operario:", None))
        self.title_label_6.setText(QCoreApplication.translate("MainWindow", u"Proceso: ", None))
    # retranslateUi

