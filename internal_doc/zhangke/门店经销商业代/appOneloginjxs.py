# coding: utf-8
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import atx
from publicMothon import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#经销商第一次登录的合同校验

package_namedealer = 'winretaildealer.net.winchannel.wincrm'

#执行该条用例需要修改main方法中的mobile属性值
class dealer_appOneloginjxsTest():
    calling = public_month()

    #初始化atx
    def __init__(self):
        self.browser =webdriver.Firefox()
        self.d =atx.connect()
    #后台新增账号
    #url,name,pwd
    #信息：名称，姓名,手机号，密码，手续费，最小起订金额,联系电话,地址,经度,维度,经销商类型
    def oneLogin_dealer(self,url,loginname,loginpwd,poiName,nickName,mobile,password,rate,minOrderAmount,telephone,address,
                        longitude, latitude, dealerSourceType, provinceName, villageName):
        #网页新增经销商
        self.browser.get(url)  # 输入url
        self.browser.maximize_window()  # 最大化
        self.browser.find_element_by_css_selector("#userAccount").send_keys(loginname)  # 输入账号
        self.browser.find_element_by_css_selector(".login_pwd").send_keys(loginpwd)  # 输入密码
        self.browser.implicitly_wait(5)  # 等待时间
        self.browser.find_element_by_css_selector(".login_on").click()  # 登陆按钮
        self.browser.find_element_by_css_selector("#menuId_hxdplatform").click()
        self.browser.switch_to.frame('menu1')
        time.sleep(3)
        self.browser.find_element_by_css_selector(".promptHeader>a").click()
        self.browser.find_element_by_id("menuGroup_jxsglnew").click()
        self.browser.find_element_by_id("a_menuId_jxsxxglnew").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_css_selector("a[href='/crmPoiInfo/crmPoiInfoAction.do?method=toAddDealer']").click()
        self.browser.find_element_by_id("poiName").send_keys(poiName)
        self.browser.find_element_by_id("nickName").send_keys(nickName)
        self.browser.find_element_by_id("mobile").send_keys(mobile)
        self.browser.find_element_by_id("password").send_keys(password)
        self.browser.find_element_by_id("rate").send_keys(rate)
        self.browser.find_element_by_id("minOrderAmount").send_keys(minOrderAmount)
        self.browser.find_element_by_id("telephone").send_keys(telephone)
        self.browser.find_element_by_id("address").send_keys(address)
        self.browser.find_element_by_id("longitude").send_keys(longitude)
        self.browser.find_element_by_id("latitude").send_keys(latitude)
        jxslx = self.browser.find_element_by_id("dealerSourceType")
        Select(jxslx).select_by_value(dealerSourceType)
        self.browser.find_element_by_id("countyName").click()
        time.sleep(2)
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.switch_to.frame("tree")
        time.sleep(4)
        self.browser.find_element_by_name("provinceName").send_keys(provinceName)
        self.browser.find_element_by_name("villageName").send_keys(villageName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(3)
        self.browser.find_element_by_id("save").click()
        #手机端经销商登录
        self.d.start_app(package_namedealer)
        time.sleep(1)
        self.d(text=u"请输入手机号码").set_text(mobile)
        self.d(className="android.widget.EditText", instance=1).set_text(password)
        time.sleep(2)
        self.d.keyevent("BACK")
        time.sleep(2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").click()
        self.calling.ccc("(true)新建经销商登录成功")
        time.sleep(2)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").wait.exists():
            self.calling.ccc("(true)新建经销商合作协议成功")
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_submit").click()
        else:
            self.calling.ccc("(false)新建经销商合作协议失败")
            pass
        time.sleep(1)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").wait.exists():
            self.calling.ccc("(true)新建经销商垫付协议成功")
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_submit").click()
        else:
            self.calling.ccc("(true)新建经销商垫付协议失败")
            pass
        time.sleep(1)
        self.d(text=u"营业执照全称").set_text(u"自动化测试营业执照")
        time.sleep(1)
        self.d(text=u"请填写").set_text(u"自动化测试法定代表人")
        time.sleep(1)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/open_bank_city").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_city").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/open_bank_info").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bank_info").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_branch_bank").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bank_info").click()

        self.d(text=u"银行卡卡号").set_text(u"1234567890212111")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/representativeSameBT").click()
        self.d(text=u"请填写").set_text(u"3")
        time.sleep(2)
        self.d(text=u"请填写").set_text(u"3")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_submit").click()
        time.sleep(2)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").wait.exists():
            self.calling.ccc("(true)新建经销商服务承诺成功")
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_submit").click()
        else:
            self.calling.ccc("(true)新建经销商服务承诺失败")
            pass
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").wait.exists():
            self.calling.ccc("(true)新建经销商登录进入APP首页成功")
        else:
            self.calling.ccc("(true)新建经销商登录进入APP首页失败")
            pass
        time.sleep(1)
        self.d.keyevent("HOME")
if __name__ == '__main__':
    call = dealer_appOneloginjxsTest()
    call.oneLogin_dealer("http://retail.wincrm.net:8203/", "zhangkedealer", "11111111",
                         u"自动化测试", u"王斌", "14733945088", "aa248163", "0", "1", "15122674750",
                         u"打劣势交付落地时间发了多少积分收到了", "100.0", "40", u"普通经销商", u"汉西省", u"柏社村")
