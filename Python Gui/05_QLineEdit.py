# PyQt line edit

# Example : Using QLineEdit

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class Lineedit(QMainWindow):        # creating child class Lineedit from parent class QMainWindow
    def __init__(self):             # child class constructor
        super().__init__()          # super() method is used to call the parent class constructor

        self.qlable1 = QLabel(self) # initializing Qlabel
        self.qlable1.setText('Input Anything')  # Label text
        self.qlable1.move(20,20)    # label position 

        self.lineEntry = QLineEdit(self)    # initializing QLineEdit for user input text
        self.lineEntry.move(20,50)          # LineEdit position
        self.lineEntry.resize(300,50)       # size of the LineEdit

        self.qlabel = QLabel(self)          # initiallizing another Qlabel 
        self.qlabel.move(20,100)            # label position

        self.lineEntry.textChanged.connect(self.onChanged)  # connecting lineedit to qlabel for current changes

        self.setGeometry(200,200,340,200)       # window position and size
        self.setWindowTitle('PyQt QLineEdit')   # window title
        #self.show()

        self.button = QPushButton('OK',self)    # initializing push button with name OK
        self.button.move(100,130)               # position of push button
        self.button.resize(150,50)              # size of push button
        self.button.clicked.connect(self.clickMethod)   # connecting push button to specified function

    def onChanged(self,text):                   # function onChanged receive input coming from lineEntry as a argument
        self.qlabel.setText(text)               # setting text coming from lineEntry to qlabel
        self.qlabel.adjustSize()                # to adjust the size(length) of text
    
    def clickMethod(self):                      # clickMethod function
        print('Your Entered:',self.lineEntry.text())    # print the entered text input by user

if __name__ == '__main__':
    app = QApplication(sys.argv)                # initializing PyQt
    Lineedit_obj = Lineedit()                   # object of a class
    Lineedit_obj.show()                         # calling show () function using class object
    sys.exit(app.exec_())                       # exiting from the window