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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time


def appClosedOrder():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    bb.saler_startapp_ios(saler[4], saler[5])
    bb.salerEnterstorehouse_ios()  # 进入仓库
    time.sleep(2)
    sumck = bb.salerAddShopsTogwc_ios()  # 加入到购物车
    time.sleep(2)
    sumgwc = bb.salerAddShopsToydd(sumck)  # 加入到预订单
    time.sleep(2)

    sumydd = bb.saleraddyddToorder(sumgwc, Commonvariable.SALER_ISSELECT_a)  # 下单是否选择优惠券
    cc.dealer_startapp_ios(dealer[4], dealer[5])
    cc.dealerOrderinfo_ios(u"待确认")
    time.sleep(3)
    cc.dealerbackone_ios()
    cc.dealerOrderinfo_ios(u"待发货")
    cc.dealerbackone_ios()
    cc.dealerOrderinfo_ios(u"关闭订单")


# #关闭订单
# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# bb.saler_startapp_ios(saler[4],"aa248163")
# bb.salerEnterstorehouse_ios()#进入仓库
# time.sleep(2)
# sumck = bb.salerAddShopsTogwc_ios()#加入到购物车
# time.sleep(2)
# sumgwc = bb.salerAddShopsToydd(sumck)#加入到预订单
# time.sleep(2)
# from AppClass import Commonvariable
# sumydd = bb.saleraddyddToorder(sumgwc,Commonvariable.SALER_ISSELECT_a)#下单是否选择优惠券
# cc.dealer_startapp_ios("14778786566","aa248163")
# cc.dealerOrderinfo_ios(u"待确认")
# time.sleep(3)
# cc.dealerbackone_ios()
# cc.dealerOrderinfo_ios(u"待发货")
# cc.dealerbackone_ios()
# cc.dealerOrderinfo_ios(u"关闭订单")
