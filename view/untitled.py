# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1278, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_ultrason = QtWidgets.QPushButton(self.centralwidget)
        self.button_ultrason.setGeometry(QtCore.QRect(160, 270, 89, 25))
        self.button_ultrason.setAutoDefault(False)
        self.button_ultrason.setFlat(False)
        self.button_ultrason.setObjectName("button_ultrason")
        self.widget_ultrason = QtWidgets.QWidget(self.centralwidget)
        self.widget_ultrason.setGeometry(QtCore.QRect(70, 70, 299, 155))
        self.widget_ultrason.setAutoFillBackground(False)
        self.widget_ultrason.setObjectName("widget_ultrason")
        self.widget_lumiere = QtWidgets.QWidget(self.centralwidget)
        self.widget_lumiere.setGeometry(QtCore.QRect(430, 70, 299, 155))
        self.widget_lumiere.setObjectName("widget_lumiere")
        self.widget_led = QtWidgets.QWidget(self.centralwidget)
        self.widget_led.setGeometry(QtCore.QRect(900, 70, 121, 152))
        self.widget_led.setObjectName("widget_led")
        self.button_lumiere = QtWidgets.QPushButton(self.centralwidget)
        self.button_lumiere.setGeometry(QtCore.QRect(540, 270, 89, 25))
        self.button_lumiere.setObjectName("button_lumiere")
        self.button_led = QtWidgets.QPushButton(self.centralwidget)
        self.button_led.setGeometry(QtCore.QRect(920, 270, 89, 25))
        self.button_led.setObjectName("button_led")
        self.label_ultrason = QtWidgets.QLabel(self.centralwidget)
        self.label_ultrason.setGeometry(QtCore.QRect(160, 240, 91, 20))
        self.label_ultrason.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ultrason.setWordWrap(True)
        self.label_ultrason.setObjectName("label_ultrason")
        self.label_lumiere = QtWidgets.QLabel(self.centralwidget)
        self.label_lumiere.setGeometry(QtCore.QRect(540, 240, 81, 20))
        self.label_lumiere.setTextFormat(QtCore.Qt.AutoText)
        self.label_lumiere.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lumiere.setWordWrap(True)
        self.label_lumiere.setObjectName("label_lumiere")
        self.label_infos = QtWidgets.QLabel(self.centralwidget)
        self.label_infos.setGeometry(QtCore.QRect(390, 390, 391, 20))
        self.label_infos.setText("")
        self.label_infos.setObjectName("label_infos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1278, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_ultrason.setText(_translate("MainWindow", "Désactiver"))
        self.button_lumiere.setText(_translate("MainWindow", "Désactiver"))
        self.button_led.setText(_translate("MainWindow", "Désactiver"))
        self.label_ultrason.setText(_translate("MainWindow", "0"))
        self.label_lumiere.setText(_translate("MainWindow", "0"))
