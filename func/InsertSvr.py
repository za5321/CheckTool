from conf.config import Config
import pymssql

con = Config().conf_db_connection()


class InsertSvr():
    def __init__(self, host, ip):
        self.host = host
        self.ip = ip
        self.serverid = 0

    def insert_svr(self, wdef, sys_code, gb_code) -> int:
        try:
            cursor = con.cursor()
            sql = f"INSERT INTO SERVER VALUES('{self.host}', '{self.ip}', {wdef}, {sys_code}, {gb_code})"
            cursor.execute(sql)
            con.commit()
        except:
            return -1
        self.serverid = self.get_serverid()
        return self.serverid

    def get_serverid(self) -> int:
        cursor = con.cursor()
        sql = f"SELECT SERVERID FROM SERVER WHERE HOSTNAME = '{self.host}' AND IP = '{self.ip}'"
        cursor.execute(sql)
        row = cursor.fetchall()
        return row[0][0]

    def insert_svr_info(self, flag: str, var: list) -> bool:
        cnt = 0
        for v in var:
            if v:
                try:
                    cursor = con.cursor()
                    sql = f"EXEC CT_INSERT_SERVER_INFO '{flag}', '{self.serverid}', '{v}'"
                    cursor.execute(sql)
                    con.commit()
                    cnt += 1
                except:
                    return False
        return cnt == len(var)
