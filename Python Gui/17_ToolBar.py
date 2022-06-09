# PyQt toolbar

# Example : QToolBar()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        # main window
        self.setGeometry(300,300,400,200)
        self.setWindowTitle("PyQt ToolBar")
        self.setWindowIcon(QIcon("Python Gui\home.png"))
        
        # calling method
        self.createLayout()
        
        # showing all windows
        self.show()

    def createLayout(self):
        # creating layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # creating QToolBar
        self.toolbar = QToolBar()
        self.layout.addWidget(self.toolbar)

        # add buttons to the toolbar
        self.toolbutton = QToolButton()
        self.toolbutton.setText("Apple")
        self.toolbutton.setIcon(QIcon("Python Gui\\apple.png"))
        self.toolbutton.setCheckable(True)
        self.toolbutton.setAutoExclusive(True)
        self.toolbar.addWidget(self.toolbutton)

        self.toolbutton1 = QToolButton()
        self.toolbutton1.setText("Orange")
        self.toolbutton1.setIcon(QIcon("Python Gui\orange.png"))
        self.toolbutton1.setCheckable(True)
        self.toolbutton1.setAutoExclusive(True)
        self.toolbar.addWidget(self.toolbutton1)

        # add textfield to window
        self.tbox = QPlainTextEdit()
        self.layout.addWidget(self.tbox)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec()