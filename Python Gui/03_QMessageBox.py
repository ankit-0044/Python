# PyQt messagebox

# Example : How to create QMessageBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)        # initializing PyQt
    widget = QWidget()                  # initializing widget window

    TextLable = QLabel(widget)          # initializing QLable for text on the window
    TextLable.setText('Message Pop Button') 
    TextLable.move(110,50)

    button = QPushButton(widget)        # initializing push button on window
    button.setText('Show dialog!')
    button.move(120,80)
    button.clicked.connect(ShowDialog)  # adding mouse click event then connecting it to specified function

    widget.setGeometry(200,200,340,200) # setting up window position and size 
    widget.setWindowTitle('PyQt Message Box')
    widget.show()                       # showing window
    sys.exit(app.exec_())

def ShowDialog():                       # ShowDialog function
    msgBox = QMessageBox()              # initializing messagebox using QMessageBox()
    msgBox.setIcon(QMessageBox.Information) # setting messagebox icon(Information)
    msgBox.setText('Message Box Pop Up Window') # messagebox text
    msgBox.setInformativeText('This is additional information') # additional information under messagebox text
    msgBox.setWindowTitle('QMessageBox')        # messagebox window title
    msgBox.setDetailedText('The details are as follow...')  # detailed information under additional information
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) # standard buttons for messagebox(Ok | Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)            # adding mouse click event then connect it to specified function

    returnValue = msgBox.exec()         # storing msgbox returning value
    if returnValue == QMessageBox.Ok:   # comparing
        print('Ok Clicked')             # print statement
    print('Value of the pressed message box button:',returnValue)       # shows the numerical value of clicked button on messagebox


def msgButtonClick(i):                 # msgButtonClick function, takes argument return value coming from msgBox
    print('Button clicked is:',i.text())    # print statement, 'i.text()' will change the object value of 'i' in text fromate

if __name__ == '__main__':
    window()                        # function call