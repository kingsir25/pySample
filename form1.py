#coding=utf-8

import sys
from PyQt5 import QtGui, QtCore

class Trans(QtGui.QWidget):

    def __init__(self):
        super(Trans, self).__init__()
        self.initUI()
        button = QtGui.QPushButton('Close', self)
        self.connect(button, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                     QtCore.SLOT('quit()'))

    def initUI(self):
        #self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    trans = Trans()
    trans.show()
    sys.exit(app.exec_())