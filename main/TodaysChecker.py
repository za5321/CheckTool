from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QAbstractButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class TodaysChecker(QDialog):
    def __init__(self, parent=None):
        from PyQt5 import uic

        super(TodaysChecker, self).__init__(parent)

        self.ui = uic.loadUi("ui\TodaysChecker.ui")
        self.set_ui()
        self.ui.show()
        self.ui.buttonBox.accepted.connect(self.accepted)

    def set_ui(self):
        self.ui.setWindowTitle(self.get_config("window_title"))
        self.ui.setWindowIcon(QtGui.QIcon(self.get_config("icon")))
        font_db = QtGui.QFontDatabase()
        font_db.addApplicationFont('font\\NanumGothic.ttf')

        self.ui.textBrowser.setFont(QtGui.QFont('NanumGothic', 11))
        self.ui.lineEdit1.setFont(QtGui.QFont('NanumGothic', 10))

        self.ui.textBrowser.setText("당직자")
        self.ui.textBrowser.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.ui.lineEdit1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    @staticmethod
    def get_config(flag: str):
        from conf.config import Config
        return Config().conf_todays_checker(flag)

    def accepted(self):
        checker: str = self.ui.lineEdit1.text()
        if not checker:
            from ui.CommonUI import MessageBoxWarning
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()
            TodaysChecker(self)
        else:
            from main.MainForm import MainForm
            MainForm(self)
