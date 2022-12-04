from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.part_menu import DetailWindow
from database.proceso import DBProceso
from database.pieza import DBPieza
from controllers.add_part_window import AddPartWindowForm 
from controllers.edit_part_window import EditPartWindow
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.delete_part_window import DeletePartWindow

class PartMenuForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        self.set_table_data()
        self.view_button.clicked.connect(self.createPart)
        self.edit_button.clicked.connect(self.EditPart)
        self.finish_button.clicked.connect(self.deletePart)

    def deletePart(self):
        self.part_machine_window = DeletePartWindow()
        self.part_machine_window.show()
        self.close()

    def EditPart(self):
        self.part_machine_window = EditPartWindow()
        self.part_machine_window.show()
        self.close()

    def createPart(self):
        self.part_machine_window = AddPartWindowForm()
        self.part_machine_window.show()
        self.close()


    def config_table(self):
        column_labels = ("ID", "NOMBRE PARTE")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_table(self, data):
        self.tableWidget.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            print(index_row)
            print(row)
            for (index_cell, cell) in enumerate(row):
                print("cell")
                print(cell)
                self.tableWidget.setItem(
                     index_row, index_cell, QTableWidgetItem(str(row))
                )
            #agregar los botones a la tabla
            #self.recipes_table.setCellWidget(
            #    index_row, 9, self.build_action_buttons()
            #)
    
    def set_table_data(self):
        usuario = DBPieza()
        usuario_list = usuario.select_name_piezas()
        print(usuario_list)
    
        self.populate_table(usuario_list)

