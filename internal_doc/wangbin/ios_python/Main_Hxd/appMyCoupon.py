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
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import time



def appMyCoupon_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios(saler[4], saler[5])
    bb.salerMycoupon(saler[4])

# appMyCoupon_IOS()

# #我的优惠券
# bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
# bb.saler_startapp_ios(saler[3],saler[4])
# bb.salerMycoupon("14778786561")
