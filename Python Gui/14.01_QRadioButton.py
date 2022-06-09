# PyQt RadioButton

# Example : QRadioButton()

import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):          # child class
    def __init__(self):
        super().__init__()          # calling parent class constructor

        self.rb1 = QRadioButton("Large",self)   # initializing QRadioButton with name 'Large'
        self.rb1.setGeometry(25,55,70,30)       # radiobutton geometry
        self.rb1.toggled.connect(self.updateLabel)  # connecting radio button check event to the updateLable method

        self.rb2 = QRadioButton("Middle",self)
        self.rb2.setGeometry(120,55,70,30)
        self.rb2.toggled.connect(self.updateLabel)

        self.rb3 = QRadioButton("Small",self)
        self.rb3.setGeometry(220,55,70,30)
        self.rb3.toggled.connect(self.updateLabel)

        self.label = QLabel('',self)                # initializing QLable with no name
        self.label.move(100,100)                    # label position
        self.label.setFont(QFont('Times New Roman',14)) # label font 
        self.label.setAlignment(Qt.AlignCenter)     # lable align to center

        self.setGeometry(300,300,320,200)       # main window geometry
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # main window icon
        self.setWindowTitle("PyQt RadioButton")         # main window name

    def updateLabel(self):              # updatelabel method
        rb = self.sender()              # check event object value assigning to a variable rb
        if rb.isChecked() == True:      # checking radiobutton is checked or not
            self.label.setText(rb.text())   # assigning label another text


if __name__=="__main__":
    app = QApplication(sys.argv)         # initilaizing PyQt
    window = Window()                    # class object
    window.show()                        # showing all windows
    sys.exit(app.exec_())                # starting loop and exit window