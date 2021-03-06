# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 332)
        MainWindow.setMinimumSize(QtCore.QSize(382, 332))
        MainWindow.setMaximumSize(QtCore.QSize(382, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(38, 32, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 171, 91))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton {\n"
"    background-color: rgb(209, 0, 174);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"    background-color: #a61c98;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 171, 91))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"    background-color: rgb(209, 0, 174);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"    background-color: #a61c98;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 361, 91))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3 {\n"
"    background-color: rgb(209, 0, 174);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"    background-color: #a61c98;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 171, 91))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("#pushButton_4 {\n"
"    background-color: rgb(209, 0, 174);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}\n"
"\n"
"#pushButton_4:hover {\n"
"    background-color: #a61c98;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 230, 171, 91))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("#pushButton_5 {\n"
"    background-color: rgb(209, 0, 174);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}\n"
"\n"
"#pushButton_5:hover {\n"
"    background-color: #a61c98;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 44pt \"Bebas Neue Cyrillic\";\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhotoConventor"))
        self.pushButton.setText(_translate("MainWindow", "To PNG"))
        self.pushButton_2.setText(_translate("MainWindow", "To JPG"))
        self.pushButton_3.setText(_translate("MainWindow", "SELECT FILE"))
        self.pushButton_4.setText(_translate("MainWindow", "To bmp"))
        self.pushButton_5.setText(_translate("MainWindow", "To tiff"))

