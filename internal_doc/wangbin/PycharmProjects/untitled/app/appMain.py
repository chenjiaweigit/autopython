# coding: utf-8
from appsaler import appsalerInformation
from appdealer import appdealerInformation
from wangye import wangyeInfomation
import time
import threading
from assertpy import assert_that
from pymssqlManage import excelManager
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")
xlsxHt_hxdUrl = saler[1]
xlsxHt_hxdname = saler[2]
xlsxHt_hxdpwd = saler[3]
xlsx_salername = int(saler[32])
xlsx_salerpwd = int(saler[33])
xlsx_dealername = int(saler[36])
xlsx_dealerpwd = int(saler[37])

def aa(ip):
    # 登录
    bb = appsalerInformation(ip)
    phonebrand = bb.start_app()
    bb.salerLog_banben(dealer[30],dealer[31])
    bb.salerlogintrue(xlsx_salername,xlsx_salerpwd)
    bb.salerLog_banben(dealer[30],dealer[32])
    # bb.appscreenshot()

    # 首页管理
    time.sleep(5)
    bb.appsalerHomepage_lunbotu()
    bb.salerLog_banben(dealer[30],dealer[33])

    # 经销商仓库
    # #bb.appsalerjxs()
    bb.salerEnterstorehouse()
    isTure = bb.salerjxsStorehouse(saler[45],"HUAWEI")
    bb.salerLog_banben(dealer[30],dealer[34])
    time.sleep(3)
    bb.salerBack()
    bb.salerBack()

    #促销信息
    aa = wangyeInfomation()
    #网页登录
    aa.wangyeLogin(xlsxHt_hxdUrl, xlsxHt_hxdname, xlsxHt_hxdpwd)
    #linkDesc 设置代理品牌促销信息
    #linkDesc = aa.wangyePromotion_banner(saler[7],saler[8], saler[9])
    linkDesc = aa.wangyePromotion_banner(saler[46], saler[45], saler[47])
    aa.wangeyqiehuaniframe("menu1")
    #promotionSimpleDesc = aa.wangyePromotion_jxs(saler[10], saler[11])
    promotionSimpleDesc = aa.wangyePromotion_jxs(saler[46], saler[48])
    aa.wangeyqiehuaniframe("menu1")
    #prodPromotion = aa.wangyePromotion_shop(saler[12], saler[13],saler[14], saler[15])
    prodPromotion = aa.wangyePromotion_shop(saler[46], saler[45], saler[49],int(saler[50]))
    bb.salerEnterstorehouse()
    shopPromotion1, shopPromotion2, banerProtion1, jxsProtion = bb.salerPromotion()
    assert_that (shopPromotion1 == prodPromotion and shopPromotion2 == prodPromotion and banerProtion1 == linkDesc and jxsProtion == promotionSimpleDesc)
    bb.salerLog_banben(dealer[30],dealer[35])
    bb.salerBack()
    time.sleep(3)
    bb.salerBack()
    time.sleep(3)
    bb.salerBack()
    time.sleep(3)
    bb.salerBack()
    time.sleep(3)
    bb.salerMyinformation(saler[16],saler[17],saler[18])#王斌自动化
    bb.salerLog_banben(dealer[30],dealer[36])
    #bb.salerAddrmanage(saler[19],saler[20],saler[21],saler[22])
    #bb.salerAddrdelete()
    # bb.salerLog_banben(dealer[6],dealer[13])
    # bb.salerBack()
    # bb.salerBack()
    # bb.start_app()

    #升级
    bb.salerUpgrade(str(xlsx_salername),"huawei")
    cc = appdealerInformation(ip)
    cc.dealerstart_app()
    cc.dealerlogin(xlsx_dealername,xlsx_dealerpwd)
    cc.dealerUpgrade(str(xlsx_dealername))
    bb.salerLog_banben(dealer[30],dealer[38])
    cc.dealerBack()
    bb.start_app()
    bb.salerBack()

    # 修改密码
    pwd1 = bb.salermodifypwd(xlsx_salerpwd,str(xlsx_salerpwd)+"new")
    print(pwd1[0],pwd1[1])
    bb.salerlogintrue(xlsx_salername,pwd1[1])
    cc.dealerstart_app()
    pwd2 = cc.dealerModifypwd(xlsx_dealerpwd,str(xlsx_dealerpwd)+"new",str(xlsx_dealerpwd)+"new")
    print(pwd2[0],pwd2[1])
    cc.dealerlogin(xlsx_dealername,pwd2[1])
    bb.salerLog_banben(dealer[30], dealer[39])
    bb.start_app()

    # 惠聊
    bb.salerHuionline(phonebrand)
    bb.salerAddshopping("5")
    # # cc.dealerlogin(u"14778786566",u"aa248163")#jxs登录
    cc.dealerstart_app()
    cc.dealerHuionline()
    cc.dealerHuionline_youhuiquan()
    bb.salerHuionline_youhuiquan()
    bb.salerLog_banben(dealer[30], dealer[40])
    time.sleep(4)
    bb.salerBack()
    time.sleep(3)
    bb.salerBack()

    # 预订单
    bb.salerEnterstorehouse()
    bb.salerAddshopping_1()
    bb.salerEntershopping_Cart()
    # 购物车总价
    tv_state = bb.salerEnterAdveeorder()
    print (tv_state)

    # 邀请码和备注#预订单的总价和应付额
    sum_money_textview, actual_payment_textview = bb.salerAdverorder(int(saler[51]),saler[52])
    print (sum_money_textview)
    print (actual_payment_textview)
    tv_order_money = bb.salerEnterOrder()
    print (tv_order_money)
    cc.dealerstart_app()
    cc.dealerBack()
    time.sleep(4)
    cc.dealerBack()
    bb.salerLog_banben(dealer[30], dealer[41])

    # 选择送货员，确认订单，选择现金支付
    #bb = appsalerInformation(ip)
    #cc = appdealerInformation(ip)
    cc.dealerOrder_confirm()
    bb.start_app()
    bb.finishorder()
    bb.salerLog_banben(dealer[30], dealer[42])
    #cc.dealerBack()
    #time.sleep(3)
    #cc.dealerBack()

    # 退出登录
    bb.salerloginOff()
    cc.dealerstart_app()
    cc.dealerOfflogin()
    #aa.wangyeQuit()
    bb.salerLog_banben(dealer[30], dealer[43])



if __name__ == '__main__':
    t1 = threading.Thread(target=aa, args=("172.18.200.192:7912",))
    # t2 = threading.Thread(target=aa, args=("192.168.253.7:7912",))
    t1.start()
    # t2.start()
















