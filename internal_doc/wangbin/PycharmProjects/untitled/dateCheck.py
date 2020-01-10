# coding: utf-8
import random
import atx
import os
import time
from datetime import datetime
from time import strftime, localtime
# import sys
from decimal import Decimal
# reload(sys)
# sys.setdefaultencoding('utf8')
#门店订单列表数据
#校验数据的通用方法：
# d =atx.connect()
#a 第一个值;b 第二个值；c 次数； d 时间 ; e  前面的string；  f  后面的string
def checkDate(a,b,c,d,e,f):
   if a==b:
      log = open('E://banben.txt', 'a+')
      log.write(
         '\n' +c + "   （ture）   " + e +"   "+a + "  =  " + f +"   "+ b + "   ---" + d + '\n')
      log.close()
   else:
      log = open('E://banben.txt', 'a+')
      log.write(
         '\n' +c + "   (false)  " + e +a + "  不=  " + f + b + "   ---" + d + '\n')
      log.close()

def checknull(a,b,c):
   if a !="":
      log = open('E://banben.txt', 'a+')
      log.write(
         '\n' +  "   （ture）   "+a  + b  + "-------"+c  + '\n')
      log.close()
   else:
      log = open('E://banben.txt', 'a+')
      log.write(
         '\n' +  "   （flase）   "+a  + b + "-------" + c  + '\n')
      log.close()

def change_shuliang():
   a = random.randint(1, 5)
   return a
def chage_jiage():
   a = random.random()
   b =round(a, 2)
   return b

# def huandong_Down():
#
#    for i in range(1,3):
#       d.swipe(300, 800, 300, 400)



# if __name__ == '__main__':









