# PyQt tooltip

# EXample : setToolTipDuration()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Window(QMainWindow):          # child class
    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.setGeometry(300,300,400,200)        # main window geometry
        self.setWindowTitle("PyQt ToolTip")      # title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # icon

        self.createlayout()         # calling method

        self.show()                 # showing all windows

    def createlayout(self):         # creating method
        label = QLabel(self)        # initializing QLabel()
        label.setText("Label Widget")   # setting text on label
        label.move(150,100)             # lable positon
        label.setStyleSheet("border :3px solid black;") # label border color
        label.setToolTip("This tooltip is for 5 seconds")   # setting tooltip
        label.setToolTipDuration(5000)                  # tooltip time duration

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    app.exec_()