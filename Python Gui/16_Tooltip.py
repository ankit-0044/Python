# PyQt tooltip

# Example : .setToolTip()

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Window(QWidget):              # child class
    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.setGeometry(300,300,400,200)       # main window geometry
        self.setWindowTitle("PyQt ToolTip")     # title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # icon

        self.createLayout()         # calling methods

        self.show()                 # showing all windows

    def createLayout(self):         # creating method
        self.layout = QGridLayout() # initializing QGridLayout()
        self.setLayout(self.layout) # setting grid layout on main window

        self.button = QPushButton("Save")   # initializing QPushButton() with name "Save"
        self.button.setToolTip("Save The File") # setting tooltip on a button
        self.layout.addWidget(self.button,0,0)  # adding button on grid layout

        self.button1 = QPushButton("Cancel")    
        self.button1.setToolTip("<b>Exit</b> <i>from</i> from the app..")
        self.layout.addWidget(self.button1,0,1)


if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    app.exec()