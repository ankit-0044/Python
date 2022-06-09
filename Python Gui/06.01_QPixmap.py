# PyQt Pixmap

# Example : using QPixmap()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def window ():                              # window function
    app = QApplication(sys.argv)            # initializing PyQt
    widget = QWidget()                      # initializing QWidget
    label = QLabel()                        # initializing QLabel
    
    img = QPixmap('Python Gui\python.jpg')  # initializing QPixmap and giving image as a argument
    label.setPixmap(img)                    # setting image on label
    
    vbox = QVBoxLayout()                    # initializing QVBoxLayout (vertical box)
    vbox.addWidget(label)                   # adding label on the vbox
    widget.setLayout(vbox)                  # adding vbox on the widget
    widget.setGeometry(200,200,340,200)     # window position and size
    widget.setWindowTitle('PyQt Pixmap')    # window title
    widget.show()                           # showing window
    sys.exit(app.exec_())                   # exit

if __name__ == '__main__':
    window()                                # function call