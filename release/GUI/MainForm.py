# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UiM(object):
    def setupUi(self, UiM):
        UiM.setObjectName("UiM")
        UiM.resize(1019, 300)
        self.verticalWidget = QtWidgets.QWidget(UiM)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 10, 1001, 281))
        self.verticalWidget.setAcceptDrops(False)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addButton = QtWidgets.QPushButton(self.verticalWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.verticalWidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(UiM)
        QtCore.QMetaObject.connectSlotsByName(UiM)

    def retranslateUi(self, UiM):
        _translate = QtCore.QCoreApplication.translate
        UiM.setWindowTitle(_translate("UiM", "Coffee"))
        self.addButton.setText(_translate("UiM", "Добавить"))
        self.editButton.setText(_translate("UiM", "Изменить"))
