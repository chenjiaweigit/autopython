# coding: utf-8
from appdealer import appdealerInformation
import time
from pymssqlManage import excelManager
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")

if __name__ == '__main__':
    #修改订单的配送时间和送货员；确认订单
    cc = appdealerInformation("172.18.200.192:7912")
    cc.dealerstart_app()
    cc.dealerlogin(int(saler[32]), int(saler[33]))
    cc.dealerOrder_confirm()#修改日期
    cc.dealerLog_banben(dealer[6],dealer[18])
