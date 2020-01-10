#-*- coding: UTF-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from AppClass import winretailsr_IOS
from AppClass import winretailsaler_IOS
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
from excelManage_ios import excelInit_ios
from AppClass import Commonvariable
saler,dealer,sr,express,htv,pc = excelInit_ios.banbeninfo("retail",Commonvariable.EXCEL_EDITION)



def appsrActive_IOS():
    bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)

    bb.salerOffLogin(saler[4],saler[5])
    dd = winretailsr_IOS.appsrrInformation_IOS(Commonvariable.PORT)
    dd.srStartapp_ios(sr[4], sr[5])
    dd.srActive_ios(saler[44], saler[45], saler[46], saler[47], saler[48], saler[49])
    time.sleep(5)
    bb.salerRegister_IOS("业代激活", saler[44], saler[44], saler[44],saler[44])


# #激活
# dd = winretailsr_IOS.appsrrInformation_IOS("http://localhost:8100")
# dd.srStartapp_ios("14778785560","123456")
# dd.srActive_ios("14778785573","激活名称","激活门店名称","激活的详细地址自动化","标准建筑","门牌号")
# time.sleep(5)
# bb = winretailsaler_IOS.appsalerInformation_IOS("http://localhost:8100")
# bb.salerRegister_IOS("业代激活","14778785573","14778785573","14778785573")


