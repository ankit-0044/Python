# PyQt5 RadioButton

# Example : QRadioButton()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Window(QWidget):      # Child class
    def __init__(self):     
        super().__init__()

        self.InitWindow()       # method call

    def InitWindow(self):       # method
        self.setGeometry(300,300,400,200)       # main window geometry
        self.setWindowTitle("PyQt RadioButton") # title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # icon

        self.createLayout()     # method call

        self.show()             # showing all windows

    def createLayout(self):     # method
        self.layout = QGridLayout()     # initializing QGridLayout
        self.setLayout(self.layout)     # setting grid layout on main window

        rb1 = QRadioButton("Australia")   # initializing QRadioButton with name 'Australia'
        rb1.setChecked(True)              # always checked by default
        rb1.country = "Australia"         # radio button variable
        rb1.toggled.connect(self.onClicked) # connecting check event to the onClicked method
        self.layout.addWidget(rb1,0,0)

        rb2 = QRadioButton("China")
        rb2.country = "China"
        rb2.toggled.connect(self.onClicked)
        self.layout.addWidget(rb2,0,1)

        rb3 = QRadioButton("India")
        rb3.country = "India"
        rb3.toggled.connect(self.onClicked)
        self.layout.addWidget(rb3,0,2)

    def onClicked(self):                # onClicked method
        rb = self.sender()              # check event object value assigning to a variable rb
        if rb.isChecked():              # condition
            print(f"Country is {rb.country}")   # print statement

if __name__=="__main__":                
    app = QApplication(sys.argv)        # initializing PyQt
    window = Window()                   # class object
    sys.exit(app.exec_())               # starting loop and exiting window