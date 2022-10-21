from PyQt5.QtWidgets import QDialog
from conf.config import Config
con = Config().conf_db_connection()


class ManageCode(QDialog):
    def __init__(self, parent):
        from PyQt5 import uic
        from PyQt5.QtGui import QIcon

        super(ManageCode, self).__init__(parent)
        self.ui = uic.loadUi("ui\ManageCode.ui")
        self.ui.setWindowTitle(self.get_config("window_title"))
        self.ui.setWindowIcon(QIcon(self.get_config("icon")))

        for i, j in enumerate(self.get_config("tab_text")):
            self.ui.tabWidget.setTabText(i, j)
        self.ui.show()

        self.sys_list, self.gb_list = [], []
        self.set_tab()

        self.ui.sys_listWgt.itemClicked.connect(self.click_sys_listWgt)
        self.ui.gb_listWgt.itemClicked.connect(self.click_gb_listWgt)
        self.ui.sys_ins_btn.clicked.connect(self.click_sys_ins_btn)
        self.ui.sys_upd_btn.clicked.connect(self.click_sys_upd_btn)
        self.ui.sys_del_btn.clicked.connect(self.click_sys_del_btn)
        self.ui.gb_ins_btn.clicked.connect(self.click_gb_ins_btn)
        self.ui.gb_upd_btn.clicked.connect(self.click_gb_upd_btn)
        self.ui.gb_del_btn.clicked.connect(self.click_gb_del_btn)

    @staticmethod
    def get_config(flag: str):
        return Config().conf_manage_code(flag)

    def set_tab(self):
        from func import GetSYSGB

        self.ui.sys_listWgt.clear()
        self.ui.gb_listWgt.clear()

        self.sys_list = GetSYSGB.GetSYSGB.get_syslist()
        self.gb_list = GetSYSGB.GetSYSGB.get_gblist()

        for i, j in enumerate(self.sys_list):
            self.ui.sys_listWgt.addItem(j[1])
        for i, j in enumerate(self.gb_list):
            self.ui.gb_listWgt.addItem(j[1])

    def click_sys_listWgt(self):
        index = self.ui.sys_listWgt.currentRow()
        self.ui.sys_code_le.setText(str(self.sys_list[index][0]))
        self.ui.sys_name_le.setText(self.sys_list[index][1])

    def click_gb_listWgt(self):
        index = self.ui.gb_listWgt.currentRow()
        self.ui.gb_code_le.setText(str(self.gb_list[index][0]))
        self.ui.gb_name_le.setText(self.gb_list[index][1])

    def click_sys_ins_btn(self):
        from ui.CommonUI import MessageBoxWarning
        code = self.ui.sys_code_le.text()
        name = self.ui.sys_name_le.text()

        if name and name:
            import pymssql
            try:
                cursor = con.cursor()
                sql = f"EXEC CT_INSERT_CODE 'sys', {code}, '{name}'"
                cursor.execute(sql)
                con.commit()

                self.set_tab()
                self.ui.sys_code_le.clear()
                self.ui.sys_name_le.clear()
            except pymssql.IntegrityError:
                msgbox = MessageBoxWarning("이미 존재하는 코드입니다.")
                msgbox.exec()
        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()

    def click_sys_upd_btn(self):
        from ui.CommonUI import MessageBoxWarning

        code = self.ui.sys_code_le.text()
        name = self.ui.sys_name_le.text()

        if code and name:
            cursor = con.cursor()
            sql = f"EXEC CT_UPDATE_CODE 'sys', {code}, '{name}'"
            cursor.execute(sql)
            con.commit()

            self.set_tab()
            self.ui.sys_code_le.clear()
            self.ui.sys_name_le.clear()
        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()

    def click_sys_del_btn(self):
        from ui.CommonUI import MessageBoxWarning

        code = self.ui.sys_code_le.text()

        if code:
            cursor = con.cursor()
            sql = "EXEC CT_DELETE_CODE 'sys', " + code
            cursor.execute(sql)
            con.commit()

            self.set_tab()
            self.ui.sys_code_le.clear()
            self.ui.sys_name_le.clear()
        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()

    def click_gb_ins_btn(self):
        from ui.CommonUI import MessageBoxWarning
        code = self.ui.gb_code_le.text()
        name = self.ui.gb_name_le.text()

        if code and name:
            import pymssql
            try:
                cursor = con.cursor()
                sql = f"EXEC CT_INSERT_CODE 'gb', {code}, '{name}'"
                cursor.execute(sql)
                con.commit()

                self.set_tab()
                self.ui.gb_code_le.clear()
                self.ui.gb_name_le.clear()

            except pymssql.IntegrityError:
                msgbox = MessageBoxWarning("이미 존재하는 코드입니다.")
                msgbox.exec()
        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()

    def click_gb_upd_btn(self):
        from ui.CommonUI import MessageBoxWarning

        code = self.ui.gb_code_le.text()
        name = self.ui.gb_name_le.text()

        if code and name:
            cursor = con.cursor()
            sql = f"EXEC CT_UPDATE_CODE 'gb', {code}, '{name}'"
            cursor.execute(sql)
            con.commit()

            self.set_tab()
            self.ui.gb_code_le.clear()
            self.ui.gb_name_le.clear()

        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()

    def click_gb_del_btn(self):
        from ui.CommonUI import MessageBoxWarning

        code = self.ui.gb_code_le.text()

        if code:
            cursor = con.cursor()
            sql = "EXEC CT_DELETE_CODE 'gb', " + code
            cursor.execute(sql)
            con.commit()

            self.set_tab()
            self.ui.gb_code_le.clear()
            self.ui.gb_name_le.clear()
        else:
            msgbox = MessageBoxWarning("내용을 입력해주세요.")
            msgbox.exec()