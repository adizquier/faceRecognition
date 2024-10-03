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
        MainWindow.resize(820, 653)
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
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.captureButton = QPushButton(self.centralwidget)
        self.captureButton.setObjectName(u"captureButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.captureButton.sizePolicy().hasHeightForWidth())
        self.captureButton.setSizePolicy(sizePolicy1)
        self.captureButton.setCheckable(True)
        self.captureButton.setChecked(True)

        self.horizontalLayout.addWidget(self.captureButton)

        self.addUser_buttom = QPushButton(self.centralwidget)
        self.addUser_buttom.setObjectName(u"addUser_buttom")
        sizePolicy1.setHeightForWidth(self.addUser_buttom.sizePolicy().hasHeightForWidth())
        self.addUser_buttom.setSizePolicy(sizePolicy1)
        self.addUser_buttom.setCheckable(True)

        self.horizontalLayout.addWidget(self.addUser_buttom)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"Stop capture", None))
        self.addUser_buttom.setText(QCoreApplication.translate("MainWindow", u"Detect face", None))
    # retranslateUi

