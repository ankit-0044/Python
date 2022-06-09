# PyQt tablewidget

# Example : QTableWidget()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class window(QWidget):              # child class
    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.setGeometry(300,300,340,200)           # main window position and size
        self.setWindowTitle("PyQt TableWidget")     # main window title
        self.setWindowIcon(QIcon('Python Gui\home.png'))    # main window icon

        self.createTable()                      # function call

        self.layout = QVBoxLayout()                 # initializing QVBoxLayout (vertical box)
        self.layout.addWidget(self.tableWidget)     # setting tableWidget on VBoxLayout
        self.setLayout(self.layout)                 # setting VBoxLayout on main window

        self.show()                                 # showing all windows
    
    def createTable(self):                          # function
        self.tableWidget = QTableWidget()           # initializing QTableWidget
        self.tableWidget.setRowCount(4)             # row count
        self.tableWidget.setColumnCount(2)          # column count

        self.tableWidget.setItem(0,0, QTableWidgetItem('Name'))     # table items
        self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))

        self.tableWidget.horizontalHeader().setStretchLastSection(True)     # setting table screen horizontally
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

if __name__ == "__main__":
    app = QApplication(sys.argv)        # initializing PyQt
    window_obj = window()               # class object
    sys.exit(app.exec_())               # starting loop and exit window