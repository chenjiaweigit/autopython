# coding: utf-8
import time
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretailsaler_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)



def appModifypwd_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios(saler[4], saler[5])
    bb.salerModifypwd(saler[5], saler[5], saler[5], saler[4])


# #修改密码
#     bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
#     bb.saler_startapp_ios(saler[4], "aa248163")
#     bb.salerModifypwd("aa248163", "aa248163", "aa248163", saler[4])