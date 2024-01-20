from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

app = QApplication([])
main_win = QWidget()
question = QLabel('В якому році?')
btn_answer1 = QRadioButton('Скільки грибів в лісі')
btn_answer2 = QRadioButton('1999')
btn_answer3 = QRadioButton('Масло в моторі')
btn_answer4 = QRadioButton('2000')

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно!\nВи виграли мотор мій')
    victory_win.exec_()
def show_lose():
    victory_lose= QMessageBox()
    victory_lose.setText('Правильно!\nВи виграли мотор мій')
    victory_lose.exec_()
v_line1= QVBoxLayout()

v_line1.addWidget(question, alignment = Qt.AlignCenter)
v_line1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
v_line1.addWidget(btn_answer2, alignment = Qt.AlignCenter)
v_line1.addWidget(btn_answer3, alignment = Qt.AlignCenter)
v_line1.addWidget(btn_answer4, alignment = Qt.AlignCenter)
main_win.setLayout(v_line1)
btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()