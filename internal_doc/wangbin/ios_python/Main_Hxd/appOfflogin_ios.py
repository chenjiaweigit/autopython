#-*- coding: UTF-8 -*-
import time
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretailsaler_IOS
from AppClass import winretaildealer_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)



def appOfflogin_IOS():
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios(dealer[4], dealer[5])  # jxs
    cc.dealerOfflogin_ios()

# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# cc.dealer_startapp_ios("14778786566","aa248163")#jxs
# cc.dealerOfflogin_ios()
# cc.dealer_startapp_ios("14778786566","aa248163")#jxs

