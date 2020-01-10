# coding: utf-8
from appsaler import appsalerInformation
from appdealer import appdealerInformation
from pymssqlManage import excelManager
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"D:\excel\banben.xls")

if __name__ == '__main__':
    bb = appsalerInformation("172.18.200.192:7912")
    cc = appdealerInformation("172.18.200.192:7912")
    phonebrand = bb.start_app()
    bb.salerHuionline(phonebrand)
    bb.salerAddshopping("5")
    # cc.dealerlogin(u"14778786566",u"aa248163")#jxs登录
    cc.dealerstart_app()
    cc.dealerHuionline()
    cc.dealerHuionline_youhuiquan()
    bb.salerHuionline_youhuiquan()
    bb.salerLog_banben(dealer[6], "（true）------hxd版本-惠聊:------")
