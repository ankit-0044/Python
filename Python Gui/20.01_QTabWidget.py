# PyQt tabwidget

# Example : QTabWidget ()

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window
        self.setWindowTitle("PyQt TabWidget")
        self.setWindowIcon(QIcon("Python Gui\home.png"))
        self.setGeometry(200,200,350,200)

        # calling MyTabWidget class
        self.tab_widget = MyTabWidget()
        self.setCentralWidget(self.tab_widget)

        # showing all windows
        self.show()

# widget class
class MyTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300,200)

        # add tabs
        self.tabs.addTab(self.tab1,"Welcome")
        self.tabs.addTab(self.tab2,"To")
        self.tabs.addTab(self.tab3,"Python")

        # create first tab
        self.tab1_layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("This is the first tab.")
        self.tab1_layout.addWidget(self.label)
        self.tab1.setLayout(self.tab1_layout)

        # create second tab
        self.tab2_layout = QGridLayout()
        self.label = QLabel()
        self.label.setText("This is the second tab.")
        self.tab2_layout.addWidget(self.label)
        self.tab2.setLayout(self.tab2_layout)

        # create third tab
        self.tab3_layout = QHBoxLayout()
        self.label = QLabel("This is the third tab.")
        self.tab3_layout.addWidget(self.label)
        self.tab3.setLayout(self.tab3_layout)

        # add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    ex = App()
    sys.exit(app.exec_())  