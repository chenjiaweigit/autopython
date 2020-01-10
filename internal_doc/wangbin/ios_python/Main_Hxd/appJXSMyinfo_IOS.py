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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time



def appJXSMyinfo():
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerMyinfo(saler[19], saler[20], saler[21])


# cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
# cc.dealer_startapp_ios(dealer[4],dealer[5])
# cc.dealerMyinfo("王斌自动化测试经销商勿删","王斌自动化测试经销商(勿删)","王斌自动化工商注册名称")
