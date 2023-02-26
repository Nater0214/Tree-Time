# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 606)
        MainWindow.setStyleSheet(u"/*\n"
"ManjaroMix Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 25/02/2020, 15:42.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/ManjaroMix.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#151a1e;\n"
"}\n"
"QCalendar {\n"
"	background-color: #151a1e;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, "
                        "x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
""
                        "	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
""
                        "	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #FFFFFF;\n"
"	padding: 2px;\n"
"	background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-color: #050a0e;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"	background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	b"
                        "order-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"	background-color: #222b2e;\n"
"	color: #d3dae3;\n"
"}\n"
"QLabel {\n"
"	color: #d3dae3;\n"
"}\n"
"QLCDNumber {\n"
"	color: #4d9b87;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: #d3dae3;\n"
"	border-radius: 10px;\n"
"	border-color: transparent;\n"
"	border-style: solid;\n"
"	background-color: #52595d;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #214037	;\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: #151a1e;\n"
"}\n"
"QMenuBar::item {\n"
"	color: #d3dae3;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: #151a1e;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: #252"
                        "a2e;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"	background-color: #151a1e;\n"
"}\n"
"QMenu::item:selected {\n"
"	background-color: #252a2e;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item {\n"
"	color: #d3dae3;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: #050a0e;\n"
"		background-color: #1e282c;\n"
"		border-style: solid;\n"
"		border-width: 1px;\n"
"    	border-bottom-left-radius: 4px;\n"
"		border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	border-top-left-radius: 4px;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
""
                        "	border-left-width:1px;\n"
"	border-right-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-color: #050a0e;\n"
"	border-top-right-radius: 4px;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-left-width:1px;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #d3dae3;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-bottom-width:0px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #1e282c;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:fi"
                        "rst:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:0px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: #050a0e;\n"
"	border-left-color: #050a0e;\n"
"	border-bottom-color: #050a0e;\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: #1e282c;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #d3dae3;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #000000;\n"
"	background-color: qradialgradient(cx:0.4, cy:0.4, radius: 1.5,fx:0, fy:0, stop:0"
                        " #1e282c, stop:0.3 #1e282c, stop:0.4 #4fa08b, stop:0.5 #1e282c, stop:1 #1e282c);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: #d3dae3;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #a9b7c6;\n"
"	background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #4fa08b, stop:1 #1e282c);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #4fa08b;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1p"
                        "x;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QTimeEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QDateEdit {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QFontComboBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"QComboBox {\n"
"	color: #d3dae3;\n"
"	background-color: #222b2e;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: #4fa08b;\n"
"}\n"
"\n"
"QDial {\n"
"	backgroun"
                        "d: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#222b2e;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: #52595d;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: #52595d;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: #1a2224;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: #1a2224;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: #52595d;\n"
"}\n"
"QSlider"
                        "::add-page:vertical {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #15433a;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #15433a;\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 10px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"	background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 10px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"	background: transparent;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: #52595d;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: #58a492;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: #52595d;\n"
"	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: #58a492;\n"
""
                        "	border-style: transparent;\n"
"	border-radius: 4px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bott"
                        "om-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 671, 291))
        self.label_2.setPixmap(QPixmap(u":/src/images/images/treetimepic.png"))
        self.label_2.setScaledContents(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/src/images/images/startimage.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.setupButton = QPushButton(self.centralwidget)
        self.setupButton.setObjectName(u"setupButton")

        self.gridLayout.addWidget(self.setupButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tree Time - Start", None))
        self.label_2.setText("")
        self.label.setText("")
        self.setupButton.setText(QCoreApplication.translate("MainWindow", u"Click Here to Start", None))
    # retranslateUi

