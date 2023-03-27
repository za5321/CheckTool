import datetime
from conf.config import Config

con = Config().conf_db_connection()


class GetSvrInfo:
    @staticmethod
    def get_row_count(flag: str, date: datetime) -> int:
        cursor = con.cursor()
        sql = f"EXEC CT_SELECT_ROW_COUNT '{flag}', '{str(date)}'"
        cursor.execute(sql)
        row = cursor.fetchall()
        return row[0][0]

    @staticmethod
    def get_svr_list() -> dict:
        svr_dict = {}

        cursor = con.cursor()
        sql = "EXEC CT_SELECT_SERVER"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            svr_dict[row[0]] = row[1]
            row = cursor.fetchone()
        return svr_dict

    @staticmethod
    def get_res(svr_id: int, date: datetime):
        cpu, mem = [], []
        cursor = con.cursor()
        sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'res', '{str(date)}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            cpu.append(row[0].strip())
            mem.append(row[1].strip())
            row = cursor.fetchone()
        return cpu, mem

    @staticmethod
    def get_disk(svr_id: int, date: datetime) -> dict:
        disk_capacity: dict = {}

        cursor = con.cursor()
        sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'disk', '{str(date)}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            disk_capacity[row[0]] = row[1]
            row = cursor.fetchone()
        return disk_capacity

    @staticmethod
    def get_service(svr_id: int, date: datetime) -> list:
        service = []

        def is_service(id: int) -> str:
            cursor = con.cursor()
            sql = f"EXEC DC_SELECT_SERVER_INFO {str(id)}, 'svc'"
            cursor.execute(sql)
            row = cursor.fetchall()
            return row[0][0].strip() if row else None

        if not is_service(svr_id):
            service.append(("NONE", "-1"))
        else:
            cursor = con.cursor()
            sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'svc', '{str(date)}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                service.append((row[0], row[1]))
                row = cursor.fetchone()
        return service

    @staticmethod
    def get_event(svr_id: int, date: datetime) -> list:
        event = []

        cursor = con.cursor()
        sql = f"EXEC CT_SELECT_EVT_CNT {str(svr_id)}, '{str(date)}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        flag = 0
        while row:
            flag = row[0]
            row = cursor.fetchone()

        if flag > 0:
            sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'evt', '{str(date)}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                event.append(row[0])
                row = cursor.fetchone()
        else:
            event = ["NO EVENT"]
        return event

    @staticmethod
    def get_task(svr_id: int, date: datetime) -> list:
        task = []

        def is_task(id: int) -> str:
            cursor = con.cursor()
            sql = f"EXEC DC_SELECT_SERVER_INFO {str(id)}, 'task'"
            cursor.execute(sql)
            row = cursor.fetchall()
            return row[0][0] if row else None

        if not is_task(svr_id):
            task.append(("NONE", "-1"))
        else:
            cursor = con.cursor()
            sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'task', '{str(date)}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                task.append((row[0], row[1]))
                row = cursor.fetchone()
        return task

    @staticmethod
    def get_windefender(svr_id: int, date: datetime) -> list:
        def is_wdef(id: int) -> str:
            cursor = con.cursor()
            sql = f"EXEC DC_SELECT_SERVER_INFO {str(id)}, 'wdef'"
            cursor.execute(sql)
            row = cursor.fetchall()
            return row[0][0]

        if is_wdef(svr_id) == 0:
            return ["-1"]
        else:
            cursor = con.cursor()
            sql = f"EXEC CT_SELECT_CHECK_RESULT {str(svr_id)}, 'wdef', '{str(date)}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            return list(row) if row else None
