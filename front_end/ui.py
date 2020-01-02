# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_end/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(640, 200))
        Dialog.setMaximumSize(QtCore.QSize(640, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"color: white;\n"
"border-style: outset;\n"
"height: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(40, 40, 40);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)
        self.confirm_button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.confirm_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirm_button.setAutoFillBackground(True)
        self.confirm_button.setStyleSheet("")
        self.confirm_button.setCheckable(False)
        self.confirm_button.setAutoDefault(False)
        self.confirm_button.setDefault(False)
        self.confirm_button.setFlat(False)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout.addWidget(self.confirm_button, 0, 2, 1, 1)
        self.no_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_button.sizePolicy().hasHeightForWidth())
        self.no_button.setSizePolicy(sizePolicy)
        self.no_button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.no_button.setFont(font)
        self.no_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.no_button.setAutoFillBackground(True)
        self.no_button.setStyleSheet("")
        self.no_button.setCheckable(False)
        self.no_button.setChecked(False)
        self.no_button.setAutoDefault(False)
        self.no_button.setDefault(False)
        self.no_button.setFlat(False)
        self.no_button.setObjectName("no_button")
        self.gridLayout.addWidget(self.no_button, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Desktop Setter"))
        self.label.setText(_translate("Dialog", "This application will change your desktop background. Continue?"))
        self.confirm_button.setText(_translate("Dialog", "Yes"))
        self.no_button.setText(_translate("Dialog", "No"))
