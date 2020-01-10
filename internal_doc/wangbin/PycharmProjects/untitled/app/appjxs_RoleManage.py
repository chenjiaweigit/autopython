# coding: utf-8
from appdealer import appdealerInformation
#from wangye import wangyeInfomation
import time
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")


if __name__ == '__main__':
    #经销商人员管理"192.168.253.7:7912"
    cc = appdealerInformation("172.18.200.192:7912")
    phonebrand = cc.dealerstart_app()
    print(phonebrand)
    cc.dealerlogin(int(saler[32]),int(saler[33]))
    cc.dealerRoleManage(u"新增自动化送货司机","14545482112","14545482112","1707810","14545482112","14545482112","14778786566","aa248163","14545482112")