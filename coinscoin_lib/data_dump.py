import logging as log

from pandas import DataFrame
from coinscoin_lib.coinpaprica_synchronize import CoinSynchronize
from coinscoin_lib.resource_manager import ResourceManager


class DataDump:

    def __init__(self, process_run_key: int = None):
        # Input params
        self.process_run_key = process_run_key
        self.db_session = ResourceManager.db_session()


    @staticmethod
    def run_data_dump_master():
        CoinSynchronize.handle()



#import pymssql
#conn = pymssql.connect(server, user, password, "tempdb")
#
#conn = pymssql.connect(user='sa', password='cardano1dolek!', database='coinscoin-dev')
#conn = pymssql.connect(server='localhost',user='sa', password='cardano1dolek!', database='coinscoin-dev')
#
#conn = pymssql.connect(host='172.19.0.2"|"1433', user='sa', password='cardano1dolek!', database='coinscoin')
#cursor = conn.cursor()
#cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')
#row = cursor.fetchone()
#while row:
#    print str(row[0]) + " " + str(row[1]) + " " + str(row[2])
#    row = cursor.fetchone()

#import pyodbc
#server = '127.0.0.1, 1433'
#database = 'coinscoin-dev'
#username = 'SA'
#password = 'cardano1dolek!'
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#
#
#import pyodbc
#connect_str = "Driver={ODBC Driver 17 for SQL Server};" + \
#              "Server={{{server}}},1433;".format(server='localhost') + \
#              "Database={{{database}}};".format(database='coinscoin-dev') + \
#              "uid={{{uid}}};".format(uid='SA') + \
#              "pwd={{{pwd}}};".format(pwd='''cardano1dolek!''')
#cnxn = pyodbc.connect(connect_str)
#
#
#
#conn = pyodbc.connect( r'DRIVER={SQL Server};SERVER=localhost;Integrated_Security=false;Trusted_Connection=yes;UID=sa;PWD=cardano1dolek!;DATABASE=coinscoin-dev')
