# PyQt tablewidget

# Example : QTableWidget()

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

data = {'col1':['1','2','3','4'],       # dictionary of list
        'col2':['1','2','1','3'],
        'col3':['1','1','2','1']}

class TableView(QTableWidget):          # child class
    def __init__(self,data,*args):      # child class constructor with 'data', '*args' arguments
        QTableWidget.__init__(self, *args)  # calling parent class construnctor

        self.data = data                # assigning data to a variable self.data
        self.setData()                  # calling function
        self.resizeColumnsToContents()  # resizing columns
        self.resizeRowsToContents()     # resizing rows
        

        self.setGeometry(300,300,300,200)   # main window position and size
        self.setWindowTitle('PyQt TableWidget') # main window title
        self.setWindowIcon(QIcon('Python Gui\home.png'))    # main window icon

    def setData(self):                  # setData function
        horHeader = []                  # empty list
        for n, key in enumerate(sorted(self.data.keys())):  # enumerating 
            horHeader.append(key)       # appending key vlaues in empty list
            for m, item in enumerate(self.data[key]):   # enumerating
                newitem = QTableWidgetItem(item)    # inserting item into tablewidget
                self.setItem(m,n,newitem)           # setting item on table
        self.setHorizontalHeaderLabels(horHeader)   # header lable

def main(args):             # main function
    app = QApplication(args)    # initializing PyQt
    TableView_obj = TableView(data,4,3)     # class object
    TableView_obj.show()                    # calling function
    sys.exit(app.exec_())                   # starting loop and exiting window

if __name__=='__main__':
    main(sys.argv)