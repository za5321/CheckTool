from PyQt5.QtWidgets import QDialog
from ui import DeleteSvrUI
from func.GetSvrInfo import GetSvrInfo


def delete(hostname: str, svrid: int) -> bool:
    from ui.CommonUI import MessageBoxWarning
    from PyQt5.QtWidgets import QMessageBox

    msgbox = MessageBoxWarning(hostname + " 서버의 기록이 모두 삭제됩니다.")
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    btn = msgbox.exec_()

    if btn == QMessageBox.Ok:
        delete_func(svrid)
        return True
    elif btn == QMessageBox.Cancel:
        msgbox.close()
        return False


def delete_func(svrid):
    from conf.config import Config
    con = Config().conf_db_connection()

    try:
        cursor = con.cursor()
        sql = f"EXEC CT_DELETE_SERVER {str(svrid)}"
        cursor.execute(sql)
        con.commit()
    except:
        return False
    return True


class DeleteSvr_New(QDialog):
    def __init__(self, parent):
        super(DeleteSvr_New, self).__init__(parent)
        self.parent = parent
        self.svr_list = GetSvrInfo.get_svr_list()

        self.ui = DeleteSvrUI.ui(self)
        self.show()

    def click_delete_btn(self):
        from ui.CommonUI import MessageBoxWarning, MessageBoxInfo

        hostname = self.linedit.text()
        svrid = self.get_svrid(hostname)

        if svrid == -1:
            msgbox = MessageBoxWarning("존재하지 않는 호스트명입니다.")
            msgbox.exec()
        else:
            if delete(hostname, svrid):
                #import datetime
                msgbox = MessageBoxInfo("서버 정보를 삭제했습니다.")
                msgbox.exec()
                self.close()
                #self.parent.set_tableWgt1(datetime.datetime.today().date())

    def get_svrid(self, hostname: str) -> int:
        if hostname not in self.svr_list.values():
            return -1
        return next(key for key, val in self.svr_list.items() if val == hostname)


# class DeleteSvr:
#     def __init__(self):
#         from func.GetSvrInfo import GetSvrInfo
#         self.svr_id, self.hostname = GetSvrInfo.get_svr_list()
#
#     def delete(self, row):
#         from ui.CommonUI import MessageBoxWarning
#         from PyQt5.QtWidgets import QMessageBox
#
#         msgbox = MessageBoxWarning(self.hostname[row] + " 서버의 기록이 모두 삭제됩니다.")
#         msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         btn = msgbox.exec_()
#
#         if btn == QMessageBox.Ok:
#             from conf.config import Config
#             from main.MainForm import MainForm
#             import datetime
#             con = Config().conf_db_connection()
#             cursor = con.cursor()
#             sql = "EXEC CT_DELETE_SERVER_LIST " + str(self.svr_id[row])
#             cursor.execute(sql)
#             con.commit()
#
#             MainForm().set_tableWgt1(datetime.datetime.today().date())
#         elif btn == QMessageBox.Cancel:
#             msgbox.close()
