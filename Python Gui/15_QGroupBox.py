# PyQt GroupBox

# Example : QGroupBox ()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Window(QWidget):          # child class
    def __init__(self):         # child class constructor
        super().__init__()      # calling parent class constructor

        self.setGeometry(300,300,340,200)       # main window positon and size
        self.setWindowTitle("PyQt GroupBox")    # main window title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # main window logo

        self.createLayout()         # calling method

        self.show()                 # showing all windows

    def createLayout(self):         # method
        self.layout = QGridLayout() # initializing QGridLayout()
        self.setLayout(self.layout) # setting grid layout on main window

        self.groupbox = QGroupBox("GroupBox Example")   # initializing QGroupBox() with name 'GroupBox Example'
        self.groupbox.setCheckable(True)                # setting default check 
        self.layout.addWidget(self.groupbox)            # adding groupbox to grid layout

        self.vbox = QVBoxLayout()                       # initializing QVBoxLayout
        self.groupbox.setLayout(self.vbox)              # setting VBox to on a groupbox

        self.rb = QRadioButton("RadioButton 1")         # initiallizing QRadioButton
        self.vbox.addWidget(self.rb)                    # adding radiobutton on vbox

        self.rb2 = QRadioButton("RadioButton 2")
        self.vbox.addWidget(self.rb2)

        self.rb3 = QRadioButton("RadioButton 3")
        self.vbox.addWidget(self.rb3)

if __name__=="__main__":
    app = QApplication(sys.argv)                        # initializing PyQt
    app.setStyle('Fusion')
    window = Window()                                   # class object
    sys.exit(app.exec_())                               # starting loop and exiting window