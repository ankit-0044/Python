# PyQt progressbar

# Example : QProgressBar()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ProgressBar(QMainWindow):     # child class 

    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.label = QLabel("ProgressBar",self)     # initializing QLabel with name 'ProgressBar'
        self.label.move(85,30)                      # label position
        self.label.resize(150,50)                   # label size
        self.label.setFont(QFont('Aerial',12))      # label font
        
        self.pbar = QProgressBar(self)              # initializing QProgressBar()
        self.pbar.setGeometry(60,80,200,25)         # progressbar position and size
        self.pbar.setValue(0)                       # progressbar initial value

        self.button = QPushButton("Start",self)     # initializing QPushButton() with name 'Start'
        self.button.setGeometry(100,130,80,30)      # button position and size
        self.button.clicked.connect(self.doAction)  # connecting button click event to a function 'doAction'
        
        self.setWindowTitle("PyQt ProgressBar")     # main window title
        self.setGeometry(300,300,350,200)           # main window position and size
        self.show()                                 # showing all windows

    def doAction(self):                             # when button is pressed this function calls
        self.timer = QTimer()                       # initializing QTimer() for time
        self.timer.timeout.connect(self.handleTimer)    # connecting timer timeout to a function 'handleTimer'
        self.timer.start(250)                       # starting timer at 250 miliseconds


    def handleTimer(self):                          # when timer start this function calls
        value = self.pbar.value()                   # taking initial value of progressbar
        if value < 100:                             # condition
            value = value + 1                       # incrementing value by 1
            self.pbar.setValue(value)               # setting incremented value to progressbar

        else:                                       # else condition
            self.timer.stop()                       # stop timer

if __name__=="__main__":            
    app = QApplication(sys.argv)                    # initializing PyQt
    ProgressBar_obj = ProgressBar()                 # class object
    sys.exit(app.exec_())                           # exit all windows