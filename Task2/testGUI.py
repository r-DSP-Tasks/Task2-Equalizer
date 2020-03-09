# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 905)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1083, 905))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.input = QtWidgets.QWidget()
        self.input.setObjectName("input")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.input)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sliderChangedGraph = PlotWidget(self.input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderChangedGraph.sizePolicy().hasHeightForWidth())
        self.sliderChangedGraph.setSizePolicy(sizePolicy)
        self.sliderChangedGraph.setMinimumSize(QtCore.QSize(250, 500))
        self.sliderChangedGraph.setObjectName("sliderChangedGraph")
        self.gridLayout_3.addWidget(self.sliderChangedGraph, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rectangle = QtWidgets.QRadioButton(self.input)
        self.rectangle.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rectangle.setChecked(True)
        self.rectangle.setObjectName("rectangle")
        self.verticalLayout_5.addWidget(self.rectangle)
        self.hanning = QtWidgets.QRadioButton(self.input)
        self.hanning.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hanning.setObjectName("hanning")
        self.verticalLayout_5.addWidget(self.hanning)
        self.hamming = QtWidgets.QRadioButton(self.input)
        self.hamming.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hamming.setObjectName("hamming")
        self.verticalLayout_5.addWidget(self.hamming)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.inputSignalGraph = PlotWidget(self.input)
        self.inputSignalGraph.setMinimumSize(QtCore.QSize(90, 130))
        self.inputSignalGraph.setObjectName("inputSignalGraph")
        self.horizontalLayout_3.addWidget(self.inputSignalGraph)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.input)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(1500, 150))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.saveResult = QtWidgets.QPushButton(self.groupBox)
        self.saveResult.setEnabled(False)
        self.saveResult.setMinimumSize(QtCore.QSize(10, 20))
        self.saveResult.setMaximumSize(QtCore.QSize(350, 140))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.saveResult.setPalette(palette)
        self.saveResult.setObjectName("saveResult")
        self.gridLayout_2.addWidget(self.saveResult, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.playResult = QtWidgets.QPushButton(self.groupBox)
        self.playResult.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icons8-play-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playResult.setIcon(icon)
        self.playResult.setObjectName("playResult")
        self.gridLayout_2.addWidget(self.playResult, 2, 2, 1, 1)
        self.resetBands = QtWidgets.QPushButton(self.groupBox)
        self.resetBands.setEnabled(False)
        self.resetBands.setObjectName("resetBands")
        self.gridLayout_2.addWidget(self.resetBands, 2, 3, 1, 1)
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        self.playButton.setEnabled(False)
        self.playButton.setText("")
        self.playButton.setIcon(icon)
        self.playButton.setFlat(True)
        self.playButton.setObjectName("playButton")
        self.gridLayout_2.addWidget(self.playButton, 0, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        self.stopButton.setEnabled(False)
        self.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/icons8-stop-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setFlat(True)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalSlider_7 = mySlider(self.input)
        self.verticalSlider_7.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_7.setMinimum(-12)
        self.verticalSlider_7.setMaximum(12)
        self.verticalSlider_7.setPageStep(1)
        self.verticalSlider_7.setSliderPosition(1)
        self.verticalSlider_7.setTracking(True)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_7.setTickInterval(1)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.gridLayout_5.addWidget(self.verticalSlider_7, 2, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.input)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 10, 1, 1)
        self.verticalSlider_2 = mySlider(self.input)
        self.verticalSlider_2.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_2.setMinimum(-12)
        self.verticalSlider_2.setMaximum(12)
        self.verticalSlider_2.setPageStep(1)
        self.verticalSlider_2.setSliderPosition(1)
        self.verticalSlider_2.setTracking(True)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_2.setTickInterval(1)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_5.addWidget(self.verticalSlider_2, 2, 1, 1, 1)
        self.verticalSlider = mySlider(self.input)
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider.setMinimum(-12)
        self.verticalSlider.setMaximum(12)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setSliderPosition(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider.setTickInterval(1)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_5.addWidget(self.verticalSlider, 2, 0, 1, 1)
        self.verticalSlider_4 = mySlider(self.input)
        self.verticalSlider_4.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_4.setMinimum(-12)
        self.verticalSlider_4.setMaximum(12)
        self.verticalSlider_4.setPageStep(1)
        self.verticalSlider_4.setSliderPosition(1)
        self.verticalSlider_4.setTracking(True)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_4.setTickInterval(1)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.gridLayout_5.addWidget(self.verticalSlider_4, 2, 3, 1, 1)
        self.verticalSlider_8 = mySlider(self.input)
        self.verticalSlider_8.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_8.setMinimum(-12)
        self.verticalSlider_8.setMaximum(12)
        self.verticalSlider_8.setPageStep(1)
        self.verticalSlider_8.setSliderPosition(1)
        self.verticalSlider_8.setTracking(True)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_8.setTickInterval(1)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.gridLayout_5.addWidget(self.verticalSlider_8, 2, 7, 1, 1)
        self.verticalSlider_6 = mySlider(self.input)
        self.verticalSlider_6.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_6.setMinimum(-12)
        self.verticalSlider_6.setMaximum(12)
        self.verticalSlider_6.setPageStep(1)
        self.verticalSlider_6.setSliderPosition(1)
        self.verticalSlider_6.setTracking(True)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_6.setTickInterval(1)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.gridLayout_5.addWidget(self.verticalSlider_6, 2, 5, 1, 1)
        self.verticalSlider_3 = mySlider(self.input)
        self.verticalSlider_3.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_3.setMinimum(-12)
        self.verticalSlider_3.setMaximum(12)
        self.verticalSlider_3.setPageStep(1)
        self.verticalSlider_3.setSliderPosition(1)
        self.verticalSlider_3.setTracking(True)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_3.setTickInterval(1)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout_5.addWidget(self.verticalSlider_3, 2, 2, 1, 1)
        self.verticalSlider_9 = mySlider(self.input)
        self.verticalSlider_9.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_9.setMinimum(-12)
        self.verticalSlider_9.setMaximum(12)
        self.verticalSlider_9.setPageStep(1)
        self.verticalSlider_9.setSliderPosition(1)
        self.verticalSlider_9.setTracking(True)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_9.setTickInterval(1)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.gridLayout_5.addWidget(self.verticalSlider_9, 2, 8, 1, 1)
        self.verticalSlider_10 = mySlider(self.input)
        self.verticalSlider_10.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_10.setMinimum(-12)
        self.verticalSlider_10.setMaximum(12)
        self.verticalSlider_10.setPageStep(1)
        self.verticalSlider_10.setSliderPosition(1)
        self.verticalSlider_10.setTracking(True)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_10.setTickInterval(1)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.gridLayout_5.addWidget(self.verticalSlider_10, 2, 9, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.input)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.input)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_15 = QtWidgets.QLabel(self.input)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.gridLayout_5.addLayout(self.verticalLayout, 2, 10, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 6, 1, 1)
        self.verticalSlider_5 = mySlider(self.input)
        self.verticalSlider_5.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalSlider_5.setMinimum(-12)
        self.verticalSlider_5.setMaximum(12)
        self.verticalSlider_5.setPageStep(1)
        self.verticalSlider_5.setSliderPosition(1)
        self.verticalSlider_5.setTracking(True)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_5.setTickInterval(1)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.gridLayout_5.addWidget(self.verticalSlider_5, 2, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 1, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 1, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 1, 8, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem11, 1, 7, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 1, 9, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 1, 10, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.input)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.input)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.input)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.input)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.input)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.input)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.input)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.input)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 7, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.input)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 8, 1, 1)
        self.label = QtWidgets.QLabel(self.input)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 9, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.input, "")
        self.output = QtWidgets.QWidget()
        self.output.setObjectName("output")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.output)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.inputFourierOriginal = PlotWidget(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputFourierOriginal.sizePolicy().hasHeightForWidth())
        self.inputFourierOriginal.setSizePolicy(sizePolicy)
        self.inputFourierOriginal.setMinimumSize(QtCore.QSize(250, 100))
        self.inputFourierOriginal.setObjectName("inputFourierOriginal")
        self.gridLayout.addWidget(self.inputFourierOriginal, 2, 0, 1, 1)
        self.inputTimeOriginal = PlotWidget(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTimeOriginal.sizePolicy().hasHeightForWidth())
        self.inputTimeOriginal.setSizePolicy(sizePolicy)
        self.inputTimeOriginal.setMinimumSize(QtCore.QSize(250, 100))
        self.inputTimeOriginal.setObjectName("inputTimeOriginal")
        self.gridLayout.addWidget(self.inputTimeOriginal, 0, 0, 1, 1)
        self.outputFourierModified = PlotWidget(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFourierModified.sizePolicy().hasHeightForWidth())
        self.outputFourierModified.setSizePolicy(sizePolicy)
        self.outputFourierModified.setMinimumSize(QtCore.QSize(250, 100))
        self.outputFourierModified.setObjectName("outputFourierModified")
        self.gridLayout.addWidget(self.outputFourierModified, 3, 0, 1, 1)
        self.outputTimeModified = PlotWidget(self.output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTimeModified.sizePolicy().hasHeightForWidth())
        self.outputTimeModified.setSizePolicy(sizePolicy)
        self.outputTimeModified.setMinimumSize(QtCore.QSize(250, 100))
        self.outputTimeModified.setObjectName("outputTimeModified")
        self.gridLayout.addWidget(self.outputTimeModified, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 2, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.pushButton_2 = QtWidgets.QPushButton(self.output)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.output)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.tabWidget.addTab(self.output, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionload = QtWidgets.QAction(MainWindow)
        self.actionload.setCheckable(False)
        self.actionload.setChecked(False)
        self.actionload.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-file-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionload.setIcon(icon2)
        self.actionload.setObjectName("actionload")
        self.toolBar.addAction(self.actionload)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rectangle.setText(_translate("MainWindow", "Rectangle"))
        self.hanning.setText(_translate("MainWindow", "Hanning"))
        self.hamming.setText(_translate("MainWindow", "Hamming"))
        self.label_3.setText(_translate("MainWindow", "Player"))
        self.saveResult.setText(_translate("MainWindow", "Save Result"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.playResult.setText(_translate("MainWindow", "Play Result"))
        self.resetBands.setText(_translate("MainWindow", "Reset Bands"))
        self.label_16.setText(_translate("MainWindow", "12 dB"))
        self.label_5.setText(_translate("MainWindow", "0 dB"))
        self.label_15.setText(_translate("MainWindow", "-12"))
        self.label_4.setText(_translate("MainWindow", "62HZ"))
        self.label_6.setText(_translate("MainWindow", "125 HZ"))
        self.label_7.setText(_translate("MainWindow", "250 HZ"))
        self.label_8.setText(_translate("MainWindow", "500 HZ"))
        self.label_9.setText(_translate("MainWindow", "1 KHZ"))
        self.label_10.setText(_translate("MainWindow", "2 KHZ"))
        self.label_11.setText(_translate("MainWindow", "4 KHZ"))
        self.label_12.setText(_translate("MainWindow", "8KHZ"))
        self.label_13.setText(_translate("MainWindow", "16 KHZ"))
        self.label.setText(_translate("MainWindow", "20 KHZ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input), _translate("MainWindow", "Input"))
        self.pushButton_2.setText(_translate("MainWindow", "save"))
        self.pushButton_3.setText(_translate("MainWindow", "compare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.output), _translate("MainWindow", "Output"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionload.setText(_translate("MainWindow", "load"))
from mySliderClass import mySlider
from pyqtgraph import PlotWidget
