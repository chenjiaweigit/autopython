#coding=utf-8
from appsaler import appsalerInformation
from wangye import wangyeInfomation
from dateCheck import checkDate
from datetime import datetime
from time import strftime, localtime
import time
#门店默认经销商
if __name__ == '__main__':
            aa = appsalerInformation()
            #uat
            #retail:14778786568 aa248163
            tuplesaler1 = aa.appsalerjxs("14778786568","aa248163")
            print (tuplesaler1)
            bb = wangyeInfomation()
        #uat:"http://uat.wincrm.net:8218","winretailsaler","win!@#"
        #retail:"http://retail.wincrm.net:8203","wangbinsaler","71028863"
            bb.wangyeLogin("http://retail.wincrm.net:8203","wangbinsaler","71028863")
            bb.wangyeSalerdefaultdealer(tuplesaler1[0])
            bb.wangyeQuit()
            tuplesaler2 =aa.appsalerjxs("14778786568","aa248163")
            print (tuplesaler2)
            log = open('E://banben.txt', 'a+')
            log.write('\n'+"(true)----版本--门店默认经销商---"+
                      time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
            log.close()
            log = open('E://banben.txt', 'a+')
            log.write('\n'+"(结束)----版本--门店默认经销商结束---"+
                      time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
            log.close()


