# coding: utf-8
from appsaler import appsalerInformation
from appdealer import appdealerInformation
from pymssqlManage import excelManager
#saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"D:\excel\banben.xls")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

if __name__ == '__main__':#升级
    aa = appsalerInformation("172.18.200.192:7912")
    bb = appdealerInformation("172.18.200.192:7912")#需要调试优化dealer的升级
    bb.dealerstart_app()
    bb.dealerlogin(int(saler[32]),int(saler[33]))
    #print(str(int(saler[32])))
    bb.dealerUpgrade(str(int(saler[32])))
    bb.dealerLog_banben(dealer[6],dealer[24])
    # print(str(row[1]))
    phonebrand = aa.start_app()
    aa.salerlogintrue(int(saler[30]),int(saler[31]))
    aa.salerUpgrade(str(int(saler[30])),phonebrand)
    aa.salerLog_banben(dealer[6],dealer[23])
