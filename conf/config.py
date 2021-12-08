import json


class Config:
    def __init__(self):
        with open('conf\config.json', 'r', encoding='UTF-8') as file:
            self.conf = json.load(file)

    def conf_db_connection(self):
        import pymssql
        import decimal
        return pymssql.connect(self.conf['Database']['ip'], self.conf['Database']['id'],
                               self.conf['Database']['password'], self.conf['Database']['name'])

    def conf_todays_checker(self, flag: str):
        return self.conf["TodaysChecker"][flag]

    def conf_main_form(self, flag: str):
        return self.conf["MainForm"][flag]

    def conf_insert_svr(self, flag: str):
        return self.conf["InsertSvr"][flag]

    def conf_manage_code(self, flag: str):
        return self.conf["ManageCode"][flag]

    def conf_delete_svr(self, flag: str):
        return self.conf["DeleteSvr"][flag]
