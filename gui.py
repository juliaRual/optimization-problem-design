# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui3.ui'
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
        Form.resize(554, 648)
        Form.setStyleSheet(u"background-color: rgb(246, 255, 251)")
        self.pushButton_calculate = QPushButton(Form)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(40, 330, 471, 51))
        font = QFont()
        font.setFamilies([u"PT Sans Caption"])
        font.setPointSize(18)
        self.pushButton_calculate.setFont(font)
        self.pushButton_calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_calculate.setMouseTracking(False)
        self.pushButton_calculate.setStyleSheet(u"background-color: rgb(26, 104, 28);\n"
"border-radius: 12;\n"
"color: rgb(215, 255, 205);\n"
"")
        self.lineEdit_k1 = QLineEdit(Form)
        self.lineEdit_k1.setObjectName(u"lineEdit_k1")
        self.lineEdit_k1.setGeometry(QRect(40, 110, 471, 51))
        font1 = QFont()
        font1.setFamilies([u"PT Sans Caption"])
        font1.setPointSize(14)
        self.lineEdit_k1.setFont(font1)
        self.lineEdit_k1.setStyleSheet(u"color: rgb(24, 100, 18);\n"
"border: 2px solid rgb(26, 104, 28);\n"
"border-radius: 25;")
        self.lineEdit_k1.setAlignment(Qt.AlignCenter)
        self.lineEdit_k2 = QLineEdit(Form)
        self.lineEdit_k2.setObjectName(u"lineEdit_k2")
        self.lineEdit_k2.setGeometry(QRect(40, 180, 471, 51))
        self.lineEdit_k2.setFont(font1)
        self.lineEdit_k2.setStyleSheet(u"color: rgb(24, 100, 18);\n"
"border: 2px solid rgb(26, 104, 28);\n"
"border-radius: 25;")
        self.lineEdit_k2.setAlignment(Qt.AlignCenter)
        self.lineEdit_k3 = QLineEdit(Form)
        self.lineEdit_k3.setObjectName(u"lineEdit_k3")
        self.lineEdit_k3.setGeometry(QRect(40, 250, 471, 51))
        font2 = QFont()
        font2.setFamilies([u"Fira Code"])
        font2.setPointSize(14)
        self.lineEdit_k3.setFont(font2)
        self.lineEdit_k3.setStyleSheet(u"color: rgb(24, 100, 18);\n"
"border: 2px solid rgb(26, 104, 28);\n"
"border-radius: 25;")
        self.lineEdit_k3.setAlignment(Qt.AlignCenter)
        self.textEdit_result = QTextEdit(Form)
        self.textEdit_result.setObjectName(u"textEdit_result")
        self.textEdit_result.setGeometry(QRect(40, 400, 471, 191))
        self.textEdit_result.setFont(font1)
        self.textEdit_result.setStyleSheet(u"color: rgb(24, 100, 18);\n"
"border: 3px solid rgb(26, 104, 28);\n"
"border-radius: 12;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 600, 471, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(24, 100, 18);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 471, 21))
        font3 = QFont()
        font3.setFamilies([u"PT Sans Caption"])
        font3.setPointSize(17)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(24, 100, 18);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 561, 41))
        self.frame.setStyleSheet(u"background-color: rgb(26, 104, 28);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 331, 16))
        font4 = QFont()
        font4.setFamilies([u"PT Sans Caption"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(215, 255, 205);")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame.raise_()
        self.pushButton_calculate.raise_()
        self.lineEdit_k1.raise_()
        self.lineEdit_k2.raise_()
        self.lineEdit_k3.raise_()
        self.textEdit_result.raise_()
        self.label_3.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"taskOne", None))
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
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u0415\u0417\u0423\u041b\u042c\u0422\u0410\u0422 \u0412\u042b\u0427\u0418\u0421\u041b\u0415\u041d\u0418\u042f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0420\u0410\u0421\u0427\u0415\u0422 \u041e\u041f\u0422\u0418\u041c\u0410\u041b\u042c\u041d\u041e\u0413\u041e \u041a\u041e\u041b\u0418\u0427\u0415\u0421\u0422\u0412\u0410 \u041a\u041e\u041c\u041f\u042c\u042e\u0422\u0415\u0420\u041e\u0412</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0418\u043c\u044f\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0430. \u0417\u0430\u0434\u0430\u0447\u0430 \u21161</p></body></html>", None))
    # retranslateUi

