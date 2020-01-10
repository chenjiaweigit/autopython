# coding: utf-8
from appsaler import appsalerInformation
import time
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

#经销商仓库
if __name__ == '__main__':
    bb  = appsalerInformation("172.18.200.192:7912")
    phthonbanner = bb.start_app()
    bb.salerlogintrue(int(saler[30]),int(saler[31]))
    bb.salerEnterstorehouse()
    bb.salerjxsStorehouse(saler[6],phthonbanner)
    bb.salerLog_banben(dealer[6],dealer[10])


