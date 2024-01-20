from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Курб'як")
main_win.resize(900, 70)
wnner = QLabel('Натисни,щоб дізнатися переможця')
a = QLabel('&')
button = QPushButton('Згенерувати')
v_line1= QVBoxLayout()

v_line1.addWidget(wnner, alignment = Qt.AlignCenter)
v_line1.addWidget(a, alignment = Qt.AlignCenter)
v_line1.addWidget(button, alignment = Qt.AlignCenter)

main_win.setLayout(v_line1)

def show_winner():
    number = randint(0, 99)
    a.setText(str(number))
    wnner.setText('Переможець:')
button.clicked.connect(show_winner)
main_win.show()
app.exec_()