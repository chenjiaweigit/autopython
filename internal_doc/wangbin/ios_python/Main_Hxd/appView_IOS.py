#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretailsr_IOS
from AppClass import winretailsaler_IOS
from AppClass import winretaildealer_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
#意见反馈
def appView_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios(saler[4], saler[5])
    bb.salerView(saler[50], saler[4])
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerView(saler[51], dealer[4])

# appView_IOS()


# bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
# bb.saler_startapp_ios(saler[4],saler[5])
# bb.salerView("sdffsdfsdfsd","14778786561")
# cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
# cc.dealer_startapp_ios(dealer[4],dealer[5])
# cc.dealerView("dsfdsfsdfdsfd","14778786566")
