# PyQt menubar

# Example : QMenuBar ()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,500,300)
        self.setWindowTitle("PyQt MenuBar")
        self.setWindowIcon(QIcon("Python Gui\home.png"))
        self.createLayout()
        self.show()
    
    def createLayout(self):
        layout = QGridLayout()
        self.setLayout(layout)

        menubar = QMenuBar()        # initializing QMenuBar ()
        layout.addWidget(menubar,0,0)   # adding to  grid layout at 0,0

        actionFile = menubar.addMenu("File")    # adding menu file
        actionFile.addAction("New")             # menu action
        actionFile.addAction("Open")
        actionFile.addAction("Save")

        actionFile.addSeparator()               # menu separator
        actionFile.addMenu("Quit")              

        menubar.addMenu("Edit")                 # adding menu edit
        menubar.addMenu("View")
        menubar.addMenu("Help")

        tbox = QPlainTextEdit()                 # initilaizing QPlainTextEdit()
        layout.addWidget(tbox,1,0)              # adding text field at 1,0

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    sys.exit(app.exec_())