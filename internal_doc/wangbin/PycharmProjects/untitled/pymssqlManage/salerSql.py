# coding: utf-8
import pyodbc
conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
cnxn = pyodbc.connect(conn_info)
sqlname = "SELECT top 1 CRM_USER_REGISTER_LOG.LON,CRM_USER_REGISTER_LOG.LAT FROM CRM_WS_CUSTOMER WITH (nolock) INNER JOIN " \
          "CRM_USER_REGISTER_LOG ON CRM_WS_CUSTOMER.CUSTOMER_ID = CRM_USER_REGISTER_LOG.CUSTOMER_ID WHERE " \
          "CRM_WS_CUSTOMER.MOBILE = '14778786561' ORDER BY CRM_USER_REGISTER_LOG.ID DESC "
cursor = cnxn.cursor()
cursor.execute(sqlname)
row = cursor.fetchone()
print(row)

def salersql_appinfo(name):
    #conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
    #conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL_UAT', '192.168.60.3', 'Retail_Uat_AutoTest', 'z1ZjXP6dkkkbScJ4')
    conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL', '118.186.244.9', 'fanhanqing', 'rVbGrebhsFow0NUV')
    cnxn = pyodbc.connect(conn_info)
    sqlname = "SELECT  CUST_PLATFORM,CUST_VERSION FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
    cursor = cnxn.cursor()
    cursor.execute(sqlname)
    row = cursor.fetchone()
    return row



