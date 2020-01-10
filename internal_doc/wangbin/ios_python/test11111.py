# -*- coding: UTF-8 -*-

from Tkinter import *
from tkMessageBox import *
import urllib
import urllib2
import time
import json
import os, sys, string, socket
from array import *
import atx

reload(sys)
sys.setdefaultencoding('utf-8')
d=atx.connect("http://localhost:8100")

def startupapp():
    d.start_app('winretailsaler.net.winchannel.wincrm')
    # d.start_app('com.winchannel.winretailsaler')#生产包
    image = d.screenshot()  # 返回图片
    image.save("screen.png")
    time.sleep(10)
    # 如果不是新安装的启动没有问答框
    if "允许“惠下单”" in d.session.alert.text:
        d.session.alert.accept()
    else:
        pass
        time.sleep(3)
    if "允许“惠下单”" in d.session.alert.text:
        d.session.alert.accept()
    else:
        pass
        time.sleep(3)
    if "允许“惠下单”" in d.session.alert.text:
        d.session.alert.accept()
    else:
        pass
        time.sleep(3)
    if "允许“惠下单”" in d.session.alert.text:
        d.session.alert.accept()
    else:
        pass
    time.sleep(5)

    pass

def downloadapp():
    downloadurlfile = "http://192.168.60.239:8080/ios_build_ver.txt"
    urllib.urlretrieve(downloadurlfile, "/Users/wangbin/Desktop/ios_build_ver.txt")
    time.sleep(2)
    fo = open("/Users/wangbin/Desktop/ios_build_ver.txt", "r")
    filecontent = fo.read()
    json_to_python = json.loads(filecontent)
    fo.close()
    url = json_to_python['iOS-WinretailSaler_rel']
    print "downloading ipa  " + url
    print(os.getcwd())
    # os.chdir('/Users/chenguoshuang/Desktop/autotest')#切换文件夹
    urllib.urlretrieve(url, "/Users/wangbin/Desktop/winretailsaler.ipa")
    time.sleep(5)
    pass
#
def installapp():
    command = "./transporter_chief.rb" + " " + "/Users/wangbin/Desktop/winretailsaler.ipa"
    os.system(command) #安装ipa
    os._exit(0)
    pass

# downloadapp()
# downloadapp()
# # d.session.alert.accept()
if "惠下单"in d.session.alert.text:
    d.session.alert.accept()

