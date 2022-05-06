from main.TodaysChecker import TodaysChecker
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TodaysChecker()
    sys.exit(app.exec())
