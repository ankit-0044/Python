# PyQt Pixmap

# Example : QPixmap ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Pixmap (QWidget):         # Pixmap child class inherited from QWidget
    def __init__(self):         # child class constructor
        super().__init__()      # calling parent class constructor

        self.initUI()           # function calling inside constructor

    def initUI (self):          # function
        hbox = QHBoxLayout(self)    # initializing QHBoxLayout (horizontal box)
        img = QPixmap('Python Gui\python.jpg')  # initializing QPixmap ans giving images as a argument

        label = QLabel(self)                # initializing Qlabel
        label.setPixmap(img)                # setting image on the label

        hbox.addWidget(label)               # setting label on the hbox
        self.setLayout(hbox)                # setting hbox on the constructor

        self.move(200,200)                  # window position
        self.setWindowTitle("PyQt Pixmap")  # window size
        self.show()                         # showing window

def main():                                 # function main
    app = QApplication(sys.argv)            # initializing PyQt
    Pixmap_obj = Pixmap()                   # class object
    #Pixmap_obj.initUI()
    sys.exit(app.exec_())                   # exit

if __name__ == '__main__':
    main()                                  # function call