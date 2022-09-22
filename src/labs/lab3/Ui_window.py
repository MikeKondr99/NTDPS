# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 530)
        self.btnLoad = QAction(MainWindow)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnSave = QAction(MainWindow)
        self.btnSave.setObjectName(u"btnSave")
        self.btnBubble = QAction(MainWindow)
        self.btnBubble.setObjectName(u"btnBubble")
        self.btnSelection = QAction(MainWindow)
        self.btnSelection.setObjectName(u"btnSelection")
        self.btnQuick = QAction(MainWindow)
        self.btnQuick.setObjectName(u"btnQuick")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.tbInput = QTextEdit(self.centralwidget)
        self.tbInput.setObjectName(u"tbInput")
        font = QFont()
        font.setFamily(u"Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tbInput.setFont(font)

        self.horizontalLayout.addWidget(self.tbInput)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.tbOutput = QTextEdit(self.centralwidget)
        self.tbOutput.setObjectName(u"tbOutput")
        self.tbOutput.setFont(font)

        self.horizontalLayout.addWidget(self.tbOutput)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.btnLoad)
        self.menu.addAction(self.btnSave)
        self.menu_2.addAction(self.btnBubble)
        self.menu_2.addAction(self.btnSelection)
        self.menu_2.addAction(self.btnQuick)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043e\u0447\u043a\u0438", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnBubble.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0437\u044b\u0440\u044c\u043a\u043e\u043c", None))
        self.btnSelection.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043e\u043c", None))
        self.btnQuick.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u043e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

