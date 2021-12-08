from conf.config import Config
con = Config().conf_db_connection()


class GetSYSGB:
    @staticmethod
    def get_syslist() -> list:
        syslist = []
        cursor = con.cursor()
        sql = "SELECT SYSCODE, SYSNAME FROM SYSCODE WITH(NOLOCK)"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            syslist.append((row[0], row[1]))
            row = cursor.fetchone()
        return syslist

    @staticmethod
    def get_gblist() -> list:
        gblist = []
        cursor = con.cursor()
        sql = "SELECT GBCODE, GBNAME FROM GBCODE WITH(NOLOCK)"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            gblist.append((row[0], row[1]))
            row = cursor.fetchone()
        return gblist
