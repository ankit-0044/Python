# PyQt slider

# Example : QSlider ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Slider(QWidget):          # child class

    def __init__(self,parent=None):     # child class constructor
        super(Slider,self).__init__(parent)     # parent class constructor calling

        layout = QVBoxLayout()          # initializing QVBoxLayout (vertical box)
        self.label = QLabel("SLIDER")   # initializing QLabel with name 'SLIDER'
        self.label.setAlignment(Qt.AlignCenter) # setting label text to center
        layout.addWidget(self.label)            # setting label widget on layout widget

        self.slider = QSlider(Qt.Horizontal)        # initializing QSlide with horizontal position
        self.slider.setMinimum(10)          # minimum value on slider
        self.slider.setMaximum(30)          # maximum value on slider
        self.slider.setValue(20)            # default value where slider defaultly positioned
        self.slider.setTickPosition(QSlider.TicksBelow)     # slider tick position
        self.slider.setTickInterval(5)          # number of ticks on the slider

        layout.addWidget(self.slider)           # adding slider to a layout
        self.slider.valueChanged.connect(self.valuechange)  # connecting slider changevalue to a specified function
        self.setLayout(layout)              # setting layout to a main window
        self.setWindowTitle("PyQt Slider")  # main window title
        self.setGeometry(200,200,340,200)   # main window position and size

    def valuechange(self):                  # vlauechange function takes changing value of slider as a argument
        size = self.slider.value()          # taking slider value then assigne it to a variable name size
        self.label.setFont(QFont("Arial",size))     # changing the font size of text 'SLIDER' according to slider value

def main():         # main function
    app = QApplication(sys.argv)        # initializing PyQt
    Slider_Obj = Slider()               # class object
    Slider_Obj.show()                   # calling show () function using class object
    sys.exit(app.exec_())               # exit 

if __name__=='__main__':
    main()                              # calling main() function