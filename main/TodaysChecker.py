from PyQt5.QtWidgets import QDialog


class TodaysChecker(QDialog):
    def __init__(self, parent=None):
        from PyQt5 import uic
        from PyQt5.QtGui import QIcon

        super(TodaysChecker, self).__init__(parent)

        self.ui = uic.loadUi("ui\TodaysChecker.ui")
        self.ui.setWindowTitle(self.get_config("window_title"))
        self.ui.setWindowIcon(QIcon(self.get_config("icon")))
        self.ui.show()

        self.ui.buttonBox.accepted.connect(self.accepted)

    @staticmethod
    def get_config(flag: str):
        from conf.config import Config
        return Config().conf_todays_checker(flag)

    def accepted(self):
        checker: str = self.ui.lineEdit1.text()
        if not checker:
            from ui.CommonUI import MessageBoxWarning
            msgbox = MessageBoxWarning("Warning", "내용을 입력해주세요.")
            msgbox.exec()
            TodaysChecker(self)
        else:
            from main.MainForm import MainForm
            MainForm(self)
