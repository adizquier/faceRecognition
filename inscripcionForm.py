# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inscripcionForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 328)
        self.nombre = QLineEdit(Dialog)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(250, 40, 250, 25))
        self.apellidos = QLineEdit(Dialog)
        self.apellidos.setObjectName(u"apellidos")
        self.apellidos.setGeometry(QRect(250, 80, 250, 25))
        self.dni = QLineEdit(Dialog)
        self.dni.setObjectName(u"dni")
        self.dni.setGeometry(QRect(250, 120, 250, 25))
        self.correo = QLineEdit(Dialog)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(250, 200, 250, 25))
        self.usuario = QLineEdit(Dialog)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(250, 160, 250, 25))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 67, 17))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 67, 17))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 67, 17))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 160, 141, 17))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 200, 141, 17))
        self.label_5.setFont(font)
        self.ingresarButtom = QPushButton(Dialog)
        self.ingresarButtom.setObjectName(u"ingresarButtom")
        self.ingresarButtom.setGeometry(QRect(250, 260, 100, 40))
        self.ingresarButtom.setFont(font)
        self.faltanDatos = QLabel(Dialog)
        self.faltanDatos.setObjectName(u"faltanDatos")
        self.faltanDatos.setEnabled(True)
        self.faltanDatos.setGeometry(QRect(390, 270, 111, 17))
        self.faltanDatos.setFont(font)
        self.faltanDatos.setStyleSheet(u"color: red;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Apellidos", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"DNI", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nombre de usuario", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Correo electr\u00f3nico", None))
        self.ingresarButtom.setText(QCoreApplication.translate("Dialog", u"Ingresar", None))
        self.faltanDatos.setText(QCoreApplication.translate("Dialog", u"FALTAN DATOS", None))
    # retranslateUi

