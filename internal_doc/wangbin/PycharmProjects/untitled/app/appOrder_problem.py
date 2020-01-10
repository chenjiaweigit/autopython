# coding: utf-8
from wangye import wangyeInfomation
from appsaler import appsalerInformation
from appdealer import appdealerInformation
import time

if __name__ == '__main__':#(需要重写)
    #uat:"http://uat.wincrm.net:8218/","winretailsaler","win!@#"
    #retail:"http://retail.wincrm.net:8218/","wangbinsaler","71028863"
    # aa = wangyeInfomation()
    bb = appsalerInformation()
    cc = appdealerInformation()
    # aa.wangyeLogin("http://retail.wincrm.net:8203/","wangbinsaler","71028863")
    # aa.wangyeSwipetodown()
    # name = aa.wangyeOrder_problem_salerleixing(u"新自动化1","400","10","5","1")
    # aa.wangeyqiehuaniframe("menu1")
    # # #######uat:"//iframe[@src='http://uat.wincrm.net:8218/widgets/My97DatePicker/My97DatePicker.htm']",retail:"//iframe[@src='http://retail.wincrm.net:8203/widgets/My97DatePicker/My97DatePicker.htm']"
    # aa.wangyeOrder_problem_Setarea(name,name,u"汉西省",name,"//iframe[@src='http://retail.wincrm.net:8203/widgets/My97DatePicker/My97DatePicker.htm']"
    #                                ,"//iframe[@src='http://retail.wincrm.net:8203/widgets/My97DatePicker/My97DatePicker.htm']","500")
    bb.start_app()
    # bb.salerlogintrue("14778786561","aa248163")

    tv_exception1,tv_exception2,tv_exception3,ordercode = bb.salerOrder_problem1("50","50","49")
    # print (tv_exception1)
    # print (tv_exception2)
    # print (tv_exception3)
    # print (ordercode)
    # cc.dealerstart_app()
    # result = cc.dealerAlterorder()#修改订单
    # aa.wangeyqiehuaniframe("menu1")
    # aa.wangyeOrderproblem_look(ordercode,"ab")#
    # aa.wangeyqiehuaniframe("menu1")
    # aa.wangyeOrderproblem_X(name)
    # if  "待审核" in tv_exception1 and "待审核"  not in tv_exception2 and result == False:
    #     log = open('E://banben.txt', 'a+')
    #     log.write(
    #         '\n' + "（true）------版本--异常订单校验:"   "------" +str(list[0])  + "------" + time.strftime(
    #             "%Y-%m-%d %H:%M:%S",
    #             time.localtime()) + '\n')
    #     log.close()
    # else:
    #     log = open('E://banben.txt', 'a+')
    #     log.write(
    #         '\n' + "（flase）------版本--异常订单校验:"   "------" +str(list[0])  + "------" + time.strftime(
    #             "%Y-%m-%d %H:%M:%S",
    #             time.localtime()) + '\n')
    #     log.close()
