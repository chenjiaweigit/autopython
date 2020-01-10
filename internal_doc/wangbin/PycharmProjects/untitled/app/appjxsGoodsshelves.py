# coding: utf-8
from appdealer import appdealerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")


if __name__ == '__main__':
    #货架管理
    cc = appdealerInformation("172.18.200.192:7912")
    # 脉动（青柠）1L*12瓶/箱,6902538004632,54
    phonebrand = cc.dealerstart_app()
    #cc.dealerlogin(dealer[4],dealer[5])
    cc.dealerlogin(int(saler[32]), int(saler[33]))
    cc.dealerGoodsshelves(saler[25],saler[26],saler[27],saler[28],phonebrand)
    cc.dealerLog_banben(dealer[6],dealer[26])
