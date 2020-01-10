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

def appWareHouse_IOS():
    # 仓库
    bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
    bb.saler_startapp_ios(saler[4], saler[5])
    bb.salerHomepage_ios(saler[52])
    time.sleep(2)
    bb.salerWarehouse_ios("3", "脉动")



# #仓库
# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# bb.saler_startapp_ios(saler[4],saler[5])
# bb.salerHomepage_ios(saler[6])
# time.sleep(2)
# bb.salerWarehouse_ios("3","脉动")