import sys
from PySide6 import QtCore, QtWidgets
from gui import Ui_Form
from calculator import abs

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# app logic
def btn():
    k1 = int(ui.lineEdit_k1.text())
    k2 = int(ui.lineEdit_k2.text())
    k3 = int(ui.lineEdit_k3.text())
    out = abs(k1, k2, k3)
    ui.textEdit_result.setText(f"""
 Исходя по потребностей рынка: 
 Фирме "Х" следует запланировать 
 сборку {out[0]} млн. копьютеров

 Из них:
 Стацонарных {out[1]} млн.
 Переносных {out[2]} млн.
 
 Цена игры фирмы "Х" и фирмы "У" 
 составила: V = {out[0]} """ )

    print(out)


ui.pushButton_calculate.clicked.connect(btn)
# run app

sys.exit(app.exec())

