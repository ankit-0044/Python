# PyQt Vbox and HBox

# Example : VBoxLayout + HboxLayout

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def window ():                  # window function
    app = QApplication(sys.argv)    # initializing PyQt
    win = QWidget()                 # initializing QWidget(main window)

    b1 = QPushButton("Button1")     # initializing pushbutton
    b2 = QPushButton("Button2")
    b2.setStyleSheet("color : red; background-color: azure")    # button text color and button background color

    vbox = QVBoxLayout()            # initializing QVBoxlayout(vertical box)
    vbox.addWidget(b1)              # adding pushbutton to vbox
    vbox.addStretch()               # stretch for spacing
    vbox.addWidget(b2)              

    
    b3 = QPushButton('Button3')     
    b4 = QPushButton("Button4")
    
    hbox = QHBoxLayout()            # initializing QHBoclayout(horizontal box)
    hbox.addWidget(b3)
    hbox.addStretch()
    hbox.addWidget(b4)

    vbox.addStretch()
    vbox.addLayout(hbox)

    win.setLayout(vbox)
    win.setGeometry(300,300,340,200)
    win.setWindowTitle("PyQt Vbox HBox")
    win.setWindowIcon(QIcon("Python Gui\home.png"))
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()