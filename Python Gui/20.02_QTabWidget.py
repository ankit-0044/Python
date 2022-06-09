# PyQt tabwidget

# Example : addtab()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Tabdemo(QTabWidget):      # child class inheriting from QTabWidget
    def __init__(self):
        super().__init__()

        self.tab1 = QWidget()       # initializing Qwidget() for tab1
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1,"Tab 1")      # Adding tab widget to main window
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")

        self.tab1UI()                       # calling Tab method
        self.tab2UI()
        self.tab3UI()

        # main Window
        self.setWindowTitle("PyQt TabWidget")
        self.setWindowIcon(QIcon("Python Gui\home.png"))
        self.setGeometry(300,300,400,150)

    def tab1UI(self):                   # tab method 1
        layout = QFormLayout()          # initializing QFormLayout()
        layout.addRow("Name",QLineEdit())   # adding row in formlayout
        layout.addRow("Address",QLineEdit())
        self.setTabText(0,"Contact Details")    # setting tab name
        self.tab1.setLayout(layout)             # setting layout to tab1

    def tab2UI(self):
        layout = QFormLayout()          # initializing QFormLayout()
        sex = QHBoxLayout()             # initializing QHBoxLayout()
        sex.addWidget(QRadioButton("Male")) # adding radiobutton widget to Hbox
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"),sex)        # adding in form layout
        layout.addRow("Date of Birth",QLineEdit())
        self.setTabText(1,"Personal Details")       # tab name
        self.tab2.setLayout(layout)         # setting layout to tab2

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Subject"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.setTabText(2,"Education Details")
        self.tab3.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Tabdemo()
    ex.show()
    sys.exit(app.exec_())