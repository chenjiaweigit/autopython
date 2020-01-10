# coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest

# import datetime
# starttime = datetime.datetime.now()
# print "request start time %s" % starttime
import threading
# import uiautomator2 as ut2
# d = ut2.connect()
# sss = d.device_info
# print type(sss)
o = threading.Lock()#引入锁
def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))
class test(threading.Thread):
    def __init__(self, people,name):
        threading.Thread.__init__(self)
        self.people = people
        self.Threadname = name
    def run(self):
        o.acquire()#加锁
        print("开始线程: " + self.Threadname)
        chiHuoGuo(self.people)
        print("结束线程: " + self.name)
        o.release()#释放锁
    print("yoyo请小伙伴开始吃火锅：！！！")
if __name__ == '__main__':
    t = test("呵呵","Thread-1")
    t2 = test("好好","Thread-2")
    t.setDaemon(True)
    t2.setDaemon(True)
    t.start()
    t2.start()
    t.join()
    t2.join()
    time.sleep(0.1)
    print("退出主线程：吃火锅结束，结账走人")

# def fun(num):
#     i = 1
#     s = 1
#     while i<=num:
#         s *=i
#         i+=1
#     return s
# ssss = fun(7)
# print ssss
#
# def fun1(num):
#     if num>1:
#         sss= num*fun1(num-1)
#     else:
#         sss = 1
#     return sss
# nn=fun1(7)
# print nn


# from selenium import webdriver
# import time,unittest
# import pymssql
# from selenium.webdriver.support import expected_conditions as EC
# import pymysql
# def salerInformation_898():
#     conn = pymssql.connect("118.186.244.9","wangbin","wb@HYTX.2017","CRM_RETAIL")
#     cursor = conn.cursor()
#     sqlname = "SELECT top 100 CRM_USER_REGISTER_LOG.LON,CRM_USER_REGISTER_LOG.LAT FROM CRM_WS_CUSTOMER WITH (nolock) INNER JOIN " \
#               "CRM_USER_REGISTER_LOG ON CRM_WS_CUSTOMER.CUSTOMER_ID = CRM_USER_REGISTER_LOG.CUSTOMER_ID WHERE " \
#               "CRM_WS_CUSTOMER.MOBILE = '14778786568' ORDER BY CRM_USER_REGISTER_LOG.ID DESC "
#     print (cursor.execute(sqlname))
#     data = (cursor.fetchone())
#     print (data)
#     conn.close()
#     return data
# if __name__ == '__main__':
#     salerInformation_898()




# import base64
# s1 = base64.encodestring('8F, Block E, Dazhongsi Zhongkun Plaza, No. A18 West Beisanhuan Road, Haidian District, Beijing')
# s2 = base64.decodestring(s1)
# print s1, s2




