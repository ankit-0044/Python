# PyQt tabwidget

# Example : QTabWidget ()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()      # initializing QGridLayout()
        self.setLayout(layout)      # setting grid layout to main window

        label1 = QLabel("Widget in Tab 1.")     # initializing label
        label2 = QLabel("Widget in Tab 2.")

        tabwidget = QTabWidget()        # initiallizing QTabWidget()
        tabwidget.addTab(label1,"Tab 1")    # adding label to tab1
        tabwidget.addTab(label2,'Tab 2')    # adding lable to tab2
        
        layout.addWidget(tabwidget,0,0)     # adding tabwidget to grid layout
        
        # main window
        self.setWindowTitle("PyQt Tabwidget")
        self.setWindowIcon(QIcon("Python Gui\home.png"))
        self.setGeometry(200,200,350,150)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())