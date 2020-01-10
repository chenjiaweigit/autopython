# coding: utf-8
from wangye import wangyeInfomation
# from appsaler import
from pymssqlManage import excelManager
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    aa = wangyeInfomation()
    #uat:http://uat.wincrm.net:8218","winretailsaler","win!@#"
    #retail:"http://retail.wincrm.net:8203","wangbinsaler","71028863"
    aa.wangyeLogin("http://retail.wincrm.net:8203","wangbinsaler","71028863")
    prodSku = aa.wangyeShopgroup(u"自动化分类",u"打奶茶组合自动化4",u"zuheshagnpin4",u"自动化子品牌    ",u"脉动",u"zuheshagnpin4","44",u"1瓶450ml","1","44","43","4",r'F:\zhsp.png')
    # print prodSku
    excelManager.jxsshangpinshangjia(prodSku)
    aa.wangeyqiehuaniframe("menu1")
    aa.wangyeshopBindingManagement(u"王斌自动化测试经销商勿删",u"lebaishi")
    aa.wangeyqiehuaniframe("menu1")
    aa.wangyeShopExcelgrounding('E:\dealerProductPricetypeTemplate.xls')

