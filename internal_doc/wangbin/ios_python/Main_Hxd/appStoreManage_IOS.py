#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretaildealer_IOS
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time


def appStoreManage_IOS():
    cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
    cc.dealer_startapp_ios("14778786566", "aa248163")
    cc.dealerStoreManage("自动化名称我的")

# #人员管理
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# cc.dealer_startapp_ios("14778786566","aa248163")
# cc.dealerStoreManage("3")