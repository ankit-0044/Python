# PyQt toolbox

# Example : QToolBox()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):          # child class
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt ToolBox")     # main window title
        self.setGeometry(300,300,300,300)       # main window geometry
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # main window icon
        
        self.createLayout()                 # calling method
        self.show()                         # showing all windows

    def createLayout(self):                 # creating method 
        self.layout = QGridLayout()         # initializing QGridLayout()
        self.setLayout(self.layout)         # settin grid layout on main window

        self.toolbox = QToolBox()           # initializing QToolBox
        self.layout.addWidget(self.toolbox) # setting toolbox on grid layout

        label = QLabel()
        self.toolbox.addItem(label, QIcon("Python Gui\student.png"),"Student")
        self.toolbox.setFont(QFont("Aerial",15))
        
        label = QLabel()
        self.toolbox.addItem(label,QIcon("Python Gui\Teacher.png"),"Teacher")

        lable = QLabel()
        self.toolbox.addItem(label,QIcon("Python Gui\Director.png"),"Directors")

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    sys.exit(app.exec_())