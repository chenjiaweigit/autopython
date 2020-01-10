# coding: utf-8
from appsaler import appsalerInformation
import time
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")


if __name__ == '__main__':#全部订单
    bb = appsalerInformation("172.18.200.192:7912")
    bb.salerAllorders()
    bb.salerLog_banben(dealer[6],"（true）------hxd版本-全部订单:------")
