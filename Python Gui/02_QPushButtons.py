# PyQt pushbutton

# Example : How to create a QPushButtons

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)            # initializing a PyQt
    widget = QWidget()                      # initializing a widget

    TextLable = QLabel(widget)              # QLable for adding text
    TextLable.setText("Push Buttons")       # adding text
    TextLable.move(115,15)                  # position of the text on the widget window

    button1 = QPushButton(widget)           # initializing a 1st push button
    button1.setText("Button 1")             # adding a text on button
    button1.move(115,32)                    # position of the button on the window
    button1.clicked.connect(button1_clicked)    # adding a mouse click event then connect it to specified function

    button2 = QPushButton(widget)           # initializing a 2nd push button
    button2.setText("Button 2")
    button2.move(115,64)
    button2.clicked.connect(button2_clicked) # click event 

    widget.setGeometry(200,200,340,120)     # setting the window position and size
    widget.setWindowTitle("PyQt5 Push Button")  # setting the window title
    widget.show()                               # showing the window

    sys.exit(app.exec_())                       # exiting the window

def button1_clicked():                          # function 1
    print('Button 1 clicked')
    
def button2_clicked():                          # function 2
    print('Button 2 clicked')

if __name__ == '__main__':
    window()                                    # calling window () function