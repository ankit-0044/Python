# PyQt slider

# Example : QSlider ()

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Slider(QMainWindow):      # Slider child class inheriting from QMainWindow

    def __init__(self):         # chlid class constructor
        super().__init__()      # calling parent class constructor

        myslider = QSlider(Qt.Horizontal,self)      # initializing QSlider in Horizontal position (Qt.Vertical for vertical position)
        myslider.setGeometry(30,40,200,30)          # slider position and size
        myslider.valueChanged[int].connect(self.changevalue)    # slider valuechanged connected to a specified function

        self.setGeometry(200,200,340,200)           # main window position and size
        self.setWindowTitle('PyQt Slider')          # main window title
        self.show()                                 # showing main window

    def changevalue(self,value):                    # changevalue function takes int value coming from valuechanged[int] as a argument
        print(value)                                # printing value

if __name__=='__main__':                        
    app = QApplication(sys.argv)            # initializing PyQt
    Slider_obj = Slider()                   # class object
    sys.exit(app.exec_())                   # exit
