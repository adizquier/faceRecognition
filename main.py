from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDialog
from inscripcionForm import Ui_Dialog
from identificationForm import Ui_Dialog as ui
from salida import Ui_Form
import numpy as np
import cv2
from mainwindow import Ui_MainWindow
import faceDetection as fd
from faceRecognition import faceRecognition

class messageOut (QWidget, Ui_Form):
    def __init__(self):
        super(messageOut, self).__init__()
        self.setupUi(self)

        self.putImage()

    def putImage(self):
        x = QtGui.QPixmap("./xBad_icon.png").scaled(70,70)

        self.texto.setWordWrap(True)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        self.imagen.setPixmap(x)
        self.texto.setText("Usuario no identificado")

class identificationForm(QDialog, ui):
    def __init__(self):
        super(identificationForm, self).__init__()  # Cambiado a identificationForm
        self.setupUi(self)

        self.faltanDatos.setVisible(False)
        self.identificar_buttom.clicked.connect(self.getInformation)

    def getInformation(self):
        usuario = self.usuario.text()

        if not usuario:
            self.faltanDatos.setVisible(True)
        else:
            self.hide()
            return (True, usuario)



class inscripcionForm(QDialog, Ui_Dialog):
    def __init__(self):
        super(inscripcionForm, self).__init__()
        self.setupUi(self)

        self.faltanDatos.setVisible(False)

        self.ingresarButtom.clicked.connect(self.getInformation)


    def getInformation(self):
        '''
        Metodo encargado de recoger los datos del dialogo de inscripcion para poder añadir a un usuario.
        En caso de haber algún campo nulo no se envian los datos, mostrando un mensaje para que el usuario
        sepa que faltan datos y los pueda añadir.
        '''
        nombre = self.nombre.text()
        apellidos = self.apellidos.text()
        dni = self.dni.text()
        usuario = self.usuario.text()
        correo = self.correo.text()

        if not nombre or not apellidos or not dni or not usuario or not correo:
            self.faltanDatos.setVisible(True)
        
        else: 
            self.hide()

            return (nombre, apellidos, dni, usuario, correo)

            



class Worker(QtCore.QThread):
    """
    Worker Thread para procesar frames mientras se sigue capturando video.
    """
    frame_processed = QtCore.Signal(np.ndarray)  # Señal para enviar el frame procesado de vuelta al MainWindow

    def __init__(self):
        super().__init__()
        self._running = True
        self.frame = None
        self.process = False

        self.processFrontal = False
        self.processRightProfile = False
        self.processLeftProfile = False

    def run(self):
        """
        Método principal del hilo para procesar los frames.
        """
        while self._running:
            if self.frame is not None and self.process:
                # Aquí puedes aplicar tu procesamiento en cada frame
                

                # Emite la señal con el frame procesado
                self.frame_processed.emit(self.frame)


    def startProcess(self):
        self.process = True

    def endProcess(self):
        self.process = False
    

    def update_frame(self, frame):
        """
        Método para actualizar el frame que se debe procesar.
        """
        self.frame = frame

    def stop(self):
        """
        Detener el hilo de procesamiento.
        """
        self._running = False


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.inscripcionForm = inscripcionForm()
        self.identificationForma = identificationForm()
        self.messageOut = messageOut()

        self.cap = cv2.VideoCapture(0)
        self.colorImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
        self.grayImage = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height()), dtype = np.uint8)

        self.imageVisor = np.zeros((self.imageFrame.size().width(), self.imageFrame.size().height(),3), dtype = np.uint8)
                
        self.worker = Worker()
        self.worker.start()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.compute)
        self.timer.start(30)

        self.addUser_buttom.clicked.connect(self.addNewUser)
        self.addFace_buttom.clicked.connect(self.addFaceFeatures)

        self.active_desactive_buttoms(False, (self.addFrontal_Buttom, self.addRight_buttom, self.addLeft_buttom))

        self.recg = faceRecognition()

        
    def active_desactive_buttoms(self, flag, buttoms):
        for bt in buttoms:
            bt.setEnabled(flag)
            bt.setVisible(flag)

    def addNewUser(self):

        self.inscripcionForm.show()

        self.inscripcionForm.exec_()

        user_info = self.inscripcionForm.getInformation()

        if user_info:
            name, surname, dni, username, gmail = user_info
            print(name)
            self.recg.addUser(name, surname, dni, username, gmail)


    def addFaceFeatures(self):
        self.identificationForma.show()
        self.identificationForma.exec_()

        introducido, usuario = self.identificationForma.getInformation()

        if introducido:

            idnt = self.recg.lookForPlayer(usuario)

            if idnt:

                self.active_desactive_buttoms(True, (self.addFrontal_Buttom, self.addRight_buttom, self.addLeft_buttom))

            else:
                self.messageOut.show()
            



            #self.worker.startProcess()

            #if self.addFrontal_Buttom.isChecked():
            


        
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
