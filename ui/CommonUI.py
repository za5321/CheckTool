from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class Lineedit(QtWidgets.QLineEdit):
    def __init__(self):
        super().__init__()


class Layout(QtWidgets.QGridLayout):
    def __init__(self):
        super().__init__()


class Label(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)


class PushButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)


class MessageBoxWarning(QtWidgets.QMessageBox):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Warning")
        self.setText(text)
        self.setWindowIcon(QIcon('icons\Warning.png'))


class MessageBoxInfo(QtWidgets.QMessageBox):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Information")
        self.setText(text)
        self.setWindowIcon(QIcon('icons\Info.png'))
