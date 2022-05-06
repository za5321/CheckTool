from PyQt5.QtWidgets import QDialog


class InsertSvr(QDialog):
    def __init__(self, parent):
        from ui import InsertSvrUI
        super(InsertSvr, self).__init__(parent)
        self.parent = parent
        self.disk_cnt = self.svc_cnt = self.task_cnt = 0
        self.disk_var = self.svc_var = self.task_var = []

        self.ui = InsertSvrUI.ui(self)
        self.show()

    def click_wdef_radio(self):
        return "1" if self.wdef_yes_radio.isChecked() else "0" if self.wdef_no_radio.isChecked() else "2"

    def click_disk_pushbtn(self):
        from ui.CommonUI import Layout, Label, Lineedit

        self.disk_cnt += 1
        self.disk_var.append(f"diskle{self.disk_cnt}")
        label = Label("디스크")
        label.setContentsMargins(0, 0, 42, 0)
        self.disk_var[self.disk_cnt - 1] = Lineedit()
        self.disk_var[self.disk_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.disk_var[self.disk_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + 2, layout)

    def click_svc_pushbtn(self):
        from ui.CommonUI import Layout, Label, Lineedit

        self.svc_cnt += 1
        self.svc_var.append(f"svcle{self.svc_cnt}")
        label = Label("서비스")
        label.setContentsMargins(0, 0, 42, 0)
        self.svc_var[self.svc_cnt - 1] = Lineedit()
        self.svc_var[self.svc_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.svc_var[self.svc_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + self.svc_cnt + 3, layout)

    def click_task_pushbtn(self):
        from ui.CommonUI import Layout, Label, Lineedit

        self.task_cnt += 1
        self.task_var.append(f"taskle{self.task_cnt}")
        label = Label("작업스케줄러")
        label.setContentsMargins(0, 0, 6, 0)
        self.task_var[self.task_cnt - 1] = Lineedit()
        self.task_var[self.task_cnt - 1].setContentsMargins(0, 0, 175, 0)
        layout = Layout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.task_var[self.task_cnt - 1], 0, 1)
        self.main_layout.insertLayout(self.disk_cnt + self.svc_cnt + self.task_cnt + 4, layout)

    def accepted(self):
        from ui.CommonUI import MessageBoxWarning
        ip = self.ih_ip_le.text()
        host = self.ih_host_le.text()
        disk = self.disk_le.text().upper()
        svc = self.sys_le.text() + " "
        task = self.task_le.text() + " "
        wdef = self.click_wdef_radio()

        sys_code = self.sys_list[self.code_sys_combo.currentIndex()][0]
        gb_code = self.gb_list[self.code_gb_combo.currentIndex()][0]

        if not ip or not host:
            self.ih_msgbox = MessageBoxWarning("Warning", "IP와 호스트명은 필수 입력항목입니다.")
            self.ih_msgbox.show()

        elif not disk:
            self.disk_msgbox = MessageBoxWarning("Warning", "디스크는 필수 입력항목입니다.")
            self.disk_msgbox.show()

        else:
            disk += ":\\ "
            disk += ":\\ ".join(i.text().upper() for i in self.disk_var)
            disk += ":\\"
            svc += " ".join(i.text() for i in self.svc_var)
            task += " ".join(i.text() for i in self.task_var)

            if wdef == "2":
                self.wdef_msgbox = MessageBoxWarning("Warning", "윈도우 디펜더는 필수 입력항목입니다.")
                self.wdef_msgbox.show()
            else:
                from conf.config import Config
                #import datetime
                import pymssql
                con = Config().conf_db_connection()
                cursor = con.cursor()

                sql = f"INSERT INTO SERVER_LIST VALUES('{host}', '{ip}', '{disk}', '{svc}', '{task}', '{wdef}', " \
                      f"'{str(sys_code)}', '{str(gb_code)}')"
                try:
                    cursor.execute(sql)
                    con.commit()
                    self.close()
                    #self.parent.set_tableWgt1(datetime.datetime.today().date())
                except pymssql.IntegrityError:
                    self.host_msgbox = MessageBoxWarning("Warning", "이미 등록된 호스트명입니다.")
                    self.host_msgbox.show()

    def rejected(self):
        self.close()
