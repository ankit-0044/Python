# PyQt checkbox

# Example : QCheckBox () adding in QButtonGroup ()

# PyQt checkbox

# Example : QCheckBox ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Checkbox(QWidget):
    def __init__(self,parent=None):
        super(Checkbox,self).__init__(parent)

        layout = QHBoxLayout()
        self.b1 = QCheckBox('CheckBox 1')
        self.b1.setChecked(True)
        #self.b1.stateChanged.connect(self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox('CheckBox 2')
        #self.b2.stateChanged.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)

        self.bg = QButtonGroup()
        self.bg.addButton(self.b1,1)
        self.bg.addButton(self.b2,2)
        self.bg.buttonClicked[QAbstractButton].connect(self.btngroup)

        self.setLayout(layout)
        self.setGeometry(200,200,340,200)
        self.setWindowTitle('PyQt CheckBox')

    def btngroup(self,btn):
        print(btn.text()+' is selected')
        

def main():
    app =QApplication(sys.argv)
    Checkbox_obj = Checkbox()
    Checkbox_obj.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()