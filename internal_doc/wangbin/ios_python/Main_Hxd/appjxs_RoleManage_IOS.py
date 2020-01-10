#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretaildealer_IOS
import time
from AppClass import Commonvariable
from excelManage_ios import excelInit_ios
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)

def appjxs_RoleManage_IOS():
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    time.sleep(2)
    cc.dealerRoleManage_ios(saler[15], saler[16], dealer[4], dealer[5])


# #人员管理
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# cc.dealer_startapp_ios("14778786566","aa248163")
# time.sleep(2)
# cc.dealerRoleManage_ios(u"新增jxs人员角色","14778786563","14778786566","aa248163")