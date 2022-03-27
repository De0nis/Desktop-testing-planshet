import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QRadioButton, QApplication, QFileDialog)
from PyQt5.QtCore import *
"""
Program for desktop testing. it copies to the clipboard the value selected from the list for later pasting. 
For correct working need you need to create a test suite file where the values listed, 
one string-one value/.txt format/
Example:
12345678
Alextest
test.test@test.ru
test@test
@#$#%$^%^*”
”SELECT * from users”
Every start you will choose a test suite file
"""
masnames = []
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
#choose test suit file
    def showDialog(self):                                       
        fname = QFileDialog.getOpenFileName(self, 'Choose test suit file', '/home')[0]
        f = open(fname, 'r')
        with f:
            names = (f.readlines())
        f.close()
        return (names)
#UI main
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = self.showDialog()
        global masnames
        for i in range(len(names)):
            button = QRadioButton(names[i][0:25])
            masnames.append(names[i])
            grid.addWidget(button)
            button.toggled.connect(lambda: self.btnstate())
        self.move(300, 250)
        self.setWindowTitle('планшет')
        self.show()
#clipboard
    def btnstate(self):
         global masnames
         clipboard = QApplication.clipboard()
         button = self.sender().text()
         for i in range(len(masnames)):
             if masnames[i][0:25] == button:
                 clipboard.setText(masnames[i])
#launcher
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

