# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LookupRaster.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LookupRaster(object):
    def setupUi(self, LookupRaster):
        LookupRaster.setObjectName("LookupRaster")
        LookupRaster.resize(530, 250)
        self.centralwidget = QtWidgets.QWidget(LookupRaster)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainGridLayout = QtWidgets.QGridLayout()
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.rasterLabel = QtWidgets.QLabel(self.centralwidget)
        self.rasterLabel.setObjectName("rasterLabel")
        self.mainGridLayout.addWidget(self.rasterLabel, 0, 0, 1, 1)
        self.rasterToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.rasterToolButton.setObjectName("rasterToolButton")
        self.mainGridLayout.addWidget(self.rasterToolButton, 1, 2, 1, 1)
        self.rasterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.rasterComboBox.setObjectName("rasterComboBox")
        self.mainGridLayout.addWidget(self.rasterComboBox, 1, 0, 1, 2)
        self.lookupFieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.lookupFieldLabel.setObjectName("lookupFieldLabel")
        self.mainGridLayout.addWidget(self.lookupFieldLabel, 2, 0, 1, 1)
        self.lookupFieldComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.lookupFieldComboBox.setObjectName("lookupFieldComboBox")
        self.mainGridLayout.addWidget(self.lookupFieldComboBox, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainGridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.ratCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ratCheckBox.setChecked(True)
        self.ratCheckBox.setObjectName("ratCheckBox")
        self.mainGridLayout.addWidget(self.ratCheckBox, 4, 0, 1, 1)
        self.outRasterLabel = QtWidgets.QLabel(self.centralwidget)
        self.outRasterLabel.setObjectName("outRasterLabel")
        self.mainGridLayout.addWidget(self.outRasterLabel, 5, 0, 1, 1)
        self.outRasterToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.outRasterToolButton.setObjectName("outRasterToolButton")
        self.mainGridLayout.addWidget(self.outRasterToolButton, 6, 2, 1, 1)
        self.outRasterLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outRasterLineEdit.setObjectName("outRasterLineEdit")
        self.mainGridLayout.addWidget(self.outRasterLineEdit, 6, 0, 1, 2)
        self.applyPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyPushButton.setObjectName("applyPushButton")
        self.mainGridLayout.addWidget(self.applyPushButton, 7, 2, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.mainGridLayout.addWidget(self.cancelPushButton, 7, 1, 1, 1)
        self.mainGridLayout.setColumnStretch(0, 2)
        self.mainGridLayout.setColumnStretch(1, 1)
        self.mainGridLayout.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.mainGridLayout)
        LookupRaster.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LookupRaster)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 22))
        self.menubar.setObjectName("menubar")
        LookupRaster.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LookupRaster)
        self.statusbar.setObjectName("statusbar")
        LookupRaster.setStatusBar(self.statusbar)

        self.retranslateUi(LookupRaster)
        QtCore.QMetaObject.connectSlotsByName(LookupRaster)
        LookupRaster.setTabOrder(self.rasterComboBox, self.rasterToolButton)
        LookupRaster.setTabOrder(self.rasterToolButton, self.lookupFieldComboBox)
        LookupRaster.setTabOrder(self.lookupFieldComboBox, self.ratCheckBox)
        LookupRaster.setTabOrder(self.ratCheckBox, self.outRasterLineEdit)
        LookupRaster.setTabOrder(self.outRasterLineEdit, self.outRasterToolButton)
        LookupRaster.setTabOrder(self.outRasterToolButton, self.cancelPushButton)
        LookupRaster.setTabOrder(self.cancelPushButton, self.applyPushButton)

    def retranslateUi(self, LookupRaster):
        _translate = QtCore.QCoreApplication.translate
        LookupRaster.setWindowTitle(_translate("LookupRaster", "Lookup"))
        self.rasterLabel.setText(_translate("LookupRaster", "Raster"))
        self.rasterToolButton.setText(_translate("LookupRaster", "..."))
        self.lookupFieldLabel.setText(_translate("LookupRaster", "Lookup Fields"))
        self.ratCheckBox.setText(_translate("LookupRaster", "Append attribute table"))
        self.outRasterLabel.setText(_translate("LookupRaster", "Output lookup raster"))
        self.outRasterToolButton.setText(_translate("LookupRaster", "..."))
        self.applyPushButton.setText(_translate("LookupRaster", "Apply"))
        self.cancelPushButton.setText(_translate("LookupRaster", "Cancel"))