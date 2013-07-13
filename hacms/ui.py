# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jul 13 14:41:47 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

#from PySide import QtCore, QtGui
from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 718)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.landsharkButton = QtGui.QPushButton(self.centralWidget)
        self.landsharkButton.setGeometry(QtCore.QRect(20, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.landsharkButton.setFont(font)
        self.landsharkButton.setCheckable(True)
        self.landsharkButton.setObjectName("landsharkButton")
        self.rcButton = QtGui.QPushButton(self.centralWidget)
        self.rcButton.setEnabled(False)
        self.rcButton.setGeometry(QtCore.QRect(20, 170, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rcButton.setFont(font)
        self.rcButton.setCheckable(True)
        self.rcButton.setObjectName("rcButton")
        self.attackButton = QtGui.QPushButton(self.centralWidget)
        self.attackButton.setEnabled(False)
        self.attackButton.setGeometry(QtCore.QRect(20, 250, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.attackButton.setFont(font)
        self.attackButton.setCheckable(True)
        self.attackButton.setObjectName("attackButton")
        self.actualSpeedLCD = QtGui.QLCDNumber(self.centralWidget)
        self.actualSpeedLCD.setEnabled(False)
        self.actualSpeedLCD.setGeometry(QtCore.QRect(280, 170, 171, 71))
        self.actualSpeedLCD.setObjectName("actualSpeedLCD")
        self.estimatedLabel = QtGui.QLabel(self.centralWidget)
        self.estimatedLabel.setEnabled(False)
        self.estimatedLabel.setGeometry(QtCore.QRect(30, 400, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.estimatedLabel.setFont(font)
        self.estimatedLabel.setStyleSheet("background-color: green; color: white;")
        self.estimatedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.estimatedLabel.setObjectName("estimatedLabel")
        self.actualLabel = QtGui.QLabel(self.centralWidget)
        self.actualLabel.setEnabled(False)
        self.actualLabel.setGeometry(QtCore.QRect(30, 330, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.actualLabel.setFont(font)
        self.actualLabel.setStyleSheet("background-color: green; color: white;")
        self.actualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actualLabel.setObjectName("actualLabel")
        self.desiredSpeedLabel = QtGui.QLabel(self.centralWidget)
        self.desiredSpeedLabel.setEnabled(False)
        self.desiredSpeedLabel.setGeometry(QtCore.QRect(280, 20, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.desiredSpeedLabel.setFont(font)
        self.desiredSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.desiredSpeedLabel.setObjectName("desiredSpeedLabel")
        self.desiredSpeedEdit = QtGui.QLineEdit(self.centralWidget)
        self.desiredSpeedEdit.setEnabled(False)
        self.desiredSpeedEdit.setGeometry(QtCore.QRect(310, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.desiredSpeedEdit.setFont(font)
        self.desiredSpeedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.desiredSpeedEdit.setObjectName("desiredSpeedEdit")
        self.actualSpeedLabel = QtGui.QLabel(self.centralWidget)
        self.actualSpeedLabel.setEnabled(False)
        self.actualSpeedLabel.setGeometry(QtCore.QRect(280, 150, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actualSpeedLabel.setFont(font)
        self.actualSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actualSpeedLabel.setObjectName("actualSpeedLabel")
        self.console = QtGui.QPlainTextEdit(self.centralWidget)
        self.console.setGeometry(QtCore.QRect(20, 490, 1211, 161))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        self.console.setFont(font)
        self.console.setPlainText("")
        self.console.setObjectName("console")
        self.outputPlot = QtGui.QWidget(self.centralWidget)
        self.outputPlot.setEnabled(False)
        self.outputPlot.setGeometry(QtCore.QRect(470, 30, 331, 201))
        self.outputPlot.setStyleSheet("background-color: white;")
        self.outputPlot.setObjectName("outputPlot")
        self.outputPlotLabel = QtGui.QLabel(self.centralWidget)
        self.outputPlotLabel.setEnabled(False)
        self.outputPlotLabel.setGeometry(QtCore.QRect(470, 10, 62, 16))
        self.outputPlotLabel.setObjectName("outputPlotLabel")
        self.estimatedSpeedLabel = QtGui.QLabel(self.centralWidget)
        self.estimatedSpeedLabel.setEnabled(False)
        self.estimatedSpeedLabel.setGeometry(QtCore.QRect(280, 260, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.estimatedSpeedLabel.setFont(font)
        self.estimatedSpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.estimatedSpeedLabel.setObjectName("estimatedSpeedLabel")
        self.estimatedSpeedLCD = QtGui.QLCDNumber(self.centralWidget)
        self.estimatedSpeedLCD.setEnabled(False)
        self.estimatedSpeedLCD.setGeometry(QtCore.QRect(280, 280, 171, 71))
        self.estimatedSpeedLCD.setObjectName("estimatedSpeedLCD")
        self.ccButton = QtGui.QPushButton(self.centralWidget)
        self.ccButton.setEnabled(False)
        self.ccButton.setGeometry(QtCore.QRect(20, 90, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ccButton.setFont(font)
        self.ccButton.setCheckable(True)
        self.ccButton.setObjectName("ccButton")
        self.setSpeedButton = QtGui.QPushButton(self.centralWidget)
        self.setSpeedButton.setEnabled(False)
        self.setSpeedButton.setGeometry(QtCore.QRect(310, 100, 101, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setSpeedButton.setFont(font)
        self.setSpeedButton.setObjectName("setSpeedButton")
        self.inputPlotLabel = QtGui.QLabel(self.centralWidget)
        self.inputPlotLabel.setEnabled(False)
        self.inputPlotLabel.setGeometry(QtCore.QRect(470, 250, 62, 16))
        self.inputPlotLabel.setObjectName("inputPlotLabel")
        self.inputPlot = QtGui.QWidget(self.centralWidget)
        self.inputPlot.setEnabled(False)
        self.inputPlot.setGeometry(QtCore.QRect(470, 270, 331, 201))
        self.inputPlot.setStyleSheet("background-color: white;")
        self.inputPlot.setObjectName("inputPlot")
        self.rightPlot = QtGui.QWidget(self.centralWidget)
        self.rightPlot.setEnabled(False)
        self.rightPlot.setGeometry(QtCore.QRect(810, 30, 421, 441))
        self.rightPlot.setStyleSheet("background-color: white;")
        self.rightPlot.setObjectName("rightPlot")
        self.rightPlotLabel = QtGui.QLabel(self.centralWidget)
        self.rightPlotLabel.setEnabled(False)
        self.rightPlotLabel.setGeometry(QtCore.QRect(810, 10, 71, 16))
        self.rightPlotLabel.setObjectName("rightPlotLabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1251, 22))
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.landsharkButton, self.ccButton)
        MainWindow.setTabOrder(self.ccButton, self.rcButton)
        MainWindow.setTabOrder(self.rcButton, self.attackButton)
        MainWindow.setTabOrder(self.attackButton, self.desiredSpeedEdit)
        MainWindow.setTabOrder(self.desiredSpeedEdit, self.setSpeedButton)
        MainWindow.setTabOrder(self.setSpeedButton, self.console)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "HACMS Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.landsharkButton.setText(QtGui.QApplication.translate("MainWindow", "Landshark", None, QtGui.QApplication.UnicodeUTF8))
        self.rcButton.setText(QtGui.QApplication.translate("MainWindow", "Resilient Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.attackButton.setText(QtGui.QApplication.translate("MainWindow", "Attack", None, QtGui.QApplication.UnicodeUTF8))
        self.estimatedLabel.setText(QtGui.QApplication.translate("MainWindow", "Estimated", None, QtGui.QApplication.UnicodeUTF8))
        self.actualLabel.setText(QtGui.QApplication.translate("MainWindow", "Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.desiredSpeedLabel.setText(QtGui.QApplication.translate("MainWindow", "Desired Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.desiredSpeedEdit.setText(QtGui.QApplication.translate("MainWindow", "0.8", None, QtGui.QApplication.UnicodeUTF8))
        self.actualSpeedLabel.setText(QtGui.QApplication.translate("MainWindow", "Actual Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.outputPlotLabel.setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.estimatedSpeedLabel.setText(QtGui.QApplication.translate("MainWindow", "Estimated Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.ccButton.setText(QtGui.QApplication.translate("MainWindow", "Cruise Control", None, QtGui.QApplication.UnicodeUTF8))
        self.setSpeedButton.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPlotLabel.setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.rightPlotLabel.setText(QtGui.QApplication.translate("MainWindow", "Odometry", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

