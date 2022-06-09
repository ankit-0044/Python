# PyQt checkbox

# Example : QCheckBox ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CheckBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        grid = QGridLayout()
        self.setLayout(grid)

        check_box = QCheckBox('You have a Dog')     # initializing QCheckBox with name 'You hava a Dog'
        check_box.move(50,50)                       # checkbox position
        check_box.setChecked(True)                  # setting checkbox to always True(already ticked)
        check_box.animal = "Dog"                    # checkbox variable animal
        check_box.toggled.connect(self.onClicked)   # checkbox ticked event connecting to a specified function
        grid.addWidget(check_box,0,0)               # setting checkbox on a grid layout 
        self.setWindowTitle("PyQt CheckBox")        # window title
        self.setGeometry(200,200,340,200)           # window position and size

    def onClicked(self):                    # onClicked function
        check_box = self.sender()           # checkbox tick event object
        print('Animal '+ (check_box.animal) +' is ' + str(check_box.isChecked()))   # print statement with checkbox variable and checking checkbox(True/False)

app = QApplication(sys.argv)                # initializing PyQt
CheckBox_obj = CheckBox()                   # class object
CheckBox_obj.show()                         # calling show () function with class object
sys.exit(app.exec_())                       # exit window