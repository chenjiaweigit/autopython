#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import wangye_IOS
from AppClass import winretailsaler_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)


import time

def appPromotion_IOS():
    #促销信息
    aa = wangye_IOS.wangyeInfomation()
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
    aa.wangyeLogin(saler[1],saler[2],saler[3])
    # #linkDesc 设置代理品牌促销信息
    linkDesc = aa.wangyePromotion_banner(u"王斌自动化测试经销商勿删",u"脉动",u"自动化-品牌促销信息10")
    aa.wangeyqiehuaniframe("menu1")
    promotionSimpleDesc = aa.wangyePromotion_jxs(u"王斌自动化测试经销商勿删",u"自动化-经销商促销信息10")
    aa.wangeyqiehuaniframe("menu1")
    prodPromotion = aa.wangyePromotion_shop(u"王斌自动化测试经销商勿删",u"南京脉动扫尾货套餐",u"自动化经-销商商品促销信息10","0")
    bb.saler_startapp_ios(saler[4],saler[5])
    bb.salerEnterstorehouse_ios()
    time.sleep(3)
    shopPromotion1, shopPromotion2, banerProtion1, jxsProtion=bb.salerPromotion_ios()
    print(shopPromotion1,prodPromotion)
    print(shopPromotion2,prodPromotion)
    print(jxsProtion,promotionSimpleDesc)
    print(banerProtion1,linkDesc)
    assert  prodPromotion in shopPromotion2
    assert  prodPromotion in shopPromotion1
    assert  promotionSimpleDesc in jxsProtion
    assert  linkDesc in banerProtion1





# if __name__ == '__main__':
#     #促销信息
import atx
d =atx.connect("http://localhost:8100")
print d(className="StaticText", index=35).text