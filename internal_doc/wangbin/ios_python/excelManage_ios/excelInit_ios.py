#coding: utf-8
import xlrd
import os
from xlutils.copy import copy
import atx
# def jxsshangpinshangjia(prodSku):
#     rb = xlrd.open_workbook(r'E:\dealerProductPricetypeTemplate.xls',formatting_info=True)
#     wb = copy(rb)
#     ws = wb.get_sheet(u'业代导入')
#     ws.write(1,2,prodSku )
#     wb.save(r'E:\dealerProductPricetypeTemplate.xls')
#     pass

def banbeninfo(a,excelname):
    data = xlrd.open_workbook(excelname)
    if a =="uat":
        table = data.sheet_by_name(u"版本信息维护uat")
    elif a=="retail":
        table = data.sheet_by_name(u"ios_retail参数")
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数

    saler = (table.col_values(1))
    dealer = (table.col_values(2))
    sr = (table.col_values(3))
    express = (table.col_values(4))
    htv = (table.col_values(5))
    pc = (table.col_values(6))
    # print(saler)
    # print(dealer)
    # print(sr)
    # print(express)
    # print(htv)
    # print(pc)
    return saler,dealer,sr,express,htv,pc



#更新经销商第一次注册账号
def excelUpdate(s):
    newjxsphthoe =str(int(s)+1)
    rb = xlrd.open_workbook(r'/Users/wangbin/Desktop/banben.xls')
    wb = copy(rb)
    ws = wb.get_sheet(u'ios_retail参数')
    ws.write(24,1,newjxsphthoe )
    wb.save(r'/Users/wangbin/Desktop/banben.xls')

    pass

#更新门店注册第一次注册账号
def excelUpdatereg(s):
    newjxsphthoe =str(int(s)+1)
    rb = xlrd.open_workbook(r'/Users/wangbin/Desktop/banben.xls')
    wb = copy(rb)
    ws = wb.get_sheet(u'ios_retail参数')
    ws.write(42,1,newjxsphthoe )
    wb.save(r'/Users/wangbin/Desktop/banben.xls')

    pass
#更新门店激活第一次注册账号
def excelUpdaterelive(s):
    newjxsphthoe =str((int(s)+1))
    rb = xlrd.open_workbook(r'/Users/wangbin/Desktop/banben.xls')
    wb = copy(rb)
    ws = wb.get_sheet(u'ios_retail参数')
    ws.write(44,1,newjxsphthoe)
    wb.save(r'/Users/wangbin/Desktop/banben.xls')

    pass



# if __name__ == '__main__':
# excelUpdaterelive("14778783505")








