# coding: utf-8
import pyodbc
def expresssql_Cust_title(name):
    conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
    cnxn = pyodbc.connect(conn_info)
    sqlname = "SELECT  CUST_TITLE FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
    cursor = cnxn.cursor()
    cursor.execute(sqlname)
    row = cursor.fetchone()
    return (str(row))

