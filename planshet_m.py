import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QRadioButton, QApplication, QFileDialog)
from PyQt5.QtCore import *
"""
Program for desktop programming fields testing. It copies to the clipboard the value selected from the list for later pasting. 
For correct working need you need to create a test suite file where the values listed, 
one string-one value/.txt format/  
Need install PyQt5
Every start you will choose a test suite file location
"""
masnames = []
class Interface(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose test suit file', '/home')[0]
        f = open(fname, 'r')
        with f:
            names = (f.readlines())
            names = [line.rstrip() for line in names]
        f.close()
        return (names)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = self.showDialog()
        global masnames
        for i in range(len(names)):
            masnames.append(names[i])
        if len(names) > 20:
            cols = 2
            rows = len(names) // 2
        else:
            cols = 1
            rows = len(names)
        cnt = 0
        positions = [(i, j) for i in range(rows) for j in range(cols)]
        for position in positions:
            if names == '':
                continue
            button = QRadioButton(names[cnt][0:25])
            grid.addWidget(button, *position)
            cnt = cnt + 1
            button.toggled.connect(lambda: self.btnstate())
        self.move(300, 250)
        self.setWindowTitle('планшет')
        self.show()

    def btnstate(self):
         global masnames
         clipboard = QApplication.clipboard()
         button = self.sender().text()
         for i in range(len(masnames)):
             if masnames[i][0:25] == button:
                 clipboard.setText(masnames[i])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
