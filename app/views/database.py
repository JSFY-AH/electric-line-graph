import pyodbc


class SqlServer():
    def __init__(self):
        self.password = "root"
        self.user = "sa"
        self.database = "apt2015"
        self.host = "localhost"

    def connnect(self):
        conn = pyodbc.connect(
            'DRIVER={SQL Server Native Client 10.0};SERVER='+self.host + ';DATABASE='+self.database +';UID='+
            self.user + ';PWD=' + self.password)
        return conn

    def select(self, table, line_id):
        pass