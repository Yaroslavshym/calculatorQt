# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorQT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 793)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color:black;\n"
"	color:white;\n"
"	\n"
"}\n"
"QPushButton{\n"
"	margin:2px;\n"
"	background-color:rgb(26,26,26);\n"
"	border-top-left-radius:35px;\n"
"	border-top-right-radius:35px;\n"
"	border-bottom-left-radius:35px;\n"
"	border-bottom-right-radius:35px;\n"
"	font-size:25px;\n"
"}\n"
"QPushButton:pressed{\n"
"	margin:10;\n"
"	border-top-left-radius:25px;\n"
"	border-top-right-radius:25px;\n"
"	border-bottom-left-radius:25px;\n"
"	border-bottom-right-radius:25px;\n"
"	font-size:22px;\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea_label_1 = QScrollArea(self.centralwidget)
        self.scrollArea_label_1.setObjectName(u"scrollArea_label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_label_1.sizePolicy().hasHeightForWidth())
        self.scrollArea_label_1.setSizePolicy(sizePolicy1)
        self.scrollArea_label_1.setMaximumSize(QSize(368, 16777215))
        self.scrollArea_label_1.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.scrollArea_label_1.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea_label_1.setLineWidth(2)
        self.scrollArea_label_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_label_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_label_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_label_1.setWidgetResizable(True)
        self.scrollArea_label_1.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-377, 0, 719, 76))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setLayoutDirection(Qt.RightToLeft)
        self.label_1.setStyleSheet(u"font-size:40px\n"
"")
        self.label_1.setInputMethodHints(Qt.ImhNone)
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_1.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.label_1)

        self.scrollArea_label_1.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_label_1)

        self.scrollArea_label_2 = QScrollArea(self.centralwidget)
        self.scrollArea_label_2.setObjectName(u"scrollArea_label_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_label_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_label_2.setSizePolicy(sizePolicy1)
        self.scrollArea_label_2.setMaximumSize(QSize(368, 16777215))
        self.scrollArea_label_2.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.scrollArea_label_2.setLayoutDirection(Qt.RightToLeft)
        self.scrollArea_label_2.setLineWidth(2)
        self.scrollArea_label_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_label_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_label_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_label_2.setWidgetResizable(True)
        self.scrollArea_label_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(-24, 0, 366, 76))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"color:rgb(151,151,151)")
        self.label_2.setInputMethodHints(Qt.ImhNone)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.label_2)

        self.scrollArea_label_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy3)
        self.pushButton_1.setMinimumSize(QSize(75, 75))
        self.pushButton_1.setSizeIncrement(QSize(0, 0))
        font = QFont()
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setAutoFillBackground(False)
        self.pushButton_1.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setSizeIncrement(QSize(0, 0))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setSizeIncrement(QSize(0, 0))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy3.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy3)
        self.pushButton_clear.setMinimumSize(QSize(75, 75))
        self.pushButton_clear.setSizeIncrement(QSize(0, 0))
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_clear.setAutoFillBackground(False)
        self.pushButton_clear.setStyleSheet(u"background-color:rgb(50,50,50);")
        self.pushButton_clear.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_clear, 0, 0, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy3.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy3)
        self.pushButton_0.setMinimumSize(QSize(75, 75))
        self.pushButton_0.setSizeIncrement(QSize(0, 0))
        self.pushButton_0.setFont(font)
        self.pushButton_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0.setAutoFillBackground(False)
        self.pushButton_0.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_backspace = QPushButton(self.centralwidget)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")
        sizePolicy3.setHeightForWidth(self.pushButton_backspace.sizePolicy().hasHeightForWidth())
        self.pushButton_backspace.setSizePolicy(sizePolicy3)
        self.pushButton_backspace.setMinimumSize(QSize(75, 75))
        self.pushButton_backspace.setSizeIncrement(QSize(0, 0))
        self.pushButton_backspace.setFont(font)
        self.pushButton_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backspace.setAutoFillBackground(False)
        self.pushButton_backspace.setStyleSheet(u"background-color:rgb(50,50,50);")
        self.pushButton_backspace.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_backspace, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setSizeIncrement(QSize(0, 0))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_00 = QPushButton(self.centralwidget)
        self.pushButton_00.setObjectName(u"pushButton_00")
        sizePolicy3.setHeightForWidth(self.pushButton_00.sizePolicy().hasHeightForWidth())
        self.pushButton_00.setSizePolicy(sizePolicy3)
        self.pushButton_00.setMinimumSize(QSize(75, 75))
        self.pushButton_00.setSizeIncrement(QSize(0, 0))
        self.pushButton_00.setFont(font)
        self.pushButton_00.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_00.setAutoFillBackground(False)
        self.pushButton_00.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_00, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(75, 75))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)
        self.pushButton_7.setMinimumSize(QSize(75, 75))
        self.pushButton_7.setSizeIncrement(QSize(0, 0))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setMinimumSize(QSize(75, 75))
        self.pushButton_8.setSizeIncrement(QSize(0, 0))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setMinimumSize(QSize(75, 75))
        self.pushButton_3.setSizeIncrement(QSize(0, 0))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_point = QPushButton(self.centralwidget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        sizePolicy3.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy3)
        self.pushButton_point.setMinimumSize(QSize(75, 75))
        self.pushButton_point.setSizeIncrement(QSize(0, 0))
        self.pushButton_point.setFont(font)
        self.pushButton_point.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_point.setAutoFillBackground(False)
        self.pushButton_point.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_point, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMinimumSize(QSize(75, 75))
        self.pushButton_9.setSizeIncrement(QSize(0, 0))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_mul = QPushButton(self.centralwidget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        sizePolicy3.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy3)
        self.pushButton_mul.setMinimumSize(QSize(75, 75))
        self.pushButton_mul.setSizeIncrement(QSize(0, 0))
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_mul.setAutoFillBackground(False)
        self.pushButton_mul.setStyleSheet(u"background-color:rgb(50,50,50);")
        self.pushButton_mul.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_mul, 1, 3, 1, 1)

        self.pushButton_div = QPushButton(self.centralwidget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        sizePolicy3.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy3)
        self.pushButton_div.setMinimumSize(QSize(75, 75))
        self.pushButton_div.setSizeIncrement(QSize(0, 0))
        self.pushButton_div.setFont(font)
        self.pushButton_div.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_div.setAutoFillBackground(False)
        self.pushButton_div.setStyleSheet(u"font-size:45px;\n"
"background-color:rgb(50,50,50);")
        self.pushButton_div.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_div, 0, 3, 1, 1)

        self.pushButton_min = QPushButton(self.centralwidget)
        self.pushButton_min.setObjectName(u"pushButton_min")
        sizePolicy3.setHeightForWidth(self.pushButton_min.sizePolicy().hasHeightForWidth())
        self.pushButton_min.setSizePolicy(sizePolicy3)
        self.pushButton_min.setMinimumSize(QSize(75, 75))
        self.pushButton_min.setSizeIncrement(QSize(0, 0))
        self.pushButton_min.setFont(font)
        self.pushButton_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_min.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_min.setAutoFillBackground(False)
        self.pushButton_min.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(50,50,50);\n"
"	font-size:33px;\n"
"}\n"
"QPushButton:pressed{\n"
"	font-size:30px;\n"
"\n"
"}")
        self.pushButton_min.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_min, 2, 3, 1, 1)

        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy4)
        self.pushButton_plus.setMinimumSize(QSize(75, 75))
        self.pushButton_plus.setSizeIncrement(QSize(0, 0))
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_plus.setAutoFillBackground(False)
        self.pushButton_plus.setStyleSheet(u"background-color:rgb(50,50,50);")
        self.pushButton_plus.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_plus, 3, 3, 1, 1)

        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        sizePolicy3.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy3)
        self.pushButton_equal.setMinimumSize(QSize(75, 75))
        self.pushButton_equal.setSizeIncrement(QSize(0, 0))
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_equal.setAutoFillBackground(False)
        self.pushButton_equal.setStyleSheet(u"background-color:rgb(225,0,126);")
        self.pushButton_equal.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_equal, 4, 3, 1, 1)

        self.pushButton_pi = QPushButton(self.centralwidget)
        self.pushButton_pi.setObjectName(u"pushButton_pi")
        sizePolicy3.setHeightForWidth(self.pushButton_pi.sizePolicy().hasHeightForWidth())
        self.pushButton_pi.setSizePolicy(sizePolicy3)
        self.pushButton_pi.setMinimumSize(QSize(75, 75))
        self.pushButton_pi.setSizeIncrement(QSize(0, 0))
        self.pushButton_pi.setFont(font)
        self.pushButton_pi.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_pi.setAutoFillBackground(False)
        self.pushButton_pi.setStyleSheet(u"background-color:rgb(50,50,50);")
        self.pushButton_pi.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_pi, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"9193810380129830912830918938x5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"9193810380129830912830918938x5", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_backspace.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_00.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_mul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_min.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
    # retranslateUi

