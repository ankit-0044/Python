# PyQt combobox

# Example : using QComboBox

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ComboBox(QMainWindow):        # ComboBox child class inheriting from QMainWindow parent class

    def __init__(self):             # child class constructor
        super().__init__()          # calling parent class constructor

        self.lst = ['Mango','Banana','Grapes','Orange']     # list

        combo = QComboBox(self)     # initializing QComboBox
        combo.addItem('Apple')      # adding item
        combo.addItem('Pear')
        combo.addItem('Lemon')
        combo.addItems(self.lst)    # adding items passing iterable object(list)

        combo.move(50,50)           # position of combobox

        self.label1 = QLabel(self)  # initializing label
        self.label1.move(50,15)     # position
        self.label1.setText('Select your Choice')   # label text
        self.label1.adjustSize()    # adjust label size according to text

        self.label2 = QLabel(self)  # initializing another label
        self.label2.move(52,85)     # position

        combo.activated[str].connect(self.onChanged)    # activating combobox and connecting it to specified function

        self.setGeometry(200,200,340,200)       # window position and size
        self.setWindowTitle('PyQt ComboBox')    # window title
        self.show()                             # showing window

    def onChanged(self,text):                   # onChanged function takes selected item as a argument from combobox
        self.label2.setText(text)               # selected item setting up on a label
        self.label2.adjustSize()                # adjust size according to text

if __name__ == '__main__':
    app = QApplication(sys.argv)                # initializing PyQt
    comboBox_obj = ComboBox()                   # class object
    sys.exit(app.exec_())                       # exiting window