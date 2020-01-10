# coding=utf8
from publicMothon import *
from selenium import webdriver
import atx
from selenium.webdriver.common.keys import Keys
package_namesr = 'winretailsr.net.winchannel.wincrm'
package_namesaler = 'winretailsaler.net.winchannel.wincrm'
class srYaoqing():
    demo = public_month()
    def __init__(self):
        self.dr = webdriver.Firefox()
        self.d = atx.connect()
    def  invitation(self,salerming,salerhao,namehao,srlerming,salerdizhi,salermenpai,salerjianzhu,yaoqing):
        self.d(text=u"ATX助手").click()
        time.sleep(2)
        self.d(text=u"输入法设置").click()
        time.sleep(2)
        self.d(resourceId="android:id/summary").click()
        self.d(resourceId="vivo:id/radio").click()
        time.sleep(1)
        self.d.keyevent("BACK")
        self.d.keyevent("BACK")
        self.d.start_app(package_namesr)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我是业代").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=3).click()
        time.sleep(2)
        if self.d(text=u"微信好友").wait.exists():
            self.demo.zzz("(true)邀请注册微信好友显示正确")
        else:
            self.demo.zzz("(false)邀请注册微信好友显示失败")
        if self.d(text=u"朋友圈").wait.exists():
            self.demo.zzz("(true)邀请注册朋友圈显示正确")
        else:
            self.demo.zzz("(false)邀请注册朋友圈显示失败")
        if self.d(text=u"短信").wait.exists():
            self.demo.zzz("(true)邀请注册短信显示正确")
        else:
            self.demo.zzz("(false)邀请注册短信显示失败")
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/ivWeChat").click()
        time.sleep(2)
        if self.d(text=u"明日风回更好").wait.exists():
            self.d(text=u"明日风回更好").click()
        else:
            self.demo.zzz("(false)微信寻找账号失败")
        time.sleep(1)
        self.d(resourceId="com.tencent.mm:id/alo").click()
        time.sleep(1)
        self.d(resourceId="com.tencent.mm:id/alo").click()
        time.sleep(1)
        if self.d(text=u"明日风回更好").wait.exists():
            self.d(text=u"明日风回更好").click()
        else:
            self.demo.zzz("(false)微信寻找账号失败")
        self.d(resourceId="com.tencent.mm:id/adv").click()
        self.d(resourceId="com.tencent.mm:id/alo").click()
        self.d.click(0.377, 0.602)
        self.d.type(salerming)
        self.d.click(0.409, 0.675)
        self.d.type(salerhao)
        self.d.click(0.799, 0.786)
        time.sleep(2)
        yanma = self.demo.databaseselect(salerhao)
        self.d.click(0.409, 0.863)
        self.d.type(yanma)
        self.d.click(0.505, 0.955)
        self.d.click(0.494, 0.595)
        self.d(resourceId="com.tencent.mm:id/akt").click()
        time.sleep(2)
        self.d(text=u"登录").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salerhao)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerhao)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_user_name").set_text(namehao)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_shop_name").set_text(srlerming)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_area").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname", text=u"马连洼街道办事处").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_street").set_text(salerdizhi)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_houseNum").set_text(salermenpai)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_land_mark").set_text(salerjianzhu)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_channel").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_checkstandNum").click()
        time.sleep(2)
        for i in range(2):
            self.d.swipe(500, 1800, 500, 1600)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/retail_add_img").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        if self.d(resourceId="android:id/button1").wait.exists():
            self.d(resourceId="android:id/button1").click()
        else:
            pass
        self.d(resourceId="com.android.attachcamera:id/shutter_button").click()
        self.d(resourceId="com.android.attachcamera:id/done_button").click()
        self.d(text=u"确定").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_invite_code_view").set_text(yaoqing)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(4)
        if self.d(text=u"有权查看使用情况的应用").wait.exists():
            self.d.keyevent("BACK")
        else:
            pass
        if self.d(text=u"优惠下单").wait.exists():
            self.demo.zzz("(true)业代邀请创建新门店账号进入首页成功")
        else:
            self.demo.zzz("(false)业代邀请新门店账号进入首页失败")
            pass
        time.sleep(1)
        self.demo.database(salerhao)
        time.sleep(1)
        self.d.stop_app(package_namesaler, clear=True)
        time.sleep(2)
        self.d.keyevent("BACK")
        time.sleep(2)
        self.d(resourceId="com.tencent.mm:id/aks").click()
        time.sleep(2)
        self.d.keyevent("BACK")
        time.sleep(1)
        self.d.keyevent("BACK")
        self.d.keyevent("BACK")
        self.d.stop_app(package_namesr)
        self.dr.implicitly_wait(10)
        url = "http://retail.wincrm.net:8203/"
        self.dr.get(url)
        self.dr.find_element_by_css_selector("#userAccount").send_keys("zhangkesaler")
        self.dr.find_element_by_css_selector("input.login_pwd").send_keys("11111111")
        self.dr.find_element_by_css_selector("li.login_on>a").click()
        self.dr.find_element_by_css_selector("#menuId_hxdplatform").click()
        self.dr.switch_to.frame("menu1")
        time.sleep(2)
        self.dr.maximize_window()
        self.dr.find_element_by_css_selector("div.promptHeader>a").click()
        time.sleep(2)
        for i in range(1, 5):
            self.dr.find_element_by_xpath(".//*[@id='menuScrollAuto']").send_keys(Keys.DOWN)
        self.dr.find_element_by_link_text("门店管理").click()
        self.dr.find_element_by_css_selector("#a_menuId_mdxxgl").click()
        time.sleep(2)
        self.dr.switch_to.default_content()
        self.dr.switch_to.frame("main1")
        self.dr.find_element_by_id("mobile").send_keys(salerhao)
        self.dr.find_element_by_css_selector("#query_A").click()
        ye = self.dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[21]").text
        if ye == yaoqing:
            self.demo.zzz("(true)门店查看业代邀请码成功")
        else:
            self.demo.zzz("(false)门店查看业代邀请码失败")
            pass
        self.dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[3]/center/a[2]/img").click()
        time.sleep(2)
        mums = self.dr.find_element_by_id("longitude")
        zzsm = mums.get_attribute("value")
        ttsl = float(zzsm)
        if ttsl != 0.00000001:
            self.demo.zzz("(true)业代邀请创建新门店账号经度上传成功")
        else:
            self.demo.zzz("(false)业代邀请创建新门店账号经度上传失败")
        nuns = self.dr.find_element_by_id("latitude")
        llss = nuns.get_attribute("value")
        yyss = float(llss)
        if yyss != 0.00000001:
            self.demo.zzz("(true)业代邀请创建新门店账号纬度上传成功")
        else:
            self.demo.zzz("(false)业代邀请创建新门店账号纬度上传失败")
        time.sleep(2)
        self.dr.quit()
        self.demo.yeDaizhuce(srlerming, srlerming)
if __name__ == '__main__':
    #收取不到验证码了  验证码在缓存中呢
    words = srYaoqing()
    words.invitation("支持原创哈哈哈", "14035511812", "任天行", "无可奈何花落去", "北上广北三十米往上五十米", "北上广-009", "无敌大转盘", "14036958563")





