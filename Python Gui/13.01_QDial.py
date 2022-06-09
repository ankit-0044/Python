# PyQt dial

# Example : QDial()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):      # child class
    def __init__(self):
        super().__init__()

        self.Initwindow()       # method call

    def Initwindow(self):       # Initwindow method
        self.setGeometry(300,300,380,200)
        self.setWindowTitle("PyQt Dial")
        self.setWindowIcon(QIcon("Python Gui\home.png"))

        self.createLayout()         # method call
        self.show()

    def createLayout(self):         # createLayout method
        self.grid = QHBoxLayout()   # initializing QHBoxLayout
        self.setLayout(self.grid)   # setting grid to main window

        self.dial = QDial()         # initializing QDial
        self.dial.setGeometry(100,100,100,100)
        self.dial.setStyleSheet("background : olive")       # dial color
        self.dial.valueChanged.connect(self.dial_method)    # connecting dial changing value event to dial_method
        self.grid.addWidget(self.dial)                      # adding dial to grid

        self.label = QLabel("PyQt Dial")        # initializing label
        self.label.setGeometry(220,100,200,60)
        self.label.setWordWrap(True) # allows long words to be able to be broken and wrap onto the next line
        self.grid.addWidget(self.label)

    def dial_method(self):      # dial_method
        value = self.dial.value()   # dial value
        self.label.setText("Current value :"+str(value))        # setting label text to dial value

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')          # setting main window style
    window = Window()
    sys.exit(app.exec_())