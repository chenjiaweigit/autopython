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


def appRegister_IOS():
    # 门店注册
    bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
    bb.salerOffLogin(saler[4],saler[5])
    bb.salerRegister_IOS("普通注册",saler[42], saler[43], "1",saler[42])
    # bb.saler_startapp_ios("14778785569","aa248163")

# #门店注册
# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# bb.salerRegister_IOS("邀请注册","14778785569","自动化姓名","1")
# # bb.saler_startapp_ios("14778785569","aa248163")
