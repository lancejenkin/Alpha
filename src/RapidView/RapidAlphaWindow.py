# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RapidAlphaWindow.ui'
#
# Created: Sun Feb 12 09:44:11 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RapidAlphaWindow(object):
    def setupUi(self, RapidAlphaWindow):
        RapidAlphaWindow.setObjectName(_fromUtf8("RapidAlphaWindow"))
        RapidAlphaWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(RapidAlphaWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.InputDeviceList = QtGui.QComboBox(self.centralwidget)
        self.InputDeviceList.setMinimumSize(QtCore.QSize(211, 26))
        self.InputDeviceList.setObjectName(_fromUtf8("InputDeviceList"))
        self.horizontalLayout.addWidget(self.InputDeviceList)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.OutputDeviceList = QtGui.QComboBox(self.centralwidget)
        self.OutputDeviceList.setMinimumSize(QtCore.QSize(211, 26))
        self.OutputDeviceList.setObjectName(_fromUtf8("OutputDeviceList"))
        self.horizontalLayout.addWidget(self.OutputDeviceList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.StartMesurement = QtGui.QCommandLinkButton(self.centralwidget)
        self.StartMesurement.setObjectName(_fromUtf8("StartMesurement"))
        self.horizontalLayout_3.addWidget(self.StartMesurement)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.AlphaPlot = MatplotlibWidget(self.centralwidget)
        self.AlphaPlot.setObjectName(_fromUtf8("AlphaPlot"))
        self.verticalLayout.addWidget(self.AlphaPlot)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.SaveGraph = QtGui.QPushButton(self.centralwidget)
        self.SaveGraph.setObjectName(_fromUtf8("SaveGraph"))
        self.horizontalLayout_2.addWidget(self.SaveGraph)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.ExportData = QtGui.QPushButton(self.centralwidget)
        self.ExportData.setObjectName(_fromUtf8("ExportData"))
        self.horizontalLayout_2.addWidget(self.ExportData)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.LoadData = QtGui.QPushButton(self.centralwidget)
        self.LoadData.setObjectName(_fromUtf8("LoadData"))
        self.horizontalLayout_2.addWidget(self.LoadData)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.Exit = QtGui.QPushButton(self.centralwidget)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.horizontalLayout_2.addWidget(self.Exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        RapidAlphaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RapidAlphaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RapidAlphaWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RapidAlphaWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RapidAlphaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RapidAlphaWindow)
        QtCore.QMetaObject.connectSlotsByName(RapidAlphaWindow)

    def retranslateUi(self, RapidAlphaWindow):
        RapidAlphaWindow.setWindowTitle(QtGui.QApplication.translate("RapidAlphaWindow", "Rapid Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Input Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Output Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.StartMesurement.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Preform Measurement", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveGraph.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Save Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.ExportData.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Export CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadData.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Load Data", None, QtGui.QApplication.UnicodeUTF8))
        self.Exit.setText(QtGui.QApplication.translate("RapidAlphaWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget
