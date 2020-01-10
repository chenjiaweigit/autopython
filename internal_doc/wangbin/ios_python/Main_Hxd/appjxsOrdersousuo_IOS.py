#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretaildealer_IOS
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time

from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)


#订单搜索
def appjxsOrdersousuo_IOS():
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerjxsOrdersousuo_ios(saler[38])

# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# cc.dealer_startapp_ios("14778786566","aa248163")
# cc.dealerjxsOrdersousuo_ios(u"自动化名称3")