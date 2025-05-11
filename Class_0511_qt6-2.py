from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.setWindowTitle('盎司毫升轉換器')

label1 = QtWidgets.QLabel(widget)
label1.setText('請輸入轉換的數字')

label2 = QtWidgets.QLabel(widget)
label2.setText('單位是oz還是ml?(o/m)')

input1 = QtWidgets.QLineEdit(widget)

# input2 = QtWidgets.QLineEdit(widget)
input2 = QtWidgets.QComboBox(widget)
input2.addItems(['o','m'])

btn = QtWidgets.QPushButton('換算')

resultLabel = QtWidgets.QLabel(widget)

grid = QtWidgets.QGridLayout(widget)
grid.addWidget(label1,0,0)
grid.addWidget(input1,0,1)
grid.addWidget(label2,1,0)
grid.addWidget(input2,1,1)
grid.addWidget(btn,2,1)
grid.addWidget(resultLabel,3,0,1,2)

def oz():
    # s = input2.text()
    s = input2.currentText()
    x = int(input1.text())
    if s =='o':
        result = float(x) * 29.573
        result = str(round(result,2))
        print(f'您的換算結果為{x}oz約{result}ml')
        resultLabel.setText(f'您的換算結果為{x}oz約{result}ml')
    else:
        result = float(x) / 29.573
        result = str(round(result,2))
        print(f'您的換算結果為{x}ml約{result}oz')
        resultLabel.setText(f'您的換算結果為{x}ml約{result}oz')


btn.clicked.connect(oz)

widget.show()

sys.exit(app.exec())