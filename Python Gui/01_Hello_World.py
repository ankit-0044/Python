# PyQt Hello_world !

# Example : how to create simple gui window

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel   # importing QtWidgets for QApplication, QWidget etc
from PyQt5.QtGui import QIcon                       # importing QtGui for QIcon
from PyQt5.QtCore import pyqtSlot

def window ():
    app = QApplication (sys.argv)               # initializing PyQt
    widget = QWidget ()

    textLabel = QLabel(widget)                  # QLable for adding text or images
    textLabel.setText('Hello World!')           # setting text
    textLabel.move(110,85)                      # postion of the text

    widget.setGeometry(100,100,320,200)         # setting the starting postion(100,100) and the window size(320,200) using setGeometry()
    widget.setWindowTitle('Python PyQt5')       # setting window title using setWindowTitle()
    widget.show()                               # showing the window
    sys.exit(app.exec_())                       # exiting the creating window

if __name__=='__main__':
    window()
    