#coding: utf-8
import xlrd
#import os
from xlutils.copy import copy
#import atx
# from xlwt import Style
#import uiautomator2 as ut2
# s = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
def jxsshangpinshangjia(prodSku):
    rb = xlrd.open_workbook(r'E:\dealerProductPricetypeTemplate.xls',formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(u'业代导入')
    ws.write(1,2,prodSku )
    wb.save(r'E:\dealerProductPricetypeTemplate.xls')
    pass

def banbeninfo(a,excelname):
    data = xlrd.open_workbook(excelname)
    if a =="uat":
        table = data.sheet_by_name(u"版本信息维护uat")
    else:
        table = data.sheet_by_name(u"版本信息维护retail")
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数

    saler = (table.col_values(1))
    dealer = (table.col_values(2))
    sr = (table.col_values(3))
    express = (table.col_values(4))
    htv = (table.col_values(5))
    pc = (table.col_values(6))
    #print(saler)
    #print(dealer)
    #print(sr)
    #print(express)
    #print(htv)
    #print(pc)
    return saler,dealer,sr,express,htv,pc


if __name__ == '__main__':
    #saler = banbeninfo("retail",r"E:\banben\banben.xlsx")
    saler = banbeninfo("retail", r"D:\excel\banben.xls")
    print(saler[1][1])








