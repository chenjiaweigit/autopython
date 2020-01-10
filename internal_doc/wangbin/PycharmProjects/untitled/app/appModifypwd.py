# coding: utf-8
import time
import datetime
from appsaler import appsalerInformation
from appdealer import appdealerInformation
from pymssqlManage import excelManager
# saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("uat",r"D:\excel\banben.xls")

#修改密码,顺时操作，第一次登录必须成功,测试的时候修改密码来控制
if __name__ == '__main__':
    # salerretail:"14778786568","aa248163"
    #dealerretail:14778786566,aa248163
    starttime = datetime.datetime.now()

    aa =appsalerInformation("172.18.200.192:7912")
    bb = appdealerInformation("172.18.200.192:7912")

    aa.start_app()
    dengluinfromatin = aa .salerlogintrue(int(saler[30]),int(saler[31]))
    print (dengluinfromatin)
    modifypwd = aa.salermodifypwd(dengluinfromatin[1],str(dengluinfromatin[1])+"new")
    print (modifypwd)
    aa.salerlogintrue(dengluinfromatin[0],modifypwd[1])
    # aa.appscreenshot()
    aa.salerLog_banben(dealer[6],dealer[19])


    bb.dealerstart_app()
    bb.dealerlogin(int(saler[32]),int(saler[33]))
    old_pws, pwd1, pwd2 =bb.dealerModifypwd(int(saler[33]),str(int(saler[33]))+"new",str(int(saler[33]))+"new")
    bb.dealerlogin(int(saler[32]),pwd2)
    bb.dealerLog_banben(dealer[6],dealer[20])
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)


