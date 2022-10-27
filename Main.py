from main.TodaysChecker import TodaysChecker
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QFontDatabase


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font_db = QFontDatabase()
    font_db.addApplicationFont('font\\NanumGothic.ttf')
    app.setFont(QFont('NanumGothic', 10))

    w = TodaysChecker()
    sys.exit(app.exec())
