from typing import Tuple
from func.GetSvrInfo import GetSvrInfo
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
import datetime

black, red, blue = QColor(0, 0, 0), QColor(238, 0, 0), QColor(8, 96, 168)


class SetMainForm:
    def __init__(self, id: int, date: datetime):
        self.id = id
        self.date = date

    def set_res(self) -> list:
        items = []
        cpu, mem = GetSvrInfo.get_res(self.id, self.date)
        if cpu and mem:
            items.append(QTableWidgetItem(cpu[0]))
            items.append(QTableWidgetItem(mem[0]))
        for item in items:
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

            if item.text() and float(item.text()) > 85:
                item.setForeground(QBrush(red))
        return items

    def set_res_rate(self) -> QTableWidgetItem:
        today_cpu, today_mem = GetSvrInfo.get_res(self.id, self.date)
        yesterday_cpu, yesterday_mem = GetSvrInfo.get_res(self.id, (self.date - datetime.timedelta(days=1)))

        if today_mem and yesterday_mem:
            rate = round(float(yesterday_mem[0]) - float(today_mem[0]), 2)
            color = blue if rate > 0 \
                else red if rate < 0 \
                else black
            item = QTableWidgetItem(f"-{abs(rate)}") if rate > 0 \
                else QTableWidgetItem(f"+{abs(rate)}") if rate < 0 \
                else QTableWidgetItem(str(rate))
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            item.setForeground(QBrush(color))
            return item

    def set_disk(self) -> Tuple[list, list]:
        letter_items: list = []
        capacity_items: list = []

        disk = GetSvrInfo.get_disk(self.id, self.date)
        if disk:
            for i, letter in enumerate(disk):
                letter_items.append(QTableWidgetItem(letter.upper()))
                capacity_items.append(QTableWidgetItem(disk[letter]))

        for i in range(len(letter_items)):
            letter_items[i].setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            capacity_items[i].setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            if int(capacity_items[i].text().replace("%", '')) > 85:
                capacity_items[i].setForeground(QBrush(red))
        return letter_items, capacity_items

    def set_disk_rate(self) -> list:
        today = GetSvrInfo.get_disk(self.id, self.date)
        yesterday = GetSvrInfo.get_disk(self.id, (self.date - datetime.timedelta(days=1)))
        rate = {}
        items = []
        if today and yesterday:
            for i, letter in enumerate(today):
                rate[letter] = int(yesterday[letter].replace("%", '')) - int(today[letter].replace("%", ''))
            for i, letter in enumerate(rate):
                val = rate[letter]
                item = QTableWidgetItem(f"+{abs(val)}") if val < 0 \
                    else QTableWidgetItem(f"-{abs(val)}") if val > 0 \
                    else QTableWidgetItem(str(val))
                color = blue if val > 0 \
                    else red if val < 0 \
                    else black
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                item.setForeground(QBrush(color))
                items.append(item)
        return items

    def set_svc(self) -> QTableWidgetItem:
        svc = GetSvrInfo.get_service(self.id, self.date)
        svc_cnt = 0
        if svc:
            for j in svc:
                svc_cnt = (svc_cnt + 1) if j[1] == "1" else -1 if j[1] == "-1" else 0
            svc_status = "??????" if svc_cnt == len(svc) else "??????" if svc_cnt == 0 else "-" if svc_cnt == -1 else ""
            item = QTableWidgetItem(svc_status)
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            if svc_status == "??????":
                item.setForeground(QBrush(red))
            return item

    def set_task(self) -> QTableWidgetItem:
        task = GetSvrInfo.get_task(self.id, self.date)
        task_cnt = 0
        if task:
            for j in task:
                task_cnt = (task_cnt + 1) if j[1] == "1" else -1 if j[1] == "-1" else 0
            task_status = "??????" if len(task) == task_cnt \
                else "??????" if task_cnt == 0 \
                else "-" if task_cnt == -1 \
                else ""
            item = QTableWidgetItem(task_status)
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            if task_status == "??????":
                item.setForeground(QBrush(red))
            return item

    def set_wdef(self) -> QTableWidgetItem:
        wdef = GetSvrInfo.get_windefender(self.id, self.date)
        if wdef:
            wdef_status = wdef[0] if wdef[0] != "-1" else "-"
            item = QTableWidgetItem(wdef_status)
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            if wdef_status == "??????":
                item.setForeground(QBrush(red))
            return item

    def set_evt(self) -> QTableWidgetItem:
        evt = GetSvrInfo.get_event(self.id, self.date)
        evt_str = ""
        if not evt:
            evt_str = "??????"
        elif evt == ["NO EVENT"]:
            evt_str = ""
        else:
            evt_str += "?????????ID: "
            for j in range(len(evt)):
                evt_list = str(evt[j]).replace("(", "").replace(")", "").replace("'", "").split(",")
                # evt_str += "\n" if evt_str != "" else ""
                # evt_str += "??????: " + str(evt_list[0])
                # evt_str += ", ??????: ??????" if evt_list[1].replace(" ", "") == '1' \
                #    else ", ??????: ??????" if evt_list[1].replace(" ", "") == '2' \
                #    else ", ??????: ??????" if evt_list[1].replace(" ", "") == '3' \
                #    else ""
                # evt_str += ", ?????????ID:" + str(evt_list[2])
                # evt_str += ", ????????????:" + str(evt_list[3])
                evt_str += (", " if evt_str != "?????????ID: " else "")
                evt_str += str(evt_list[0])
        return QTableWidgetItem(evt_str)
