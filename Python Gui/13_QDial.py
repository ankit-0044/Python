# PyQt dial

# Example : QDial()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Window(QWidget):          # child class
    def __init__(self):
        super().__init__()

        self.initwindow()           # calling initwindow()

    def initwindow(self):
        self.setGeometry(300,300,340,200)           # main window geometry
        self.setWindowIcon(QIcon("Python Gui\home.png"))        # main window icon
        self.setWindowTitle("PyQt Dial")                    # main window title

        self.createLayout()             # calling createLayout()
    
        self.show()                     # showing all the windows
    
    def createLayout(self):
        self.layout = QGridLayout()     # initializing QGridlayout
        self.setLayout(self.layout)     # setting grid layout on main window

        self.dial = QDial()             # initializing QDial
        self.dial.setMinimum(0)         # dial minimum value
        self.dial.setMaximum(100)       # dial maximum value
        self.dial.setValue(20)          # dial default(initial) value
        self.dial.valueChanged.connect(self.sliderMoved)        # dial value change event connecting to sliderMoved function

        self.layout.addWidget(self.dial)            # adding dial to layout widget
    
    def sliderMoved(self):
        print("Dial value = %i" %(self.dial.value()))   # printing dial value

if __name__=="__main__":
    app = QApplication(sys.argv)                # initializing PyQt
    window = Window()
    sys.exit(app.exec_())