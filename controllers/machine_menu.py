from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from interface.machine_menu import DetailWindow
from database.proceso import DBProceso
from database.maquina import DBMaquina
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi
from controllers.add_machine_window import PartMachineWindow
from controllers.edit_machine_window import EditMachineWindow
from controllers.delete_machine_window import DeleteMachineWindow


class MachineMenuForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        self.set_table_data()
        self.view_button.clicked.connect(self.view_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.finish_button.clicked.connect(self.finish_button_clicked)

    def finish_button_clicked(self):
        delete_machine = DeleteMachineWindow()
        delete_machine.show()
        self.close()

    def edit_button_clicked(self):
        edit_machine = EditMachineWindow()
        edit_machine.show()
        self.close()

    def view_button_clicked(self):
        new_machine = PartMachineWindow()
        new_machine.show()
        self.close()


    def config_table(self):
        column_labels = ("ID" , "NOMBRE MAQUINA")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(1, 300)
        
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
                    index_row, index_cell, QTableWidgetItem(row)
                )
            #agregar los botones a la tabla
            #self.recipes_table.setCellWidget(
            #    index_row, 9, self.build_action_buttons()
            #)
    
    def set_table_data(self):
        maquina = DBMaquina()
        maquina_list = maquina.select_name_maquinas_enabled()
        print(maquina_list)

        self.populate_table(maquina_list)
