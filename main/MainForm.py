# import collections

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
import datetime


class MainForm(QMainWindow):
    def __init__(self, parent):
        from PyQt5.QtCore import QDate
        from PyQt5.QtGui import QIcon
        from PyQt5.QtWidgets import QHeaderView, QFrame
        from PyQt5 import uic

        QMainWindow.__init__(self, parent)
        self.svr_rowspan: dict = {}
        self.svr_current_row: dict = {}

        self.ui = uic.loadUi("ui\MainForm.ui")
        self.ui.tableWgt1.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.tableWgt1.horizontalHeader().setFixedHeight(40)
        self.ui.tableWgt1.horizontalHeader().setStyleSheet("QHeaderView::section {"
                                                           "background: rgb(240,255,255); "
                                                           "border: 1px solid rgb(203, 235, 255);"
                                                           "font-weight: 600;"
                                                           "color: rgb(95, 95, 95);}")

        self.ui.setWindowTitle(self.get_config("window_title"))
        self.ui.setWindowIcon(QIcon(self.get_config("icon")))
        self.ui.dateEdit1.setDate(QDate.currentDate())
        self.ui.show()

        self.ui.toolBtn1.clicked.connect(self.click_toolBtn1)
        self.ui.toolBtn2.clicked.connect(self.click_toolBtn2)
        self.ui.toolBtn3.clicked.connect(self.click_toolBtn3)
        self.ui.toolBtn4.clicked.connect(self.click_toolBtn4)
        self.ui.toolBtn5.clicked.connect(self.click_toolBtn5)
        self.ui.toolBtn6.clicked.connect(self.click_toolBtn6)
        self.ui.tableWgt1.clicked.connect(self.click_tableWgt1)
        self.ui.tableWgt1.installEventFilter(self)

        #resized = QtCore.pyqtSignal()
        #resized.connect(self.resize_check)

    @staticmethod
    def get_config(flag: str):
        from conf.config import Config
        return Config().conf_main_form(flag)

    def set_tableWgt1(self, date: datetime):
        """tableWgt1: Main table widget to present the result of the date"""
        from func.GetSvrInfo import GetSvrInfo
        from main.btn.SetMainForm import SetMainForm
        from PyQt5.QtWidgets import QTableWidgetItem

        self.ui.tableWgt1.clearContents()

        svr_list: dict = GetSvrInfo.get_svr_list()
        self.ui.tableWgt1.setRowCount(GetSvrInfo.get_row_count("total"))

        current_row = 0

        for i, id in enumerate(svr_list):
            s = SetMainForm(id, date)
            rowspan = GetSvrInfo.get_row_count(str(id))
            self.svr_rowspan[id] = rowspan
            self.svr_current_row[id] = current_row

            host_item = QTableWidgetItem(svr_list[id])
            self.ui.tableWgt1.setItem(current_row, 0, host_item)

            res_items = s.set_res()
            if res_items:
                self.ui.tableWgt1.setItem(current_row, 1, res_items[0])
                self.ui.tableWgt1.setItem(current_row, 2, res_items[1])

            res_rate_item = s.set_res_rate()
            if res_rate_item:
                self.ui.tableWgt1.setItem(current_row, 3, res_rate_item)

            letter_items, capacity_items = s.set_disk()
            disk_rate_items = s.set_disk_rate()
            for j in range(len(letter_items)):
                self.ui.tableWgt1.setItem(current_row + j, 4, letter_items[j])
                self.ui.tableWgt1.setItem(current_row + j, 5, capacity_items[j])
                if disk_rate_items:
                    self.ui.tableWgt1.setItem(current_row + j, 6, disk_rate_items[j])

            svc_item = s.set_svc()
            self.ui.tableWgt1.setItem(current_row, 7, svc_item)

            task_item = s.set_task()
            self.ui.tableWgt1.setItem(current_row, 8, task_item)

            wdef_item = s.set_wdef()
            self.ui.tableWgt1.setItem(current_row, 9, wdef_item)

            evt_item = s.set_evt()
            self.ui.tableWgt1.setItem(current_row, 10, evt_item)

            for col in range(self.ui.tableWgt1.columnCount()):
                if col not in self.get_config("use_separated_row"):
                    self.ui.tableWgt1.setSpan(current_row, col, rowspan, 1)
            current_row += rowspan

        self.ui.tableWgt1.resizeRowsToContents()
        # self.ui.tableWgt1.resizeColumnsToContents()

    def click_toolBtn1(self):
        """Refresh tableWgt1 (date: today)"""
        today = datetime.datetime.today().date()
        self.set_tableWgt1(today)

    def click_toolBtn2(self):
        """Insert a new server"""
        from main.btn.InsertSvr import InsertSvr
        InsertSvr(self)

    def click_tableWgt1(self) -> int:
        return self.ui.tableWgt1.currentRow()

    def click_toolBtn3(self):
        """Delete the server"""
        from main.btn.DeleteSvr import DeleteSvr_New
        # DeleteSvr().delete(self.click_tableWgt1())
        DeleteSvr_New(self)

    def click_toolBtn4(self):
        """Refresh tableWgt1 (date: selected date)"""
        date = datetime.datetime.strptime(self.ui.dateEdit1.date().toString('yyyy-MM-dd'), '%Y-%m-%d').date()
        self.set_tableWgt1(date)

    def click_toolBtn5(self):
        """To manage syscode, gbcode"""
        from main.btn.ManageCode import ManageCode
        ManageCode(self)

    def click_toolBtn6(self):
        """Download Excel file"""
        self.qtablewidget_to_excel()

    def get_svrid(self, current_row: int) -> int:
        try:
            return next(key for key, value in self.svr_current_row.items() if value == current_row)
        except StopIteration:
            val = 0
            for value in self.svr_current_row.values():
                if value < current_row:
                    val = max(val, value)
            return next(key for key, value in self.svr_current_row.items() if value == val)

    '''def resizeEvent(self, event):
        self.resized.emit()
        return super(MainForm, self).resizeEvent(event)

    def resize_check(self):
        self.ui.width = self.ui.centralWidget.frameSize().width() - self.ui.verticalLayout.maximumSize().width()'''

    def eventFilter(self, source, event):
        """To copy and paste selected items in tableWgt1"""
        from PyQt5.QtCore import QEvent
        from PyQt5.QtGui import QKeySequence

        if source == self.ui.tableWgt1 and event.type() == QEvent.KeyPress and event == QKeySequence.Copy and not event.isAutoRepeat():
            # copy_string = ""
            # for i in self.ui.tableWgt1.selectedIndexes():
            #     copy_string += "\n" if i.column() == 0 and copy_string else ""
            #     copy_string += i.data() if i.data() else ""
            #     copy_string += "\t"

            datadict = {}
            for i, id in enumerate(self.svr_rowspan):
                datadict[id] = {}
                for j in range(self.svr_rowspan[id]):
                    datadict[id][j] = []

            for i in self.ui.tableWgt1.selectedIndexes():
                id = self.get_svrid(i.row())
                datadict[id][i.row()-self.svr_current_row[id]].append(i.data() if i.data() else "")

            copy_string = self.datadict_to_html(datadict)

            from PyQt5.QtWidgets import QApplication
            QApplication.clipboard().setText(copy_string)
            return True
        return super(QMainWindow, self).eventFilter(source, event)

    def datadict_to_html(self, datadict: dict) -> str:
        copy_string: str = self.get_config("copy_string")
        copy_html: list = ["<html>\n", "\t<table>\n", copy_string]
        for key, value in datadict.items():
            rowspan = self.svr_rowspan[key]
            for k, v in value.items():
                copy_html.append("\t\t<tr>\n")
                for i, val in enumerate(v):
                    copy_html.append(f"\t\t\t<td rowspan={rowspan}>" if i not in self.get_config("use_separated_row") and k == 0 else "\t\t\t<td>")
                    copy_html.append(val)
                    copy_html.append("</td>\n")
                copy_html.append("\t\t</tr>\n")
        copy_html.append("\t</table>\n")
        copy_html.append("</html>\n")
        return "".join(copy_html)

    def qtablewidget_to_excel(self):
        import openpyxl
        from openpyxl import styles
        from datetime import date

        def merge(row: str, col: str, text: str, *color: str):
            ws[row] = text
            ws.merge_cells(f"{row}:{col}")

        days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        today = str(date.today()) + " " + days[date.today().weekday()]

        if self.get_config("license") == "JAEMU":
            if date.today().day == 16:
                wb = openpyxl.Workbook()
                ws = wb.active

                merge('A1', 'H6', today+"\n"+self.get_config("window_title"))
                merge('I1', 'I2', '담당자')
                merge('I3', 'I6', '')
                merge('J1', 'J2', '파트장')
                merge('J3', 'J6', '')
                merge('A7', 'J7', '')
                merge('A8', 'J8', '장애 및 특이사항 없음')
                merge('A9', 'J9', '총용량 입력 X, 남은 용량만 입력, 사용량 85% 이상이면 노란색으로 자동 표시됨, 해당 란에 서버 명 표시')

                merge('A10', 'E10', '1. SAP 점검')
                merge('A11', 'D11', '1-1. SMLG(CCMS)')
                merge('A12', 'D12', '1-2. SM66(System Work Process Overview)')
                merge('A13', 'D13', '1-3. SM12(Select lock entry)')
                merge('A14', 'D14', '1-4. SM37(Job scheduling)')
                merge('A15', 'D15', '1-5. SM21(System Log)')
                merge('A16', 'D16', '1-6. DB02(DB Performance)')
                merge('A17', 'D17', '1-7. DB13(Database Log)')
                merge('A18', 'D18', '1-8. ST22(ABAP runtime errors)')
                merge('A19', 'D19', '1-9. AL11(Firm banking Log)')
                merge('A20', 'D20', '1-10. SU01(User Maintenance)')
                for i in range(11, 20):
                    ws[f'E{i}'] = "정상"
                ws['E20'] = ""

                wb.save('D:\\test.xlsx')

            else:
                wb = openpyxl.load_workbook('D:\\202210_전산재무담당_모니터링.xlsx')
                ws = wb.create_sheet(f'{date.today()}')
                wb.save('D:\\202210_전산재무담당_모니터링.xlsx')
            print("finished")
