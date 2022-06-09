# PyQt Pixmap

# Example : showing image using QPixmap()

import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QGridLayout, QWidget
from PyQt5.QtGui import QPixmap

class Pixmap(QWidget):          # Pixmap Child class inherited from QWidget
    def __init__(self):         # child class constructor
        super().__init__()      # calling parent class constructor using super()

        self.img = QPixmap("Python Gui\download.jpg")   # initializing QPixmap and giving image as a argument
        self.label = QLabel()               # initializing label
        self.label.setPixmap(self.img)      # setting image on label

        self.grid = QGridLayout()           # initializing QGridLayout
        self.grid.addWidget(self.label,1,1) # adding label on grid
        self.setLayout(self.grid)           # setting grid layout to the constructor

        self.setGeometry(200,200,340,200)   # window position and size 
        self.setWindowTitle('PyQt Pixmap')  # window title
        #self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)            # initializing PyQt
    Pixmap_obj = Pixmap()                   # class object
    Pixmap_obj.show()                       # calling show() using class object
    sys.exit(app.exec_())                   # exit window
