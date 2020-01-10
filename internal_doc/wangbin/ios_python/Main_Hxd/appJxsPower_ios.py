# coding: utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretaildealer_IOS

from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)


def appJxsPower():
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    cc.dealer_startapp_ios("14778786566", "aa248163")  # jxs
    cc.dealerJxsPower_ios("jxs")
    cc.dealerOfflogin_ios()
    cc.dealer_startapp_ios("14528745875","14528745875")#送货司机
    cc.dealerJxsPower_ios("shsj")
    cc.dealerOfflogin_ios()
    cc.dealer_startapp_ios("14667764667", "14667764667")  # 车销司机
    cc.dealerJxsPower_ios("chsj")
    cc.dealerOfflogin_ios()
    cc.dealer_startapp_ios("14697876648", "14697876648")  # 首单员
    cc.dealerJxsPower_ios("sdy")
    cc.dealerOfflogin_ios()


# if __name__ == '__main__':
#     cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
#     cc.dealer_startapp_ios("14778786566", "aa248163")  # jxs
#     cc.dealerJxsPower_ios("jxs")
#     cc.dealerOfflogin_ios()
#     cc.dealer_startapp_ios("14528745875","14528745875")#送货司机
#     cc.dealerJxsPower_ios("shsj")
#     cc.dealerOfflogin_ios()
#
#     cc.dealer_startapp_ios("14667764667", "14667764667")  # 车销司机
#     cc.dealerJxsPower_ios("chsj")
#     cc.dealerOfflogin_ios()
#
#     cc.dealer_startapp_ios("14697876648", "14697876648")  # 首单员
#     cc.dealerJxsPower_ios("sdy")
#     cc.dealerOfflogin_ios()

