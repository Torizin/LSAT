# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Project.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Project(object):
    def setupUi(self, Project):
        Project.setObjectName("Project")
        Project.resize(450, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(Project)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainGridLayout = QtWidgets.QGridLayout()
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.createProjectPushButton = QtWidgets.QPushButton(Project)
        self.createProjectPushButton.setObjectName("createProjectPushButton")
        self.mainGridLayout.addWidget(self.createProjectPushButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainGridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.spatialReferenceGroupBox = QtWidgets.QGroupBox(Project)
        self.spatialReferenceGroupBox.setObjectName("spatialReferenceGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.spatialReferenceGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spatialReferenceGroupBoxGridLayout = QtWidgets.QGridLayout()
        self.spatialReferenceGroupBoxGridLayout.setObjectName("spatialReferenceGroupBoxGridLayout")
        self.rightLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.rightLineEdit.setObjectName("rightLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.rightLineEdit, 10, 2, 1, 1)
        self.topLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName("topLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.topLabel, 8, 1, 1, 1)
        self.extentLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.extentLabel.setObjectName("extentLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.extentLabel, 7, 0, 1, 3)
        self.cellsizeLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.cellsizeLabel.setObjectName("cellsizeLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.cellsizeLabel, 14, 0, 1, 3)
        self.maskRasterDatasetLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.maskRasterDatasetLineEdit.setObjectName("maskRasterDatasetLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.maskRasterDatasetLineEdit, 1, 0, 1, 2)
        self.bottomLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.bottomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bottomLabel.setObjectName("bottomLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.bottomLabel, 13, 1, 1, 1)
        self.bottomLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.bottomLineEdit.setObjectName("bottomLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.bottomLineEdit, 12, 1, 1, 1)
        self.leftLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.leftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.leftLabel.setObjectName("leftLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.leftLabel, 9, 0, 1, 1)
        self.maskRasterDatasetLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.maskRasterDatasetLabel.setObjectName("maskRasterDatasetLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.maskRasterDatasetLabel, 0, 0, 1, 1)
        self.topLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.topLineEdit.setObjectName("topLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.topLineEdit, 9, 1, 1, 1)
        self.maskRasterDatasetToolButton = QtWidgets.QToolButton(self.spatialReferenceGroupBox)
        self.maskRasterDatasetToolButton.setObjectName("maskRasterDatasetToolButton")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.maskRasterDatasetToolButton, 1, 2, 1, 1)
        self.leftLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.leftLineEdit.setObjectName("leftLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.leftLineEdit, 10, 0, 1, 1)
        self.cellsizeLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.cellsizeLineEdit.setObjectName("cellsizeLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.cellsizeLineEdit, 15, 0, 1, 2)
        self.rightLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.rightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightLabel.setObjectName("rightLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.rightLabel, 9, 2, 1, 1)
        self.epsgCodeLabel = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.epsgCodeLabel.setObjectName("epsgCodeLabel")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.epsgCodeLabel, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.spatialReferenceGroupBox)
        self.label.setObjectName("label")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.epsgCodeLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.epsgCodeLineEdit.setObjectName("epsgCodeLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.epsgCodeLineEdit, 6, 0, 1, 1)
        self.epsgToolButton = QtWidgets.QToolButton(self.spatialReferenceGroupBox)
        self.epsgToolButton.setObjectName("epsgToolButton")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.epsgToolButton, 6, 1, 1, 1)
        self.srNameLineEdit = QtWidgets.QLineEdit(self.spatialReferenceGroupBox)
        self.srNameLineEdit.setObjectName("srNameLineEdit")
        self.spatialReferenceGroupBoxGridLayout.addWidget(self.srNameLineEdit, 4, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.spatialReferenceGroupBoxGridLayout)
        self.mainGridLayout.addWidget(self.spatialReferenceGroupBox, 2, 0, 1, 2)
        self.generalGroupBox = QtWidgets.QGroupBox(Project)
        self.generalGroupBox.setObjectName("generalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.generalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.generalGroupBoxGridLayout = QtWidgets.QGridLayout()
        self.generalGroupBoxGridLayout.setObjectName("generalGroupBoxGridLayout")
        self.projectNameLineEdit = QtWidgets.QLineEdit(self.generalGroupBox)
        self.projectNameLineEdit.setObjectName("projectNameLineEdit")
        self.generalGroupBoxGridLayout.addWidget(self.projectNameLineEdit, 3, 0, 1, 1)
        self.projectNameLabel = QtWidgets.QLabel(self.generalGroupBox)
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.generalGroupBoxGridLayout.addWidget(self.projectNameLabel, 2, 0, 1, 1)
        self.descriptionLabel = QtWidgets.QLabel(self.generalGroupBox)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.generalGroupBoxGridLayout.addWidget(self.descriptionLabel, 4, 0, 1, 1)
        self.projectLocationLineEdit = QtWidgets.QLineEdit(self.generalGroupBox)
        self.projectLocationLineEdit.setObjectName("projectLocationLineEdit")
        self.generalGroupBoxGridLayout.addWidget(self.projectLocationLineEdit, 1, 0, 1, 1)
        self.projectLocationToolButton = QtWidgets.QToolButton(self.generalGroupBox)
        self.projectLocationToolButton.setObjectName("projectLocationToolButton")
        self.generalGroupBoxGridLayout.addWidget(self.projectLocationToolButton, 1, 1, 1, 1)
        self.projectLocationLabel = QtWidgets.QLabel(self.generalGroupBox)
        self.projectLocationLabel.setObjectName("projectLocationLabel")
        self.generalGroupBoxGridLayout.addWidget(self.projectLocationLabel, 0, 0, 1, 1)
        self.descriptionTextEdit = QtWidgets.QTextEdit(self.generalGroupBox)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.generalGroupBoxGridLayout.addWidget(self.descriptionTextEdit, 5, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.generalGroupBoxGridLayout)
        self.mainGridLayout.addWidget(self.generalGroupBox, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.mainGridLayout)

        self.retranslateUi(Project)
        QtCore.QMetaObject.connectSlotsByName(Project)

    def retranslateUi(self, Project):
        _translate = QtCore.QCoreApplication.translate
        Project.setWindowTitle(_translate("Project", "Dialog"))
        self.createProjectPushButton.setText(_translate("Project", "Create project"))
        self.spatialReferenceGroupBox.setTitle(_translate("Project", "Spatial Reference"))
        self.topLabel.setText(_translate("Project", "Top"))
        self.extentLabel.setText(_translate("Project", "Extent"))
        self.cellsizeLabel.setText(_translate("Project", "Cell size"))
        self.bottomLabel.setText(_translate("Project", "Bottom"))
        self.leftLabel.setText(_translate("Project", "Left"))
        self.maskRasterDatasetLabel.setText(_translate("Project", "Mask raster dataset (Optional)"))
        self.maskRasterDatasetToolButton.setText(_translate("Project", "..."))
        self.rightLabel.setText(_translate("Project", "Right"))
        self.epsgCodeLabel.setText(_translate("Project", "EPSG code"))
        self.label.setText(_translate("Project", "Name of Coordinate System"))
        self.epsgToolButton.setText(_translate("Project", "..."))
        self.generalGroupBox.setTitle(_translate("Project", "General"))
        self.projectNameLabel.setText(_translate("Project", "Project name"))
        self.descriptionLabel.setText(_translate("Project", "Description"))
        self.projectLocationToolButton.setText(_translate("Project", "..."))
        self.projectLocationLabel.setText(_translate("Project", "Project location"))