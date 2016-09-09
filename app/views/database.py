import pyodbc


class SqlServer():
    def __init__(self):
        self.password = "apt2015aptyanke"
        self.user = "sa"
        self.database = "apt2015"
        self.host = "61.234.123.236"

    def connnect(self):
        conn = pyodbc.connect(
            'DRIVER={SQL Server Native Client 10.0};SERVER='+self.host + ';DATABASE='+self.database +';UID='+
            self.user + ';PWD=' + self.password)
        return conn

    def select(self, table, line_id):
        pass
