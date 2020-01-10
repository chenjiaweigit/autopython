#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import wangye_IOS
from AppClass import winretaildealer_IOS
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)




def appJxsOneLogin_IOS():
    aa = wangye_IOS.wangyeInfomation()
    aa.wangyeLogin(saler[1], saler[2], saler[3])
    #
    # 经销商名称,姓名，账号，密码，经度，纬度，最小启动金额，联系电话，地址;查询省市,查询居委会，
    poiName, nickName, mobile, password, longitude, latitude, minOrderAmount, telephone, address, provinceName, villageName = \
        aa.dealerJxsOneLogin(saler[22], saler[23], saler[24], saler[25], saler[26], saler[27], saler[28],
                             saler[29], saler[30], saler[31], saler[32])
    cc = winretaildealer_IOS.appdealerInformation_IOS(Commonvariable.PORT)
    print(saler[24])
    cc.dealer_startapp_ios(saler[24], saler[25])
    cc.dealerjxsOnelogin_ios(saler[33], saler[34], saler[35], saler[36], saler[37])
    excelInit_ios.excelUpdate(saler[24])


# appJxsOneLogin_IOS()
# aa = wangye_IOS.wangyeInfomation()
# aa.wangyeLogin("http://retail.wincrm.net:8203","wangbinsaler","71028863")
# #
# #经销商名称,姓名，账号，密码，经度，纬度，最小启动金额，联系电话，地址;查询省市,查询居委会，
# poiName,nickName,mobile,password,longitude,latitude,minOrderAmount,telephone,address,provinceName,villageName = \
#     aa.dealerJxsOneLogin(u"新增自动化二",u"冬瓜荷叶茶二","14678786520","aa248163","100.0","40.0","1",
#                          "15122674750",u"加夫里什大家发了多少积分2",u"汉西",u"柏社村")
# cc = winretaildealer_IOS.appdealerInformation_IOS("http://localhost:8100")
# cc.dealer_startapp_ios(mobile,password)
# cc.dealerjxsOnelogin_ios(u"自动化工商",u"自动化法人","12345678910111213","10","10")
