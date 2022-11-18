from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from database.usuario import DBUsuario
from interface.user_menu import DetailWindow
from controllers.add_edit_user_window import AddEditUserWindowForm
from controllers.edit_user_window import EditUserWindowForm
from controllers.delete_user_window import DeleteUserWindowForm
#from database.proceso import DBProceso
from database.usuario import DBUsuario
#from interface import components
import os
from interface.general_custom_ui import GeneralCustomUi


class UserMenuForm(QWidget,DetailWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        self.set_table_data()
        self.view_button.clicked.connect(self.createUser)
        self.edit_button.clicked.connect(self.editUser)
        self.finish_button.clicked.connect(self.deleteUser)

    def editUser(self):
        print("edit user")
        edit = EditUserWindowForm()
        edit.show()
        self.close()
    
    def deleteUser(self):
        print("delete user")
        delete = DeleteUserWindowForm()
        delete.show()
        self.close()

    def createUser(self):
        print("create user")
        new = AddEditUserWindowForm()
        new.show()
        self.close()
# Path: controllers\user_menu.

    def config_table(self):
        column_labels = ("ID", "NOMBRE USUARIO","FECHA NACIMIENTO")
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
                     index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #agregar los botones a la tabla
            #self.recipes_table.setCellWidget(
            #    index_row, 9, self.build_action_buttons()
            #)
    
    def set_table_data(self):
        usuario = DBUsuario()
        usuario_list = usuario.select_all_info_usuarios()
        print(usuario_list)
    
        self.populate_table(usuario_list)
