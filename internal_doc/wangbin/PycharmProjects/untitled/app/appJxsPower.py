# coding: utf-8
from appdealer import appdealerInformation
from pymssqlManage import dealerSql
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

if __name__ == '__main__':
#经销商权限功能
    cc = appdealerInformation("172.18.200.192:7912")
    cc.dealerstart_app()
    #登录不同的角色（送货员，车销司机，收单员，经销商）1707810  song ,14528745875，che 14667764667，shou  14697876648,jxs  14778786566
    # dealername = cc.dealerlogin(int(saler[32]),int(saler[33]))#经销商
    # print(dealername)
    # cust_title = dealerSql.dealersql_Cust_title(str(dealername))
    # print(cust_title)
    # cc.dealerRolePower(cust_title)
    # cc.dealerOfflogin()#退出登录
    #
    # dealername = cc.dealerlogin("14697876648","14697876648")#收单员
    # print(dealername)
    # cust_title = dealerSql.dealersql_Cust_title(str(dealername))
    # print(cust_title)
    # cc.dealerRolePower(cust_title)
    # cc.dealerOfflogin()#退出登录

    dealername = cc.dealerlogin("14667764667","14667764667")#车销司机
    print(dealername)
    cust_title = dealerSql.dealersql_Cust_title(str(dealername))
    print(cust_title)
    cc.dealerRolePower(cust_title)
    #cc.dealerOfflogin()#退出登录

    # dealername = cc.dealerlogin("14528745875","14528745875")#送货司机
    # print(dealername)
    # cust_title = dealerSql.dealersql_Cust_title(str(dealername))
    # print(cust_title)
    # cc.dealerRolePower(cust_title)
    # #cc.dealerOfflogin()#退出登录



