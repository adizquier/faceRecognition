from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
from mainwindow import Ui_MainWindow
import face_recognition as frec


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cap = cv2.VideoCapture(2)
        self.colorImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
        self.grayImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height()), dtype = np.uint8)

        self.imageVisor = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
                
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.compute)
        self.timer.start(30)

        self.facesEncodings = []
        self.facesNames = []

    def compute(self):

        ret, capImage = self.cap.read()
 
        if ret:
            self.colorImage = cv2.resize(capImage, (self.imageFrame.size().width(), self.imageFrame.size().height()))
            self.imageVisor = cv2.resize(self.imageVisor, (self.imageFrame.size().width(), self.imageFrame.size().height()))

            self.colorImage = cv2.cvtColor(self.colorImage, cv2.COLOR_BGR2RGB)
            np.copyto(self.imageVisor, self.colorImage)
            self.grayImage = cv2.cvtColor(self.colorImage, cv2.COLOR_BGR2GRAY)

        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        
        qp.begin(self)
        if self.colorImage is not None:
            w = (self.imageFrame.size().width()//4)*4
            h = self.imageFrame.size().height()
            cvImage = cv2.resize(self.colorImage, (w,h))
            qImg = QtGui.QImage(cvImage,w, h,QtGui.QImage.Format_RGB888)

            qp.drawImage(self.imageFrame.pos().x(), self.imageFrame.pos().y(), qImg)
        qp.end()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
