# coding: utf-8
from wangye import wangyeInfomation
from appsaler import appsalerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

import time
if __name__ == '__main__':
    #促销信息
    aa = wangyeInfomation()
    bb = appsalerInformation("172.18.200.192:7912")
    #uat:http://uat.wincrm.net:8218","winretailsaler","win!@#"
    #retail:"http://retail.wincrm.net:8203","wangbinsaler","71028863"
    aa.wangyeLogin(saler[1],saler[2],saler[3])
    # #linkDesc 设置代理品牌促销信息
    linkDesc = aa.wangyePromotion_banner(saler[7],saler[8],saler[9])
    aa.wangeyqiehuaniframe("menu1")
    promotionSimpleDesc = aa.wangyePromotion_jxs(saler[10],saler[11])
    aa.wangeyqiehuaniframe("menu1")
    prodPromotion = aa.wangyePromotion_shop(saler[12],saler[13],saler[14],saler[15])
    bb.start_app()
    bb.salerlogintrue(saler[4],saler[5])
    bb.salerEnterstorehouse()
    time.sleep(3)
    shopPromotion1, shopPromotion2, banerProtion1, jxsProtion=bb.salerPromotion()
    print(shopPromotion1,prodPromotion)
    print(shopPromotion2,prodPromotion)
    print(jxsProtion,promotionSimpleDesc)
    print(banerProtion1,linkDesc)
    # assert shopPromotion1 == prodPromotion and shopPromotion2 == prodPromotion and jxsProtion ==promotionSimpleDesc and banerProtion1==linkDesc
    assert shopPromotion2 ==prodPromotion
    assert shopPromotion1 == prodPromotion
    assert jxsProtion ==promotionSimpleDesc
    assert banerProtion1==linkDesc
    bb.salerLog_banben(dealer[6],dealer[11])
