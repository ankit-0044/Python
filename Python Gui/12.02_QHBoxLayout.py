# PyQt QHBoxLayout

# Example : QHBoxlayout()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def window():
    app = QApplication(sys.argv)        # initializing PyQt
    win = QWidget()                     # initializing QWidget(main window)

    b1 = QPushButton("Button1")         # initializing pushbutton
    b2 = QPushButton("Button2")

    hbox = QHBoxLayout()                # initializing QHBoxLayout

    hbox.addWidget(b1)                  # adding pushbutton to hbox
    hbox.addStretch()
    hbox.addWidget(b2)

    win.setLayout(hbox)                 # setting hboxlayout to widget(main window)
    win.setGeometry(300,300,340,200)    # window position and size
    win.setWindowTitle("PyQt QHBoxLayout")  # window title
    win.setWindowIcon(QIcon("Python Gui\home.png")) # window icon
    win.show()                          # showing all window
    sys.exit(app.exec_())               # starting loop and exit window

if __name__ == '__main__':
    window()                            # function call