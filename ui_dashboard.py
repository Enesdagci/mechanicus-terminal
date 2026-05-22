# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/* Master Background */\n"
"QMainWindow {\n"
"    background-color: #050f05; /* Deep, dark green/black */\n"
"}\n"
"\n"
"/* Panel Frames */\n"
"QFrame {\n"
"    background-color: #0a170a;\n"
"    border: 2px solid #1a4a1a;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* Typography and Labels */\n"
"QLabel {\n"
"    color: #4af626; /* Bright phosphor green */\n"
"    font-family: \"Consolas\", \"Courier New\", monospace;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: none; /* Removes border from text */\n"
"}\n"
"\n"
"/* Terminal and Lists */\n"
"QTextEdit, QListWidget, QGraphicsView {\n"
"    background-color: #020502;\n"
"    color: #4af626;\n"
"    border: 1px solid #2a7a2a;\n"
"    font-family: \"Consolas\", monospace;\n"
"}\n"
"\n"
"/* Standard Buttons */\n"
"QPushButton {\n"
"    background-color: #1a4a1a;\n"
"    color: #4af626;\n"
"    border: 1px solid #4af626;\n"
"    font-family: \"Consolas\", monospace;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {"
                        "\n"
"    background-color: #4af626;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* The Emergency Stop Button */\n"
"QPushButton#pushButton_2 { /* Change this ID to match your E-Stop button's objectName! */\n"
"    background-color: #4a0a0a;\n"
"    color: #ff3333;\n"
"    border: 2px solid #ff3333;\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: #ff3333;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Reactor Core / Progress Bar */\n"
"QProgressBar {\n"
"    border: 1px solid #4af626;\n"
"    background-color: #020502;\n"
"    text-align: center;\n"
"    color: #4af626;\n"
"    font-weight: bold;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #4af626;\n"
"    width: 10px; /* Creates that segmented, retro blocky look */\n"
"    margin: 1px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LeftFrame = QFrame(self.frame)
        self.LeftFrame.setObjectName(u"LeftFrame")
        self.LeftFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.LeftFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.progressBar = QProgressBar(self.LeftFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout_2.addWidget(self.LeftFrame)

        self.CenterFrame = QFrame(self.frame)
        self.CenterFrame.setObjectName(u"CenterFrame")
        self.CenterFrame.setFrameShape(QFrame.StyledPanel)
        self.CenterFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.CenterFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.CenterFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.graphicsView = QGraphicsView(self.CenterFrame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_3.addWidget(self.graphicsView)


        self.horizontalLayout_2.addWidget(self.CenterFrame)

        self.RightFrame = QFrame(self.frame)
        self.RightFrame.setObjectName(u"RightFrame")
        self.RightFrame.setFrameShape(QFrame.StyledPanel)
        self.RightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.RightFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.RightFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.listWidget = QListWidget(self.RightFrame)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.RightFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.RightFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.RightFrame)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_5.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[ SYSTEM TELEMETRY ]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[ MAIN AUSPEX ]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"[ COMMAND LINKS ]", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ENGAGE PROTOCOL", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY SCRAM", None))
    # retranslateUi

