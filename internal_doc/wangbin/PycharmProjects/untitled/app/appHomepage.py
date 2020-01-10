# coding: utf-8
#from wangye import wangyeInfomation
from appsaler import appsalerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")
#首页

if __name__ == '__main__':
    bb = appsalerInformation("172.18.200.192:7912")
    bb.start_app()
    bb.salerlogintrue(int(saler[4]),int(saler[5]))
    bb.appsalerHomepage_lunbotu()
    bb.salerLog_banben(dealer[6],dealer[9])
