from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.setWindowTitle('Hello QT6')
widget.resize(700,600)

# 網格
grid = QtWidgets.QGridLayout(widget)

label = QtWidgets.QLabel(widget)
label.setText('輸入框1')
# label.move(20,35) mark it due to via grid
grid.addWidget(label,0,0)

label2 = QtWidgets.QLabel(widget)
label2.setText('輸入框2')
# label2.move(20,75) mark it due to via grid
grid.addWidget(label2,1,0)

input1 = QtWidgets.QLineEdit(widget)
# input1.move(80,30) mark it due to via grid
grid.addWidget(input1,0,1)

input2 = QtWidgets.QTextEdit(widget)
# text1.move(100, 100)
grid.addWidget(input2,1,1)

# 顯示輸入的text
showLabel = QtWidgets.QLabel(widget)
grid.addWidget(showLabel,3,1)

def test():
    # print('hello')
    showLabel.setText((input1.text()))


btn = QtWidgets.QPushButton(widget)
btn.setText('確定')

# def clrtext():
#     # print('hello')
#     # showLabel.setText((input1.text()))
#     showLabel.clear(input1)
# clrbtn = QtWidgets.QPushButton(widget)
# clrbtn.setText('清除')

# ======================================================
# ======================================================

grid.addWidget(btn, 3, 0)
btn.clicked.connect(test)

# grid.addWidget(clrbtn, 3,0 )
# clrbtn.clicked.connect(test)


widget.show()
sys.exit(app.exec())
