# coding: utf-8
import time
from appdealer import appdealerInformation
from appsaler import appsalerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

#退出登录，再登录(ok)
if __name__ == '__main__':
    # salerretail:14778786568 aa248163
    #delaerretail:14778786566 aa248163

    #aa = appsalerInformation("192.168.253.3:7912")
    #bb = appdealerInformation("192.168.253.3:7912")

    aa = appsalerInformation("172.18.200.192:7912")
    bb = appdealerInformation("172.18.200.192:7912")

    aa.start_app()
    salerinformatin = aa.salerlogintrue(int(saler[4]),int(saler[5]))
    print (salerinformatin)
    aa.salerloginOff()
    aa.salerlogintrue(int(saler[4]),int(saler[5]))
    time.sleep(3)
    aa.appscreenshot()
    aa.salerLog_banben(dealer[6],dealer[19])

    bb.dealerstart_app()
    bb.dealerlogin(dealer[4], dealer[5])
    bb.dealerOfflogin()
    bb.dealerlogin(dealer[4], dealer[5])
    bb.dealerLog_banben(dealer[6],dealer[20])



