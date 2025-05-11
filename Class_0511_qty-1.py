from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.setWindowTitle('Hello QT6')
widget.resize(400,300)

grid = QtWidgets.QGridLayout(widget)

label = QtWidgets.QLabel(widget)
label.setText('TEST')
# label.move(30,30)
grid.addWidget(label,0,0)

label2 = QtWidgets.QLabel(widget)
label2.setText('POIUY')
# label2.move(30,50)
grid.addWidget(label2,1,0)

input1 = QtWidgets.QLineEdit(widget)
# input1.move(60, 30)
grid.addWidget(input1,0,1)

input2 = QtWidgets.QTextEdit(widget)
# text1.move(100, 100)
grid.addWidget(input2,1,1)

def test():
    print('hello')

btn = QtWidgets.QPushButton(widget)
btn.setText('按我按我')
grid.addWidget(btn, 2, 0)
btn.clicked.connect(test)


widget.show()

sys.exit(app.exec())