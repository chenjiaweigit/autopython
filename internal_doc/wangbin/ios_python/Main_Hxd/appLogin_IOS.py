# coding: utf-8
#!/usr/bin/env python
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



def appLogin():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios(saler[4], saler[5])
# appLogin()


# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# bb.saler_startapp_ios(saler[4],"aa248163")
