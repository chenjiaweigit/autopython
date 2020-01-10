# coding: utf-8
from appsaler import appsalerInformation
from pymssqlManage import salerSql
import time
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

if __name__ == '__main__':
    #我的信息，地址管理(ok)
    bb = appsalerInformation("172.18.200.192:7912")
    #retail:"14778786568", "aa248163"
    bb.start_app()
    bb.salerlogintrue(int(saler[30]), int(saler[31]))
    bb.salerMyinformation(saler[16],saler[17],saler[18])#王斌自动化
    bb.salerLog_banben(dealer[6],dealer[12])
    bb.salerAddrmanage(saler[19],saler[20],saler[21],saler[22])
    bb.salerLog_banben(dealer[6], dealer[13])
    bb.salerAddrdelete()
    bb.salerLog_banben(dealer[6], dealer[21])
