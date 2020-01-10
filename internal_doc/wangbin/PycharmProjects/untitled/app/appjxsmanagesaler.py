# coding: utf-8
from appdealer import appdealerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

if __name__ == '__main__':
    #经销商人员管理
    cc = appdealerInformation("172.18.200.192:7912")
    cc.dealerstart_app()
    cc.dealerlogin(int(saler[32]), int(saler[33]))
    cc.dealerManagesalers(saler[29],saler[28])
    cc.dealerLog_banben(dealer[6],dealer[23])
