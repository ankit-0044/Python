# PyQt Vboxlayout

# Example : QVBoxLayout()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])              # initializing PyQt
window = QWidget()                  # initializing QWidget
layout = QVBoxLayout()              # initializing QVBoxLayout (vertical box)

layout.addWidget(QPushButton('1'))  # adding and initializing pushbutton
layout.addWidget(QPushButton('2'))
layout.addWidget(QPushButton('3'))

window.setLayout(layout)            # setting VBoxLayout on a widget(main widget)
window.setGeometry(300,300,340,200) # main window position and size
window.setWindowTitle("PYQt VBoxLayout")    # window title
window.setWindowIcon(QIcon("Python Gui\home.png"))  # window icon
window.show()                       # showing all window
app.exec_()                         # starting loop