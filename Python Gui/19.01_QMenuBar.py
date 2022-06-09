# PyQt menubar

# Example : QMenuBar ()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()      # initializing QHBoxlayout()
        bar = self.menuBar()        # initializing menuBar()
        file = bar.addMenu("File")  # adding file menu
        file.addAction("New")       # adding 'New' action inside file menu

        save = QAction("Save",self) # adding 'Save' action inside file menu
        save.setShortcut("Ctrl+S")  # shortcut for save action
        file.addAction(save)        # adding save in the file menu

        edit = file.addMenu("Edit") # adding 'Edit' action inside file menu
        edit.addAction("Copy")      # adding 'copy' action inside 'Edit"
        edit.addAction("Paste")     # adding 'Paste' action inse=ide "Edit"

        quit = QAction("Quit",self) # adding 'Quit' action
        file.addAction(quit)        # adding quit inside file menu
        file.triggered[QAction].connect(self.processtrigger)    # connecting trigger signal to a method
        
        self.setWindowTitle("PyQt MenuBar")     # main window title
        self.setWindowIcon(QIcon("Python Gui\home.png"))    # main window icon

    def processtrigger(self,q):                 # trigger method
        print(q.text()+" is triggered")         # print statement

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()