# PyQt progressbar

# Example : QProgressBar ()


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ProgressBar(QWidget):                     # child class

    def __init__(self):                         # child class constructor
        super().__init__()                      # parent class constructor

        self.window()                           # function calling inside child class constructor

    def window(self):                           # function

        self.label = QLabel("ProgressBar",self) # initializing QLable with name 'ProgressBar'
        self.label.move(140,80)                 # lable position
        self.label.setFont(QFont("Aerial",12))  # lable font

        self.pbar = QProgressBar(self)          # initializing QProgressBar()
        self.pbar.setGeometry(100,120,250,25)   # pbar position and size

        self.button = QPushButton("Start",self) # initializing QPushButton()
        self.button.move(160,160)
        self.button.clicked.connect(self.doAction)  # when the the button se pressed doAction function is called

        self.timer = QBasicTimer()              # initializing QBasicTimer() for time events
        self.step = 0                           # initilaizing a variable step

        self.setGeometry(300,300,400,250)       # main window position and size
        self.setWindowTitle("PyQt ProgressBar") # main window title
        self.show()                             # showing all the windows

    def timerEvent(self,e):                     # timerEvent function from QBasicTimer for handling time event
        if self.step >= 100:                    # condition
            self.timer.stop()                   # stop timer
            self.button.setText('Finished')     # changing button text
            return

        self.step = self.step + 1               # incrementing step variable
        self.pbar.setValue(self.step)           # setting pbar value 

    def doAction(self):                         # doAction function for handling button pressing
        if self.timer.isActive():               # condition
            self.timer.stop()                   # stop timer
            self.button.setText("Start")        # change button text
        else:
            self.timer.start(100,self)          # start timer with 100 miliseconds
            self.button.setText("Stop")         # change button text

def main():
    app = QApplication(sys.argv)
    ProgressBar_Obj = ProgressBar()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()