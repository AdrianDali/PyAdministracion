# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficas_produccion_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(1402, 840)
        DetailWindow.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
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
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
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
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
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
        self.close_button.setGeometry(QRect(90, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView_3 = PlotWidget(self.frame)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.gridLayout.addWidget(self.graphicsView_3, 4, 0, 1, 1)

        self.action_bar_frame_5 = QFrame(self.frame)
        self.action_bar_frame_5.setObjectName(u"action_bar_frame_5")
        self.action_bar_frame_5.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_5.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.action_bar_frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.comboBox_3 = QComboBox(self.action_bar_frame_5)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_8.addWidget(self.comboBox_3)


        self.gridLayout.addWidget(self.action_bar_frame_5, 5, 0, 1, 1)

        self.action_bar_frame_14 = QFrame(self.frame)
        self.action_bar_frame_14.setObjectName(u"action_bar_frame_14")
        self.action_bar_frame_14.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_14.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.action_bar_frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.title_label_5 = QLabel(self.action_bar_frame_14)
        self.title_label_5.setObjectName(u"title_label_5")
        self.title_label_5.setFont(font)
        self.title_label_5.setStyleSheet(u"color: black;")
        self.title_label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.title_label_5)


        self.gridLayout.addWidget(self.action_bar_frame_14, 3, 1, 1, 1)

        self.action_bar_frame_4 = QFrame(self.frame)
        self.action_bar_frame_4.setObjectName(u"action_bar_frame_4")
        self.action_bar_frame_4.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_4.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.action_bar_frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBox_4 = QComboBox(self.action_bar_frame_4)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_7.addWidget(self.comboBox_4)


        self.gridLayout.addWidget(self.action_bar_frame_4, 5, 1, 1, 1)

        self.action_bar_frame_13 = QFrame(self.frame)
        self.action_bar_frame_13.setObjectName(u"action_bar_frame_13")
        self.action_bar_frame_13.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_13.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.action_bar_frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.title_label_3 = QLabel(self.action_bar_frame_13)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setFont(font)
        self.title_label_3.setStyleSheet(u"color: black;")
        self.title_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.title_label_3)


        self.gridLayout.addWidget(self.action_bar_frame_13, 0, 1, 1, 1)

        self.graphicsView = PlotWidget(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.action_bar_frame_9 = QFrame(self.frame)
        self.action_bar_frame_9.setObjectName(u"action_bar_frame_9")
        self.action_bar_frame_9.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_9.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.action_bar_frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBox = QComboBox(self.action_bar_frame_9)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_12.addWidget(self.comboBox)


        self.gridLayout.addWidget(self.action_bar_frame_9, 2, 0, 1, 1)

        self.action_bar_frame_11 = QFrame(self.frame)
        self.action_bar_frame_11.setObjectName(u"action_bar_frame_11")
        self.action_bar_frame_11.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_11.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.action_bar_frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.title_label_2 = QLabel(self.action_bar_frame_11)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet(u"color: black;")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.title_label_2)


        self.gridLayout.addWidget(self.action_bar_frame_11, 0, 0, 1, 1)

        self.graphicsView_2 = PlotWidget(self.frame)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout.addWidget(self.graphicsView_2, 4, 1, 1, 1)

        self.action_bar_frame_12 = QFrame(self.frame)
        self.action_bar_frame_12.setObjectName(u"action_bar_frame_12")
        self.action_bar_frame_12.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_12.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.action_bar_frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.title_label_4 = QLabel(self.action_bar_frame_12)
        self.title_label_4.setObjectName(u"title_label_4")
        self.title_label_4.setFont(font)
        self.title_label_4.setStyleSheet(u"color: black;")
        self.title_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.title_label_4)


        self.gridLayout.addWidget(self.action_bar_frame_12, 3, 0, 1, 1)

        self.action_bar_frame_3 = QFrame(self.frame)
        self.action_bar_frame_3.setObjectName(u"action_bar_frame_3")
        self.action_bar_frame_3.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_3.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.action_bar_frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox_2 = QComboBox(self.action_bar_frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;")

        self.horizontalLayout_6.addWidget(self.comboBox_2)


        self.gridLayout.addWidget(self.action_bar_frame_3, 2, 1, 1, 1)

        self.graphicsView_4 = PlotWidget(self.frame)
        self.graphicsView_4.setObjectName(u"graphicsView_4")

        self.gridLayout.addWidget(self.graphicsView_4, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Graficas de produccion ", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.title_label_5.setText(QCoreApplication.translate("DetailWindow", u"MERMA POR OPERARIO ", None))
        self.title_label_3.setText(QCoreApplication.translate("DetailWindow", u"PRODUCCION POR OPERARIO ", None))
        self.title_label_2.setText(QCoreApplication.translate("DetailWindow", u"PRODUCCION TOTAL  ", None))
        self.title_label_4.setText(QCoreApplication.translate("DetailWindow", u"MERMA TOTAL ", None))
    # retranslateUi

