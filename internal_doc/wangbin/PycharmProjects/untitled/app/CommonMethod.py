# coding: utf-8
import datetime

def Ttime():
    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)
    pass


if __name__ == '__main__':
    Ttime()
