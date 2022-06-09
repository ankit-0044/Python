# PyQt toolbar

# Example : QToolBar()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.InitUI()

    def InitUI(self):

        # tool exit action which terminate the application when triggered
        exitAct = QAction(QIcon("Python Gui\exit24.png"),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        # action object quit() method of the QMainWindow is connected to the triggered signal
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        # main window
        self.setWindowTitle("PyQt ToolBar")
        self.setGeometry(300,300,300,300)
        self.setWindowIcon(QIcon("Python Gui\home.png"))

        self.show()

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    app.exec()

if __name__=="__main__":
    main()