# coding: utf-8

from appexpress import appexpressInformation
from pymssqlManage import excelManager

'''调取excel中的数据uat or retail'''
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")
xlsx_expressname = express[4]
xlsx_expresspwd = express[5]
if __name__ == '__main__':
    ee = appexpressInformation()
    ee.expressStart()
    phone_brand = ee.expressLogin(xlsx_expressname,xlsx_expresspwd)
    # ee.expressDriverManage(u"自动化_司机1","14211011010","130728199007276013",phone_brand)
    # ee.expressBack()
    # ee.expressMyinfo()
    # ee.expressBack()
    # ee.expressBack()
    ee.expressCarsmanage(u"自动化车辆1","123123","2","2","2","15")
    ee.expressBack()