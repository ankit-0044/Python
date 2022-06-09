# PyQt Groupbox

# Example : QGroupBox()

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Window(QWidget):              # child class
    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.setGeometry(300,300,500,300)       # main window geometry
        self.setWindowTitle("PyQt GroupBox")    # main window title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # main window icon

        self.Initwindow()               # calling method

        self.show()                     # showing all windows

    def Initwindow(self):               # creating method
        self.grid = QGridLayout()       # initializing QGridLayout()
        self.grid.addWidget(self.createLayout(),0,0)    # adding createlayout() method on grid layout
        self.grid.addWidget(self.createLayout(),1,0)
        self.grid.addWidget(self.createLayout(),0,1)
        self.grid.addWidget(self.createLayout(),1,1)
        
        self.setLayout(self.grid)       # setting grid layout on main window
        
    def createLayout(self):             # creating method
        self.groupbox = QGroupBox("Best Food")  # initializing QGroupBox()
        self.groupbox.setStyleSheet("background-color: antiquewhite; color : teal") # box color

        self.rb1 = QRadioButton("Radio Pizza")          # initilaizing QRadioButton
        self.rb1.setIcon(QIcon("Python Gui\pizza.png")) # radiobutton icon
        self.rb2 = QRadioButton("Radio taco")
        self.rb2.setIcon(QIcon("Python Gui\Taco.png"))
        self.rb3 = QRadioButton("Radio burrito")
        self.rb3.setIcon(QIcon("Python Gui\Burrito.png"))

        self.rb1.setChecked(True)                       # setting rb1 checked by default

        self.vbox = QVBoxLayout()                       # initializing QVBoxLayout()
        self.vbox.addWidget(self.rb1)                   # adding radiobutton on vbox
        self.vbox.addWidget(self.rb2)
        self.vbox.addWidget(self.rb3)
        self.vbox.addStretch(1)                         # adding sapce

        self.groupbox.setLayout(self.vbox)              # setting vbox on groupbox

        return self.groupbox                            # returning 

if __name__=="__main__":
    app = QApplication(sys.argv)                        # initializing PyQt
    app.setStyle('Fusion')                              # app style
    window = Window()                                   # class object
    sys.exit(app.exec())                               # starting loop and exiting windows