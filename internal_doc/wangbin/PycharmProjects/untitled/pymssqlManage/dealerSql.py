# coding: utf-8
import pyodbc
def dealersql_Cust_title(name):
    conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
    cnxn = pyodbc.connect(conn_info)
    sqlname = "SELECT  CUST_TITLE FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
    cursor = cnxn.cursor()
    cursor.execute(sqlname)
    row = cursor.fetchone()
    return (str(row))
def dealersql_appinfo(name):
    #conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
    #conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL_UAT', '192.168.60.3', 'Retail_Uat_AutoTest', 'z1ZjXP6dkkkbScJ4')
    conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL', '118.186.244.9', 'fanhanqing', 'rVbGrebhsFow0NUV')
    cnxn = pyodbc.connect(conn_info)
    sqlname = "SELECT  CUST_PLATFORM,CUST_VERSION FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
    cursor = cnxn.cursor()
    cursor.execute(sqlname)
    row = cursor.fetchone()
    print(row[0])
    print(row[1])
    return row
if __name__ == '__main__':
    row = dealersql_appinfo("14778786561")
    print(str(row[0]))
    print(str(row[1]))





