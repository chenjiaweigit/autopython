# coding: utf-8
import atx
import unittest
from publicMothon import *
import time
package_namesaler = 'winretailsaler.net.winchannel.wincrm'
package_namedealer = 'winretaildealer.net.winchannel.wincrm'
package_namesr = 'winretailsr.net.winchannel.wincrm'
#登录
#初始化atx
class aler_loginTest(unittest.TestCase):
    demo = public_month()
    def setUp(self):
        self.d = atx.connect()
    #封装登录saler的方法
    def login_saler(self,username,password):
        self.d.start_app(package_namesaler)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        time.sleep(1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(username)
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(password)
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        time.sleep(2)
    def test_salerlogin1(self):
        #'''用户名、密码为空登录'''
        self.login_saler(" ", " ")
        self.demo.ccc("(true)门店用户名、密码为空登录")
    def runTest(self):
        pass
    def test_salerlogin2(self):
        #'''用户名正确,密码为空'''
        self.login_saler("14036958563", " ")
        self.demo.ccc("(true)门店用户名正确,密码为空")
    def test_salerlogin3(self):
        #用户名为空，密码正确
        self.login_saler(" ", "aa248163")
        self.demo.ccc("(true)门店用户名为空，密码正确")
    '''密码正确'''
    def test_salerlogin4(self):
       # '''用户est_sale名密码正确 '''
        self.login_saler("14036958563", "958563")
        self.demo.ccc("(true)门店用户名正确密码正确")
    @unittest.skip("我不想执行")
    def test_salerStopapp(self):
        # 清空登录信息
        self.d.stop_app(package_namesaler,clear =True)

class dealer_loginTest(unittest.TestCase):
    demo1 = public_month()
    def setUp(self):
        self.d = atx.connect()
    def login_dealer(self,username,password):
        self.d.start_app(package_namedealer)
        time.sleep(1)
        a = self.d(className="android.widget.EditText")
        a[0].set_text(username)
        time.sleep(2)
        a[1].set_text(password)
        time.sleep(2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").click()
        time.sleep(2)
    def test_dealerlogin1(self):
        #'''用户名、密码为空登录'''
        self.login_dealer(" ", " ")
        self.demo1.ccc("(true)经销商用户名、密码为空登录")

    def test_dealerlogin2(self):
        #'''用户名正确,密码为空'''
        self.login_dealer("14019117419", "")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        self.demo1.ccc("(true)经销商用户名正确,密码为空")

    def test_dealerlogin3(self):
        #用户名为空，密码正确
        self.login_dealer(" ", "117419")
        self.demo1.ccc("(true)经销商用户名为空，密码正确")

    def test_dealerlogin4(self):
       # '''用户名密码正确 '''
        self.login_dealer("14019117419", "117419")
        self.demo1.ccc("(true)经销商用户名密码正确")
    @unittest.skip("skip")
    def test_dealerStopapp(self):
        #清空登录信息
        self.d.stop_app(package_namedealer, clear=True)
class sr_loginTest(unittest.TestCase):
    demo2 = public_month()
    def setUp(self):
        self.d = atx.connect()
    #封装登录sr的方法
    def login_sr(self,username,password):
        self.d.start_app(package_namesr)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_username").set_text(username)
        time.sleep(2)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_pwd").set_text(password)
        time.sleep(2)
        if self.d(resourceId="com.huawei.secime:id/char_keyboard_hide_btn").wait.exists():
            self.d(resourceId="com.huawei.secime:id/char_keyboard_hide_btn").click()
        else:
            pass
        time.sleep(2)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/btn_login").click()
        time.sleep(2)
    def test_srlogin1(self):
        # '''用户名、密码为空登录'''
        self.login_sr(" ", " ")
        self.demo2.ccc("(true)业代用户名、密码为空登录")
    def test_srlogin2(self):
        # '''用户名正确,密码为空'''
        self.login_sr("14022996352", " ")
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        self.demo2.ccc("(true)业代用户名正确,密码为空")
    def test_srlogin3(self):
        # 用户名为空，密码正确
        self.login_sr(" ", "aa248163")
        self.demo2.ccc("(true)业代用户名为空，密码正确")
    def test_srlogin4(self):
        # '''用户名密码正确 '''
        self.login_sr("14088745623", "123456")
        self.demo2.ccc("(true)业代用户名密码正确")
    @unittest.skip("skip")
    def test_srStopapp(self):
        # 清空登录信息
        self.d.stop_app(package_namesr, clear=True)

if __name__ == '__main__':
    unittest.main()
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(aler_loginTest("test_salerlogin1"))
    # testsuite.addTest(aler_loginTest("test_salerlogin2"))
    # testsuite.addTest(aler_loginTest("test_salerlogin3"))
    # testsuite.addTest(aler_loginTest("test_salerlogin4"))
    # testsuite.addTest(dealer_loginTest("test_dealerlogin1"))
    # testsuite.addTest(dealer_loginTest("test_dealerlogin2"))
    # testsuite.addTest(dealer_loginTest("test_dealerlogin3"))
    # testsuite.addTest(dealer_loginTest("test_dealerlogin4"))
    # testsuite.addTest(sr_loginTest("test_srlogin1"))
    # testsuite.addTest(sr_loginTest("test_srlogin2"))
    # testsuite.addTest(sr_loginTest("test_srlogin3"))
    # testsuite.addTest(sr_loginTest("test_srlogin4"))
    # runner = unittest.TextTestRunner()
    # runner.run(testsuite)






