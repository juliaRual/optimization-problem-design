# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(569, 423)
        Form.setStyleSheet(u"background-color: #22222e")
        self.pushButton_calculate = QPushButton(Form)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(30, 320, 131, 51))
        font = QFont()
        font.setFamilies([u"PT Mono"])
        font.setPointSize(18)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_calculate.setMouseTracking(False)
        self.pushButton_calculate.setStyleSheet(u"background-color: rgb(221, 130, 96);\n"
"border-radius: 25;\n"
"")
        self.lineEdit_k1 = QLineEdit(Form)
        self.lineEdit_k1.setObjectName(u"lineEdit_k1")
        self.lineEdit_k1.setGeometry(QRect(30, 110, 131, 51))
        font1 = QFont()
        font1.setFamilies([u"PT Mono"])
        font1.setPointSize(14)
        self.lineEdit_k1.setFont(font1)
        self.lineEdit_k1.setStyleSheet(u"color: rgb(214, 214, 214);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 25;")
        self.lineEdit_k1.setAlignment(Qt.AlignCenter)
        self.lineEdit_k2 = QLineEdit(Form)
        self.lineEdit_k2.setObjectName(u"lineEdit_k2")
        self.lineEdit_k2.setGeometry(QRect(30, 180, 131, 51))
        self.lineEdit_k2.setFont(font1)
        self.lineEdit_k2.setStyleSheet(u"color: rgb(214, 214, 214);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 25;")
        self.lineEdit_k2.setAlignment(Qt.AlignCenter)
        self.lineEdit_k3 = QLineEdit(Form)
        self.lineEdit_k3.setObjectName(u"lineEdit_k3")
        self.lineEdit_k3.setGeometry(QRect(30, 250, 131, 51))
        self.lineEdit_k3.setFont(font1)
        self.lineEdit_k3.setStyleSheet(u"color: rgb(214, 214, 214);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 25;")
        self.lineEdit_k3.setAlignment(Qt.AlignCenter)
        self.textEdit_result = QTextEdit(Form)
        self.textEdit_result.setObjectName(u"textEdit_result")
        self.textEdit_result.setGeometry(QRect(220, 160, 291, 211))
        self.textEdit_result.setFont(font1)
        self.textEdit_result.setStyleSheet(u"color: white;\n"
"border: 2px dashed white;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 110, 311, 41))
        font2 = QFont()
        font2.setFamilies([u"PT Mono"])
        font2.setPointSize(24)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: white")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -20, 571, 111))
        self.frame.setStyleSheet(u"background-color: rgb(221, 130, 96);\n"
"border-radius: 20;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 501, 16))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 40, 441, 21))
        font3 = QFont()
        font3.setFamilies([u"PT Mono"])
        font3.setPointSize(20)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: white")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 581, 421))
        self.label_4.setPixmap(QPixmap(u"fon.png"))
        self.label_4.raise_()
        self.pushButton_calculate.raise_()
        self.lineEdit_k1.raise_()
        self.lineEdit_k2.raise_()
        self.lineEdit_k3.raise_()
        self.textEdit_result.raise_()
        self.label_3.raise_()
        self.frame.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"BerdnikovaJulia", None))
#if QT_CONFIG(statustip)
        Form.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_calculate.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_k1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_k1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_k1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_k1.setInputMask("")
        self.lineEdit_k1.setText("")
        self.lineEdit_k1.setPlaceholderText(QCoreApplication.translate("Form", u"\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041a1", None))
        self.lineEdit_k2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041a2", None))
        self.lineEdit_k3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u041a3", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(statustip)
        self.label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1 \u043a\u0443\u0440\u0441\u043e\u0432\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0422\u041f\u0420. \u0411\u0435\u0440\u0434\u043d\u0438\u043a\u043e\u0432\u0430 \u042e\u043b\u0438\u044f, \u0418\u0410\u0421-20-1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u041c\u0410\u041a\u0421\u0418\u041c\u0418\u0417\u0410\u0426\u0418\u042f \u0421\u0423\u041c\u041c\u0410\u0420\u041d\u041e\u0413\u041e \u041e\u0411\u042a\u0415\u041c\u0410 \u0421\u0411\u042b\u0422\u0410</p></body></html>", None))
        self.label_4.setText("")
    # retranslateUi

