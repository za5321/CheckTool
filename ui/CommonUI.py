from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class Lineedit(QtWidgets.QLineEdit):
    def __init__(self, width: int):
        super().__init__()
        self.setFixedWidth(width) if width else None
        self.setStyleSheet("QLineEdit {border: 2px solid rgb(203, 235, 255);background: rgb(250, 255, 255);}")


class Combobox(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QComboBox {background: rgb(203,235,255);} QListView {background:white; border: 2px solid rgb(203, 235, 255);}")


class Layout(QtWidgets.QGridLayout):
    def __init__(self):
        super().__init__()


class Label(QtWidgets.QLabel):
    def __init__(self, text: str, width: int):
        super().__init__()
        self.setFixedWidth(width) if width else None
        self.setText(text)


class PushButton(QtWidgets.QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)


class ToolButton(QtWidgets.QToolButton):
    def __init__(self, text, color):
        super().__init__()
        self.setText(text)
        if color == "blue":
            self.setStyleSheet("QToolButton {border: 2px solid rgb(203, 235, 255);background: rgb(203, 235, 255);}")
        elif color == "red":
            self.setStyleSheet("QToolButton {border: 2px solid rgb(255, 155, 130);background: rgb(255, 155, 130);}")


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
