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
# Commonvariable.PORT

saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)


#地址管理
def appAddrmanage_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios("14778785572", "785572")  # 激活的账号北京
    bb.salerAddrmanage(saler[8], saler[9], saler[10], saler[11])




# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# bb.saler_startapp_ios("14778785572","785572")#激活的账号北京
# bb.salerAddrmanage(u"ios自动化","15122674750",u"就到了教室里发生的了","076161")