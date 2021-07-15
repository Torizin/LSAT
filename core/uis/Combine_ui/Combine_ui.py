# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Combine.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Combine(object):
    def setupUi(self, Combine):
        Combine.setObjectName("Combine")
        Combine.resize(551, 607)
        Combine.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../Images/Infinite_slope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Combine.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Combine)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainGridLayout = QtWidgets.QGridLayout()
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.outputGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.outputGroupBox.setObjectName("outputGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.outputGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.outpitGroupBoxGridLayout = QtWidgets.QGridLayout()
        self.outpitGroupBoxGridLayout.setObjectName("outpitGroupBoxGridLayout")
        self.combineRasterLineEdit = QtWidgets.QLineEdit(self.outputGroupBox)
        self.combineRasterLineEdit.setObjectName("combineRasterLineEdit")
        self.outpitGroupBoxGridLayout.addWidget(self.combineRasterLineEdit, 1, 0, 1, 1)
        self.combineRasterLabel = QtWidgets.QLabel(self.outputGroupBox)
        self.combineRasterLabel.setObjectName("combineRasterLabel")
        self.outpitGroupBoxGridLayout.addWidget(self.combineRasterLabel, 0, 0, 1, 1)
        self.combineRasterToolButton = QtWidgets.QToolButton(self.outputGroupBox)
        self.combineRasterToolButton.setObjectName("combineRasterToolButton")
        self.outpitGroupBoxGridLayout.addWidget(self.combineRasterToolButton, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.outpitGroupBoxGridLayout)
        self.mainGridLayout.addWidget(self.outputGroupBox, 2, 1, 1, 2)
        self.maskGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.maskGroupBox.setObjectName("maskGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.maskGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.maskGroupBoxGridLayout = QtWidgets.QGridLayout()
        self.maskGroupBoxGridLayout.setObjectName("maskGroupBoxGridLayout")
        self.maskToolButton = QtWidgets.QToolButton(self.maskGroupBox)
        self.maskToolButton.setEnabled(False)
        self.maskToolButton.setObjectName("maskToolButton")
        self.maskGroupBoxGridLayout.addWidget(self.maskToolButton, 1, 1, 1, 1)
        self.maskLineEdit = QtWidgets.QLineEdit(self.maskGroupBox)
        self.maskLineEdit.setEnabled(False)
        self.maskLineEdit.setObjectName("maskLineEdit")
        self.maskGroupBoxGridLayout.addWidget(self.maskLineEdit, 1, 0, 1, 1)
        self.maskRasterCheckBox = QtWidgets.QCheckBox(self.maskGroupBox)
        self.maskRasterCheckBox.setChecked(True)
        self.maskRasterCheckBox.setObjectName("maskRasterCheckBox")
        self.maskGroupBoxGridLayout.addWidget(self.maskRasterCheckBox, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.maskGroupBoxGridLayout)
        self.mainGridLayout.addWidget(self.maskGroupBox, 1, 1, 1, 2)
        self.inputGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.inputGroupBox.setObjectName("inputGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.inputGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputGroupBoxGridLayout = QtWidgets.QGridLayout()
        self.inputGroupBoxGridLayout.setObjectName("inputGroupBoxGridLayout")
        self.addToolButton = QtWidgets.QToolButton(self.inputGroupBox)
        self.addToolButton.setText("")
        self.addToolButton.setObjectName("addToolButton")
        self.inputGroupBoxGridLayout.addWidget(self.addToolButton, 0, 1, 1, 1)
        self.removeToolButton = QtWidgets.QToolButton(self.inputGroupBox)
        self.removeToolButton.setText("")
        self.removeToolButton.setObjectName("removeToolButton")
        self.inputGroupBoxGridLayout.addWidget(self.removeToolButton, 1, 1, 1, 1)
        self.setAsMaskToolButton = QtWidgets.QToolButton(self.inputGroupBox)
        self.setAsMaskToolButton.setEnabled(False)
        self.setAsMaskToolButton.setText("")
        self.setAsMaskToolButton.setObjectName("setAsMaskToolButton")
        self.inputGroupBoxGridLayout.addWidget(self.setAsMaskToolButton, 2, 1, 1, 1)
        self.rasterCollectionListWidget = QtWidgets.QListWidget(self.inputGroupBox)
        self.rasterCollectionListWidget.setAcceptDrops(True)
        self.rasterCollectionListWidget.setObjectName("rasterCollectionListWidget")
        self.inputGroupBoxGridLayout.addWidget(self.rasterCollectionListWidget, 0, 0, 4, 1)
        self.inputGroupBoxGridLayout.setColumnStretch(0, 5)
        self.verticalLayout_2.addLayout(self.inputGroupBoxGridLayout)
        self.mainGridLayout.addWidget(self.inputGroupBox, 0, 1, 1, 2)
        self.applyPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyPushButton.setObjectName("applyPushButton")
        self.mainGridLayout.addWidget(self.applyPushButton, 3, 2, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.mainGridLayout.addWidget(self.cancelPushButton, 3, 1, 1, 1)
        self.mainGridLayout.setRowStretch(0, 4)
        self.mainGridLayout.setRowStretch(1, 1)
        self.mainGridLayout.setRowStretch(2, 2)
        self.verticalLayout.addLayout(self.mainGridLayout)
        Combine.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Combine)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 18))
        self.menubar.setObjectName("menubar")
        Combine.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Combine)
        self.statusbar.setObjectName("statusbar")
        Combine.setStatusBar(self.statusbar)

        self.retranslateUi(Combine)
        QtCore.QMetaObject.connectSlotsByName(Combine)
        Combine.setTabOrder(self.rasterCollectionListWidget, self.addToolButton)
        Combine.setTabOrder(self.addToolButton, self.removeToolButton)
        Combine.setTabOrder(self.removeToolButton, self.setAsMaskToolButton)
        Combine.setTabOrder(self.setAsMaskToolButton, self.maskRasterCheckBox)
        Combine.setTabOrder(self.maskRasterCheckBox, self.maskLineEdit)
        Combine.setTabOrder(self.maskLineEdit, self.maskToolButton)
        Combine.setTabOrder(self.maskToolButton, self.combineRasterLineEdit)
        Combine.setTabOrder(self.combineRasterLineEdit, self.combineRasterToolButton)
        Combine.setTabOrder(self.combineRasterToolButton, self.cancelPushButton)
        Combine.setTabOrder(self.cancelPushButton, self.applyPushButton)

    def retranslateUi(self, Combine):
        _translate = QtCore.QCoreApplication.translate
        Combine.setWindowTitle(_translate("Combine", "Combine"))
        self.outputGroupBox.setTitle(_translate("Combine", "Output"))
        self.combineRasterLabel.setText(_translate("Combine", "Combine raster dataset"))
        self.combineRasterToolButton.setText(_translate("Combine", "..."))
        self.maskGroupBox.setTitle(_translate("Combine", "Mask raster"))
        self.maskToolButton.setText(_translate("Combine", "..."))
        self.maskRasterCheckBox.setText(_translate("Combine", "Use the Projects default Mask raster"))
        self.inputGroupBox.setTitle(_translate("Combine", "Input raster datasets"))
        self.applyPushButton.setText(_translate("Combine", "Apply"))
        self.cancelPushButton.setText(_translate("Combine", "Cancel"))