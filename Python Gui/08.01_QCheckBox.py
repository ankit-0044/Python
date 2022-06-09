# PyQt checkbox

# Example : QCheckBox ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Checkbox(QWidget):
    def __init__(self,parent=None):
        super(Checkbox,self).__init__(parent)

        layout = QHBoxLayout()          # horizontal box
        self.b1 = QCheckBox('CheckBox 1')   # checkbox 1
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))    # statechanged signal connected to specified function
        layout.addWidget(self.b1)

        self.b2 = QCheckBox('CheckBox 2')       # checkbox 2
        self.b2.stateChanged.connect(lambda:self.btnstate(self.b2))    # stateChanged signal connected to specified function 
        layout.addWidget(self.b2)

        self.setLayout(layout)      # setting horizontal box on main layout
        self.setGeometry(200,200,340,200)   # windows position and size
        self.setWindowTitle('PyQt CheckBox')    # windows title

    def btnstate(self,b):       # btnstate function takes stateChanged signal as a argument
        if b.text() == "CheckBox 1":    # condition
            if b.isChecked() == True:   # condition
                print(f'{b.text() } is slected')
            else:
                print(f'{b.text() } is deselected')
        
        if b.text() == "CheckBox 2":
            if b.isChecked() == True:
                print(f'{b.text() } is selected')
            else:
                print(f'{b.text() } is deselected')

def main():     # main function
    app =QApplication(sys.argv)     # initializing PyQt
    Checkbox_obj = Checkbox()       # class object
    Checkbox_obj.show()             # calling show ()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()                          # calling main