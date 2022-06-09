# PyQt slider

# Example : QSlider ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Slider(QWidget):      # child class

    def __init__(self):     # child class constructor
        super().__init__()      # calling parent class constructor

        self.window()           # function call inside constructor
    
    def window(self):           # function

        self.layout = QVBoxLayout()     # initializing QVBoxLayout (vertical box)
        self.label1 = QLabel("Mute")        # initializing label
        self.label1.setAlignment(Qt.AlignCenter)    # label position in center
        self.label1.setFont(QFont('Arial',20))      # label font
        self.layout.addWidget(self.label1)          # adding label to layout

        self.slider = QSlider(Qt.Horizontal,self)   # initializing slider with horizontal position
        self.slider.setFocusPolicy(Qt.NoFocus)      # setFocusPolicy() holds the way the widget accepts keyboard focus
        self.slider.valueChanged[int].connect(self.changevalue) # connecting value change in slider to a function called changevalue
        self.layout.addWidget(self.slider)          # adding slider on a layout

        self.label = QLabel(self)                   # initializing another QLabel
        self.label.setPixmap(QPixmap('Python Gui\Mute.png'))    # setting image on a label 
        self.label.setAlignment(Qt.AlignCenter)                 # label position
        self.layout.addWidget(self.label)                       # adding label on a layout
        

        self.setLayout(self.layout)                 # setting layout on a main window
        self.setGeometry(300,300,600,400)           # main window position and size
        self.setWindowTitle('PyQt Slider')          # main window name
        self.show()                                 # showing main window

    def changevalue(self,value):            # function takes valuechange from slider as a argument

        if value == 0:      # condition
            self.label.setPixmap(QPixmap("Python Gui\Mute.png")) # setting image on a label
            self.label1.setText("Mute")     # changing label1 text
        
        elif 0 < value <= 30:   # condition
            self.label.setPixmap(QPixmap("Python Gui\Min.png")) # changing image of a label
            self.label1.setText("Min")      # changing lable1 text
        
        elif 30 < value <= 80:  # Condition
            self.label.setPixmap(QPixmap("Python Gui\Mid.png"))  # changing image of a lable
            self.label1.setText('Mid')      # changing text of a label1

        else:   # condition
            self.label.setPixmap(QPixmap("Python Gui\Max.png"))
            self.label1.setText("Max")

def main():         # main function
    app = QApplication(sys.argv)            # initializing PyQt
    Slider_obj = Slider()                   # class object
    sys.exit(app.exec_())                   # exit window

if __name__=="__main__":
    main()                                  # calling main function