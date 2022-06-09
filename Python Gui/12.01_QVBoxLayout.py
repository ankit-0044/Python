# PyQt VBoxLayout

# Example : QVBoxLayout()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def window():                   # window function
    app = QApplication(sys.argv)    # initializing PyQt
    widget = QWidget()              # initializing QWidget for window

    b1 = QPushButton("Button1")     # initializing pushbutton
    b2 = QPushButton("Button2")

    vbox = QVBoxLayout()            # initializing QVBoxLayout (vertical box)
    vbox.addWidget(b1)              # adding pushbutton to vbox
    vbox.addStretch()               # addStretch for stretch(spacing)
    vbox.addWidget(b2)              
    widget.setLayout(vbox)          # adding vboxlayout to widget (main window)

    widget.setWindowTitle('PyQt VBoxLayout')    # window title
    widget.setGeometry(300,300,340,200)         # window position and size
    widget.setWindowIcon(QIcon("Python Gui\home.png"))  # window icon
    widget.show()                               # showing all window
    sys.exit(app.exec_())                       # starting loop and exit window

if __name__ == '__main__':
    window()                        # function call