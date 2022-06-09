# PyQt grid

# Example : Creating a GridLayout

import sys
from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window(): 
    app = QApplication(sys.argv)
    widget = QWidget()
    
    grid = QGridLayout()            # initializing grid using QGridLayout()
    for i in range(0,10):            # outer for loop
        for j in range(0,10):        # inner for loop
            grid.addWidget(QPushButton(str(i)+str(j)),i,j)   # adding a pushbuttons on a grid layout, then values of i,j setting up on pushbuttons
    
    widget.setLayout(grid)      # setting grid layout on a widget window
    widget.setGeometry(200,200,340,200)     # window positon and size
    widget.setWindowTitle('PyQt Grid')      # window title
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()