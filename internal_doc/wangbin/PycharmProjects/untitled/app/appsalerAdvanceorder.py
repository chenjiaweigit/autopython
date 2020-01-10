# coding: utf-8
from appsaler import appsalerInformation
import time
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

#预订单
if __name__ == '__main__':
    bb = appsalerInformation("172.18.200.192:7912")
    bb.salerEnterstorehouse()
    bb.salerAddshopping_1()
    bb.salerEntershopping_Cart()
    tv_state = bb.salerEnterAdveeorder()#购物车总价
    print (tv_state)
    sum_money_textview, actual_payment_textview = bb.salerAdverorder("11",u"胜利大街发了圣诞节")#邀请码和备注#预订单的总价和应付额
    print (sum_money_textview)
    print (actual_payment_textview)
    tv_order_money = bb.salerEnterOrder()#
    bb.salerLog_banben(dealer[6],dealer[22])
