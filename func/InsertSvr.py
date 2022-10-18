from conf.config import Config

con = Config().conf_db_connection()


class InsertSvr():
    def __init__(self, host, ip):
        self.host = host
        self.ip = ip
        self.serverid = 0

    def insert_svr(self, wdef, sys_code, gb_code):
        cursor = con.cursor()
        print(self.host, type(self.host))
        print(self.ip, type(self.ip))
        print(wdef, type(wdef))
        print(sys_code, type(sys_code))
        print(gb_code, type(gb_code))
        #sql = f"EXEC CT_INSERT_SERVER '{self.host}', '{self.ip}', {wdef}, {sys_code}, {gb_code}"
        sql = f"insert into server values '{self.host}', '{self.ip}', {wdef}, {sys_code}, {gb_code}"
        cursor.execute(sql)

        self.serverid = self.get_serverid()

    def get_serverid(self) -> int:
        cursor = con.cursor()
        sql = f"SELECT SERVERID FROM SERVER WHERE HOSTNAME = {self.host} AND IP = {self.ip}"
        cursor.execute(sql)
        row = cursor.fetchall()
        return row[0][0]

    def insert_svr_info(self, flag: str, var: list):
        for v in var:
            cursor = con.cursor()
            sql = f"EXEC CT_INSERT_SERVER_INFO {flag}, {self.serverid}, {v}"
            cursor.execute(sql)
