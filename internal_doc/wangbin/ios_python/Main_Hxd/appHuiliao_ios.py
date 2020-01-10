# coding: utf-8
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



def appHuiliao_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    #
    bb.saler_startapp_ios(saler[4], saler[5])
    startNum = bb.salerHuiliao_ios(saler[13], saler[14])
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerHuiliao_ios(startNum)


# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# #
# bb.saler_startapp_ios(saler[4],saler[5])
# startNum = bb.salerHuiliao_ios(u"王斌",u"自动化消息")
# cc.dealer_startapp_ios(dealer[4],dealer[5])
# cc.dealerHuiliao_ios(startNum)