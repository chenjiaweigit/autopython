#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretaildealer_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)


def appjxsGoodsshelves_IOS():
    cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
    # 脉动（青柠）1L*12瓶/箱,6902538004632,54
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerjxsGoodsshelves_ios(saler[17], saler[18], dealer[4], dealer[5])


# #货架管理
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# # 脉动（青柠）1L*12瓶/箱,6902538004632,54
# cc.dealer_startapp_ios("14778786566", "aa248163")
# cc.dealerjxsGoodsshelves_ios(u"南京","201.99","14778786566", "aa248163")

