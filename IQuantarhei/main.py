# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

def window():
    
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    
    b.setText("Welcome to Quantarhei!")
    w.setGeometry(100,100,200,50)
    b.move(40,20)
    w.setWindowTitle("PyQt")
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window()
    
    
