# coding: utf-8
import pymssql


# conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
# cnxn = pyodbc.connect(conn_info)
# sqlname = "SELECT top 1 CRM_USER_REGISTER_LOG.LON,CRM_USER_REGISTER_LOG.LAT FROM CRM_WS_CUSTOMER WITH (nolock) INNER JOIN " \
#           "CRM_USER_REGISTER_LOG ON CRM_WS_CUSTOMER.CUSTOMER_ID = CRM_USER_REGISTER_LOG.CUSTOMER_ID WHERE " \
#           "CRM_WS_CUSTOMER.MOBILE = '14778786561' ORDER BY CRM_USER_REGISTER_LOG.ID DESC "
# cursor = cnxn.cursor()
# cursor.execute(sqlname)
# row = cursor.fetchone()
# print(row)
#
# #我的信息
# def salersql_appinfo(name):
#     conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%('CRM_RETAIL', '118.186.244.9', 'wangbin', 'wb@HYTX.2017')
#     cnxn = pyodbc.connect(conn_info)
#     sqlname = "SELECT  CUST_PLATFORM,CUST_VERSION FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
#     cursor = cnxn.cursor()
#     cursor.execute(sqlname)
#     row = cursor.fetchone()
#     return row
#
# #注册
def salersql_register_ios(name):
    db = pymssql.connect(host='118.186.244.9',user='wangbin',password='wb@HYTX.2017',database='CRM_RETAIL')
    cursor = db.cursor()
    sqlname = "SELECT SMS_CODE FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
    cursor.execute(sqlname)
    results = cursor.fetchall()
    code = str(results[0][0])
    print(code)
    print(type(code))
    return code
# # #注册验证码
# def salersql_register_ios(name):
#     db = pymssql.connect(host='118.186.244.9',user='wangbin',password='wb@HYTX.2017',database='CRM_RETAIL')
#     cursor = db.cursor()
#     sqlname = "SELECT SMS_CODE FROM CRM_WS_CUSTOMER WITH(nolock) where MOBILE = '"+ name+"'"
#     cursor.execute(sqlname)
#     results = cursor.fetchall()
#     code = str(results[0][0])
#     print(code)
#     print(type(code))
#     return code

#坐标
def salersql_finish_regInfo_ios(name):
    db = pymssql.connect(host='118.186.244.9',user='wangbin',password='wb@HYTX.2017',database='CRM_RETAIL')
    cursor = db.cursor()
    sqlname = "SELECT TOP 1 CRM_USER_REGISTER_LOG.LON FROM CRM_WS_CUSTOMER WITH (nolock) INNER JOIN CRM_USER_REGISTER_LOG ON CRM_WS_CUS" \
          "TOMER.CUSTOMER_ID = CRM_USER_REGISTER_LOG.CUSTOMER_ID WHERE CRM_WS_CUSTOMER.MOBILE = '"+name+"' ORDER BY CRM_US" \
          "ER_REGISTER_LOG.ID DESC"
    cursor.execute(sqlname)
    results = cursor.fetchall()
    code = str(results[0][0])
    print(code)
    print(type(code))
    return code

def salerSUMMyCoupon(moblie,status):
    db = pymssql.connect(host='118.186.244.9',user='wangbin',password='wb@HYTX.2017',database='CRM_RETAIL')
    cursor = db.cursor()
    #状态(0-无效,1-已使用，2-未使用， 3-已过期,4-退回)
    sqlname1 = "SELECT  COUNT(*) from  HXD_COUPON_TEMPLATE_send a with(nolock) where  phone = '"+moblie+"' and status = 1"#已经使用
    sqlname2 = "SELECT COUNT ( * ) FROM  HXD_COUPON_TEMPLATE_send a WITH ( nolock )  LEFT JOIN CRM_WS_CUSTOMER W WITH ( nolock )  ON a.CUSTOMER_ID=W.CUSTOMER_ID WHERE    W.MOBILE = '"+moblie+"' AND W.CUST_TITLE='店主'    AND ( status = 2 OR status = 4 )    AND end_time >= GETDATE()"#未使用
    sqlname3 = "SELECT  COUNT(*) from  HXD_COUPON_TEMPLATE_send a with(nolock) where  phone = '"+moblie+"' and (status = 2 or status = 4) and GETDATE() > end_time"#已经过期
    if status =="可使用":
        s = cursor.execute(sqlname2)
        results = cursor.fetchall()
        code = str(results[0][0])
        print(code)
    elif status =="已使用":
        s = cursor.execute(sqlname1)
        results = cursor.fetchall()
        code = str(results[0][0])
        print(code)
    elif status == "已过期":
        s = cursor.execute(sqlname3)
        results = cursor.fetchall()
        code = str(results[0][0])
        print(code)
    return code

if __name__ == '__main__':
    # salersql_register_ios("14778786550")
    aa =salerSUMMyCoupon("14778786561","可使用")
    aa = salerSUMMyCoupon("14778786561", "已使用")
    aa = salerSUMMyCoupon("14778786561", "已过期")




