# PyQt combobox

# Example : QComboBox

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ComboBox(QWidget):            # ComboBox child class inheriting from QWidget
    def __init__(self,parent = None):     # child class constructor
        super(ComboBox,self).__init__(parent)   # calling parent class constructor

        self.Hbox = QHBoxLayout()           # initializing QHBoxLayout (horizontal box)
        self.cb = QComboBox()               # initializing QComboBox
        self.cb.addItem('c')                # adding item in combobox
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItem('Java')
        self.cb.currentIndexChanged.connect(self.selectionchange)   # index value of  choosed item

        self.Hbox.addWidget(self.cb)        # adding combobox to Hbox
        self.setLayout(self.Hbox)           # setting Hbox on a window
        self.setWindowTitle('PyQt ComboBox')    # window title
        self.setGeometry(200,200,340,200)       # window position and size

    def selectionchange(self,i):            # function taking index value coming from 'currentIndexChanged' as a argument
        print('Item in the list are:')      # simple print statement

        for count in range(self.cb.count()):    # loop for counting the combobox items
            print(self.cb.itemText(count))      # printing box item
        
        print('Current index',i,'selection changed',self.cb.currentText()) # print statement with index value and selected item from the box

def main():         # function main
    app = QApplication(sys.argv)        # initializing PyQt
    ComboBox_obj = ComboBox()           # class object
    ComboBox_obj.show()                 # calling show () function using class object
    sys.exit(app.exec_())               # exit window

if __name__ == "__main__":
    main()                              # main function call