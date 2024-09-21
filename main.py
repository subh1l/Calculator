import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(QSize(360, 450))

        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QGridLayout()

        self.button_map = {}
        button_layout = QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "root"],
            ["4", "5", "6", "*", "square"],
            ["1", "2", "3", "-", "C"],
            ["0", ".", "%", "+", "="],
        ]

        for row, keys in enumerate(keyboard):
            for col, keyboard_key in enumerate(keys):
                self.button_map[keyboard_key] = QPushButton(keyboard_key)
                self.button_map[keyboard_key].setFixedSize(QSize(40, 40))
        layout3.addWidget(QPushButton("7"), 0, 0)
        layout3.addWidget(QPushButton("8"), 0, 1)
        layout3.addWidget(QPushButton("9"), 0, 2)
        layout3.addWidget(QPushButton("/"), 0, 3)
        layout3.addWidget(QPushButton("root"), 0, 4)
        layout3.addWidget(QPushButton("4"), 1, 0)
        layout3.addWidget(QPushButton("5"), 1, 1)
        layout3.addWidget(QPushButton("6"), 1, 2)
        layout3.addWidget(QPushButton("*"), 1, 3)
        layout3.addWidget(QPushButton("square"), 1, 4)
        layout3.addWidget(QPushButton("1"), 2, 0)
        layout3.addWidget(QPushButton("2"), 2, 1)
        layout3.addWidget(QPushButton("3"), 2, 2)
        layout3.addWidget(QPushButton("-"), 2, 3)
        layout3.addWidget(QPushButton("C"), 2, 4)
        layout3.addWidget(QPushButton("0"), 3, 0)
        layout3.addWidget(QPushButton("."), 3, 1)
        layout3.addWidget(QPushButton("%"), 3, 2)
        layout3.addWidget(QPushButton("+"), 3, 3)
        layout3.addWidget(QPushButton("="), 3, 4)

        self.display1= QLineEdit(f"123345")
        self.display1.setFixedHeight(35)
        self.display1.setReadOnly(True)

        layout2.addWidget(self.display1)
        layout2.addWidget(QLineEdit("Hello World!"))
        layout2.addWidget(QLineEdit("Hello World!"))
        layout2.addWidget(QLineEdit("Hello World!"))

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()