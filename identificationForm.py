# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'identificationForm.ui'
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
        Dialog.resize(450, 200)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 141, 17))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.usuario = QLineEdit(Dialog)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(200, 80, 211, 25))
        self.identificar_buttom = QPushButton(Dialog)
        self.identificar_buttom.setObjectName(u"identificar_buttom")
        self.identificar_buttom.setGeometry(QRect(180, 140, 91, 31))
        self.identificar_buttom.setFont(font)
        self.faltanDatos = QLabel(Dialog)
        self.faltanDatos.setObjectName(u"faltanDatos")
        self.faltanDatos.setGeometry(QRect(290, 150, 111, 17))
        self.faltanDatos.setFont(font)
        self.faltanDatos.setStyleSheet(u"color: red;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre de usuario", None))
        self.identificar_buttom.setText(QCoreApplication.translate("Dialog", u"Identificar", None))
        self.faltanDatos.setText(QCoreApplication.translate("Dialog", u"FALTAN DATOS", None))
    # retranslateUi

