# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 686)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setSizeIncrement(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.identify_buttom = QPushButton(self.centralwidget)
        self.identify_buttom.setObjectName(u"identify_buttom")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.identify_buttom.sizePolicy().hasHeightForWidth())
        self.identify_buttom.setSizePolicy(sizePolicy1)
        self.identify_buttom.setCheckable(True)
        self.identify_buttom.setChecked(False)

        self.horizontalLayout_5.addWidget(self.identify_buttom)

        self.addUser_buttom = QPushButton(self.centralwidget)
        self.addUser_buttom.setObjectName(u"addUser_buttom")
        sizePolicy1.setHeightForWidth(self.addUser_buttom.sizePolicy().hasHeightForWidth())
        self.addUser_buttom.setSizePolicy(sizePolicy1)
        self.addUser_buttom.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.addUser_buttom)

        self.addFace_buttom = QPushButton(self.centralwidget)
        self.addFace_buttom.setObjectName(u"addFace_buttom")

        self.horizontalLayout_5.addWidget(self.addFace_buttom)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.addFaceMenu = QHBoxLayout()
        self.addFaceMenu.setObjectName(u"addFaceMenu")
        self.addFaceMenu.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.addFrontal_Buttom = QPushButton(self.centralwidget)
        self.addFrontal_Buttom.setObjectName(u"addFrontal_Buttom")
        self.addFrontal_Buttom.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.addFrontal_Buttom.sizePolicy().hasHeightForWidth())
        self.addFrontal_Buttom.setSizePolicy(sizePolicy1)
        self.addFrontal_Buttom.setCheckable(False)
        self.addFrontal_Buttom.setChecked(False)

        self.addFaceMenu.addWidget(self.addFrontal_Buttom)

        self.addRight_buttom = QPushButton(self.centralwidget)
        self.addRight_buttom.setObjectName(u"addRight_buttom")
        self.addRight_buttom.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.addRight_buttom.sizePolicy().hasHeightForWidth())
        self.addRight_buttom.setSizePolicy(sizePolicy1)
        self.addRight_buttom.setCheckable(False)

        self.addFaceMenu.addWidget(self.addRight_buttom)

        self.addLeft_buttom = QPushButton(self.centralwidget)
        self.addLeft_buttom.setObjectName(u"addLeft_buttom")
        self.addLeft_buttom.setEnabled(True)

        self.addFaceMenu.addWidget(self.addLeft_buttom)


        self.verticalLayout.addLayout(self.addFaceMenu)

        self.imageFrame = QFrame(self.centralwidget)
        self.imageFrame.setObjectName(u"imageFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageFrame.sizePolicy().hasHeightForWidth())
        self.imageFrame.setSizePolicy(sizePolicy2)
        self.imageFrame.setMinimumSize(QSize(800, 600))
        self.imageFrame.setSizeIncrement(QSize(0, 0))
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.imageFrame)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.identify_buttom.setText(QCoreApplication.translate("MainWindow", u"Identificar", None))
        self.addUser_buttom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir usuario", None))
        self.addFace_buttom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir cara", None))
        self.addFrontal_Buttom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir frontal", None))
        self.addRight_buttom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir perfil derecho", None))
        self.addLeft_buttom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir perfil izquierdo", None))
    # retranslateUi

