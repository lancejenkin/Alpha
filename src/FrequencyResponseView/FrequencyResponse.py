# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrequencyResponse.ui'
#
# Created: Fri Jul  6 15:00:54 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FrequencyResponse(object):
    def setupUi(self, FrequencyResponse):
        FrequencyResponse.setObjectName(_fromUtf8("FrequencyResponse"))
        FrequencyResponse.resize(801, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/frequency_response.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrequencyResponse.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(FrequencyResponse)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(281, 0))
        self.frame.setMaximumSize(QtCore.QSize(281, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(self.frame)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 253, 274))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_28 = QtGui.QLabel(self.page)
        self.label_28.setMaximumSize(QtCore.QSize(51, 16777215))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_26.addWidget(self.label_28)
        self.inputDevices = QtGui.QComboBox(self.page)
        self.inputDevices.setObjectName(_fromUtf8("inputDevices"))
        self.horizontalLayout_26.addWidget(self.inputDevices)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_30 = QtGui.QLabel(self.page)
        self.label_30.setMaximumSize(QtCore.QSize(51, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_27.addWidget(self.label_30)
        self.outputDevices = QtGui.QComboBox(self.page)
        self.outputDevices.setObjectName(_fromUtf8("outputDevices"))
        self.horizontalLayout_27.addWidget(self.outputDevices)
        self.verticalLayout_4.addLayout(self.horizontalLayout_27)
        spacerItem = QtGui.QSpacerItem(20, 211, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/speaker.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 253, 274))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.signalType = QtGui.QComboBox(self.page_2)
        self.signalType.setObjectName(_fromUtf8("signalType"))
        self.signalType.addItem(_fromUtf8(""))
        self.signalType.addItem(_fromUtf8(""))
        self.signalType.addItem(_fromUtf8(""))
        self.signalType.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.signalType)
        self.signalOptions = QtGui.QStackedWidget(self.page_2)
        self.signalOptions.setObjectName(_fromUtf8("signalOptions"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_4 = QtGui.QLabel(self.page_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.numTaps = QtGui.QSpinBox(self.page_5)
        self.numTaps.setObjectName(_fromUtf8("numTaps"))
        self.horizontalLayout_9.addWidget(self.numTaps)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_23 = QtGui.QLabel(self.page_5)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_8.addWidget(self.label_23)
        self.numBursts = QtGui.QSpinBox(self.page_5)
        self.numBursts.setObjectName(_fromUtf8("numBursts"))
        self.horizontalLayout_8.addWidget(self.numBursts)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.signalOptions.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.page_6)
        self.label_5.setMinimumSize(QtCore.QSize(22, 25))
        self.label_5.setMaximumSize(QtCore.QSize(22, 25))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.upperFreq = QtGui.QSpinBox(self.page_6)
        self.upperFreq.setMaximum(20000)
        self.upperFreq.setObjectName(_fromUtf8("upperFreq"))
        self.horizontalLayout_6.addWidget(self.upperFreq)
        self.label_8 = QtGui.QLabel(self.page_6)
        self.label_8.setMinimumSize(QtCore.QSize(17, 25))
        self.label_8.setMaximumSize(QtCore.QSize(17, 25))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.page_6)
        self.label_6.setMaximumSize(QtCore.QSize(27, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.signalLength = QtGui.QSpinBox(self.page_6)
        self.signalLength.setMaximum(99999)
        self.signalLength.setObjectName(_fromUtf8("signalLength"))
        self.horizontalLayout_7.addWidget(self.signalLength)
        self.label_7 = QtGui.QLabel(self.page_6)
        self.label_7.setMaximumSize(QtCore.QSize(19, 25))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.signalOptions.addWidget(self.page_6)
        self.verticalLayout_5.addWidget(self.signalOptions)
        self.line = QtGui.QFrame(self.page_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_22 = QtGui.QLabel(self.page_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_5.addWidget(self.label_22)
        self.numRepititions = QtGui.QSpinBox(self.page_2)
        self.numRepititions.setObjectName(_fromUtf8("numRepititions"))
        self.horizontalLayout_5.addWidget(self.numRepititions)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(20, 99, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/signal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 253, 274))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.filterType = QtGui.QComboBox(self.page_3)
        self.filterType.setObjectName(_fromUtf8("filterType"))
        self.filterType.addItem(_fromUtf8(""))
        self.filterType.addItem(_fromUtf8(""))
        self.filterType.addItem(_fromUtf8(""))
        self.filterType.addItem(_fromUtf8(""))
        self.verticalLayout_11.addWidget(self.filterType)
        self.filterOptions = QtGui.QStackedWidget(self.page_3)
        self.filterOptions.setObjectName(_fromUtf8("filterOptions"))
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.filterOptions.addWidget(self.page_7)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.page_8)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.page_8)
        self.label_10.setMinimumSize(QtCore.QSize(25, 25))
        self.label_10.setMaximumSize(QtCore.QSize(27, 25))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.freqLPF = QtGui.QSpinBox(self.page_8)
        self.freqLPF.setMaximum(20000)
        self.freqLPF.setObjectName(_fromUtf8("freqLPF"))
        self.horizontalLayout_10.addWidget(self.freqLPF)
        self.label_11 = QtGui.QLabel(self.page_8)
        self.label_11.setMinimumSize(QtCore.QSize(17, 25))
        self.label_11.setMaximumSize(QtCore.QSize(17, 25))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(self.page_8)
        self.label_12.setMaximumSize(QtCore.QSize(35, 25))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.orderLPF = QtGui.QSpinBox(self.page_8)
        self.orderLPF.setMaximum(99999)
        self.orderLPF.setObjectName(_fromUtf8("orderLPF"))
        self.horizontalLayout_12.addWidget(self.orderLPF)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.filterOptions.addWidget(self.page_8)
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.page_9)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_13 = QtGui.QLabel(self.page_9)
        self.label_13.setMinimumSize(QtCore.QSize(25, 25))
        self.label_13.setMaximumSize(QtCore.QSize(27, 25))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_13.addWidget(self.label_13)
        self.freqHPF = QtGui.QSpinBox(self.page_9)
        self.freqHPF.setMaximum(20000)
        self.freqHPF.setObjectName(_fromUtf8("freqHPF"))
        self.horizontalLayout_13.addWidget(self.freqHPF)
        self.label_14 = QtGui.QLabel(self.page_9)
        self.label_14.setMinimumSize(QtCore.QSize(17, 25))
        self.label_14.setMaximumSize(QtCore.QSize(17, 25))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_15 = QtGui.QLabel(self.page_9)
        self.label_15.setMaximumSize(QtCore.QSize(35, 25))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_14.addWidget(self.label_15)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.orderHPF = QtGui.QSpinBox(self.page_9)
        self.orderHPF.setMaximum(99999)
        self.orderHPF.setObjectName(_fromUtf8("orderHPF"))
        self.horizontalLayout_15.addWidget(self.orderHPF)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.filterOptions.addWidget(self.page_9)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName(_fromUtf8("page_10"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.page_10)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_16 = QtGui.QLabel(self.page_10)
        self.label_16.setMinimumSize(QtCore.QSize(25, 25))
        self.label_16.setMaximumSize(QtCore.QSize(25, 25))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_16.addWidget(self.label_16)
        self.freqLow = QtGui.QSpinBox(self.page_10)
        self.freqLow.setMaximum(20000)
        self.freqLow.setObjectName(_fromUtf8("freqLow"))
        self.horizontalLayout_16.addWidget(self.freqLow)
        self.label_17 = QtGui.QLabel(self.page_10)
        self.label_17.setMinimumSize(QtCore.QSize(17, 25))
        self.label_17.setMaximumSize(QtCore.QSize(17, 25))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_16.addWidget(self.label_17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_18 = QtGui.QLabel(self.page_10)
        self.label_18.setMaximumSize(QtCore.QSize(35, 25))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_17.addWidget(self.label_18)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.orderLow = QtGui.QSpinBox(self.page_10)
        self.orderLow.setMaximum(99999)
        self.orderLow.setObjectName(_fromUtf8("orderLow"))
        self.horizontalLayout_18.addWidget(self.orderLow)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_19 = QtGui.QLabel(self.page_10)
        self.label_19.setMinimumSize(QtCore.QSize(25, 25))
        self.label_19.setMaximumSize(QtCore.QSize(25, 25))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_19.addWidget(self.label_19)
        self.freqHigh = QtGui.QSpinBox(self.page_10)
        self.freqHigh.setMaximum(20000)
        self.freqHigh.setObjectName(_fromUtf8("freqHigh"))
        self.horizontalLayout_19.addWidget(self.freqHigh)
        self.label_20 = QtGui.QLabel(self.page_10)
        self.label_20.setMinimumSize(QtCore.QSize(17, 25))
        self.label_20.setMaximumSize(QtCore.QSize(17, 25))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_19.addWidget(self.label_20)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_21 = QtGui.QLabel(self.page_10)
        self.label_21.setMaximumSize(QtCore.QSize(35, 25))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_20.addWidget(self.label_21)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.orderHigh = QtGui.QSpinBox(self.page_10)
        self.orderHigh.setMaximum(99999)
        self.orderHigh.setObjectName(_fromUtf8("orderHigh"))
        self.horizontalLayout_21.addWidget(self.orderHigh)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.filterOptions.addWidget(self.page_10)
        self.verticalLayout_11.addWidget(self.filterOptions)
        spacerItem4 = QtGui.QSpacerItem(20, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon3, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 253, 274))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_32 = QtGui.QLabel(self.page_4)
        self.label_32.setMinimumSize(QtCore.QSize(51, 16))
        self.label_32.setMaximumSize(QtCore.QSize(51, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_25.addWidget(self.label_32)
        self.winLength = QtGui.QSpinBox(self.page_4)
        self.winLength.setMaximum(99999)
        self.winLength.setObjectName(_fromUtf8("winLength"))
        self.horizontalLayout_25.addWidget(self.winLength)
        self.label_33 = QtGui.QLabel(self.page_4)
        self.label_33.setMinimumSize(QtCore.QSize(51, 16))
        self.label_33.setMaximumSize(QtCore.QSize(51, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_25.addWidget(self.label_33)
        self.verticalLayout_12.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_29 = QtGui.QLabel(self.page_4)
        self.label_29.setMinimumSize(QtCore.QSize(41, 16))
        self.label_29.setMaximumSize(QtCore.QSize(41, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_24.addWidget(self.label_29)
        self.taperLength = QtGui.QSpinBox(self.page_4)
        self.taperLength.setMaximum(99999)
        self.taperLength.setObjectName(_fromUtf8("taperLength"))
        self.horizontalLayout_24.addWidget(self.taperLength)
        self.label_31 = QtGui.QLabel(self.page_4)
        self.label_31.setMinimumSize(QtCore.QSize(51, 16))
        self.label_31.setMaximumSize(QtCore.QSize(51, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_24.addWidget(self.label_31)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        spacerItem5 = QtGui.QSpacerItem(20, 209, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/impulse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_4, icon4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.startButton = QtGui.QPushButton(self.frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon5)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.impulsePlot = MatplotlibWidget(self.centralwidget)
        self.impulsePlot.setMinimumSize(QtCore.QSize(0, 148))
        self.impulsePlot.setMaximumSize(QtCore.QSize(16777215, 148))
        self.impulsePlot.setObjectName(_fromUtf8("impulsePlot"))
        self.verticalLayout_2.addWidget(self.impulsePlot)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frequencyPlot = MatplotlibWidget(self.centralwidget)
        self.frequencyPlot.setObjectName(_fromUtf8("frequencyPlot"))
        self.verticalLayout_2.addWidget(self.frequencyPlot)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        FrequencyResponse.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FrequencyResponse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        FrequencyResponse.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FrequencyResponse)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FrequencyResponse.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FrequencyResponse)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        FrequencyResponse.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(FrequencyResponse)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon6)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(FrequencyResponse)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(FrequencyResponse)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()

        self.retranslateUi(FrequencyResponse)
        self.toolBox.setCurrentIndex(0)
        self.signalOptions.setCurrentIndex(0)
        self.filterOptions.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(FrequencyResponse)

    def retranslateUi(self, FrequencyResponse):
        FrequencyResponse.setWindowTitle(QtGui.QApplication.translate("FrequencyResponse", "Frequency Response", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("FrequencyResponse", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("FrequencyResponse", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("FrequencyResponse", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.signalType.setItemText(0, QtGui.QApplication.translate("FrequencyResponse", "Inverse Repeat Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.signalType.setItemText(1, QtGui.QApplication.translate("FrequencyResponse", "Maximum Length Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.signalType.setItemText(2, QtGui.QApplication.translate("FrequencyResponse", "Swept Sine", None, QtGui.QApplication.UnicodeUTF8))
        self.signalType.setItemText(3, QtGui.QApplication.translate("FrequencyResponse", "Low Pass Swept Sine", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FrequencyResponse", "Taps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("FrequencyResponse", "Bursts", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>f<span style=\" vertical-align:sub;\">high</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FrequencyResponse", "Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>T<span style=\" vertical-align:sub;\">span</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FrequencyResponse", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("FrequencyResponse", "Signal Repitions", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("FrequencyResponse", "Signal", None, QtGui.QApplication.UnicodeUTF8))
        self.filterType.setItemText(0, QtGui.QApplication.translate("FrequencyResponse", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.filterType.setItemText(1, QtGui.QApplication.translate("FrequencyResponse", "Low Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.filterType.setItemText(2, QtGui.QApplication.translate("FrequencyResponse", "High Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.filterType.setItemText(3, QtGui.QApplication.translate("FrequencyResponse", "Band Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>f<span style=\" vertical-align:sub;\">c_LPF</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("FrequencyResponse", "Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>f<span style=\" vertical-align:sub;\">c_HPF</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("FrequencyResponse", "Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>f<span style=\" vertical-align:sub;\">c_low</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("FrequencyResponse", "Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>f<span style=\" vertical-align:sub;\">c_high</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("FrequencyResponse", "Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("FrequencyResponse", "<html><head/><body><p>Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("FrequencyResponse", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("FrequencyResponse", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("FrequencyResponse", "samples", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("FrequencyResponse", "Taper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("FrequencyResponse", "samples", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("FrequencyResponse", "Extraction", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("FrequencyResponse", "Start Measurment", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FrequencyResponse", "Impulse Response", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FrequencyResponse", "Frequency Response", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FrequencyResponse", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("FrequencyResponse", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("FrequencyResponse", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("FrequencyResponse", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("FrequencyResponse", "Save...", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget
import icons_rc
