from PyQt5.QtWidgets import QDialog
from ui.CommonUI import Layout, Label, Lineedit
import pymssql


class InsertSvr(QDialog):
    def __init__(self, parent):
        from ui import InsertSvrUI
        super(InsertSvr, self).__init__(parent)
        self.parent = parent
        self.disk_cnt = self.svc_cnt = self.task_cnt = 0
        self.disk_var, self.svc_var, self.task_var = [], [], []

        self.ui = InsertSvrUI.ui(self)
        self.show()

    def click_wdef_radio(self):
        return "1" if self.wdef_yes_radio.isChecked() else "0" if self.wdef_no_radio.isChecked() else "2"

    def click_disk_pushbtn(self):
        self.disk_cnt += 1
        self.disk_var.append(f"diskle{self.disk_cnt}")
        label = Label("디스크")
        label.setContentsMargins(0, 0, 42, 0)
        self.disk_var[self.disk_cnt - 1] = Lineedit()
        self.disk_var[self.disk_cnt - 1].setFixedWidth(170)
        self.disk_var[self.disk_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.disk_var[self.disk_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + 3, layout)

    def click_svc_pushbtn(self):
        self.svc_cnt += 1
        self.svc_var.append(f"svcle{self.svc_cnt}")
        label = Label("서비스")
        label.setContentsMargins(0, 0, 42, 0)
        self.svc_var[self.svc_cnt - 1] = Lineedit()
        self.svc_var[self.svc_cnt - 1].setFixedWidth(170)
        self.svc_var[self.svc_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.svc_var[self.svc_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + self.svc_cnt + 4, layout)

    def click_task_pushbtn(self):
        self.task_cnt += 1
        self.task_var.append(f"taskle{self.task_cnt}")
        label = Label("작업스케줄러")
        label.setContentsMargins(0, 0, 6, 0)
        self.task_var[self.task_cnt - 1] = Lineedit()
        self.task_var[self.task_cnt - 1].setFixedWidth(170)
        self.task_var[self.task_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.task_var[self.task_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + self.svc_cnt + self.task_cnt + 5, layout)

    def accepted(self):
        from ui.CommonUI import MessageBoxWarning, MessageBoxInfo

        def insert_server():
            from func.InsertSvr import InsertSvr

            insert = InsertSvr(host, ip)
            id = insert.insert_svr(int(wdef), int(sys_code), int(gb_code))
            if id != -1:
                if insert.insert_svr_info('DISK', disk) \
                        and insert.insert_svr_info('SERVICE', svc) \
                        and insert.insert_svr_info('TASK', task):
                    return True
                else:
                    from . import DeleteSvr
                    DeleteSvr.delete_func(id)
                    return False
            else:
                return False

        ip = self.ih_ip_le.text()
        host = self.ih_host_le.text()
        disk = [self.disk_le.text().upper()]
        svc = [self.sys_le.text()] if self.sys_le.text() else []
        task = [self.task_le.text()] if self.task_le.text() else []
        wdef = self.click_wdef_radio()

        sys_code = self.sys_list[self.code_sys_combo.currentIndex()][0]
        gb_code = self.gb_list[self.code_gb_combo.currentIndex()][0]

        if not ip or not host:
            self.msgbox = MessageBoxWarning("IP와 호스트명은 필수 입력항목입니다.")
            self.msgbox.show()

        elif not disk:
            self.msgbox = MessageBoxWarning("디스크는 필수 입력항목입니다.")
            self.msgbox.show()

        elif wdef == "2":
            self.msgbox = MessageBoxWarning("윈도우 디펜더는 필수 입력항목입니다.")
            self.msgbox.show()

        else:
            if self.disk_var:
                for i in self.disk_var:
                    disk.append(i.text().upper())
            if self.svc_var:
                for i in self.svc_var:
                    svc.append(i.text())
            if self.task_var:
                for i in self.task_var:
                    task.append(i.text())

        if insert_server():
            self.msgbox = MessageBoxInfo("서버 정보를 등록했습니다.")
            self.msgbox.show()
            self.close()
        else:
            self.msgbox = MessageBoxWarning("서버 정보 등록에 실패했습니다.")
            self.msgbox.show()

    def rejected(self):
        self.close()
