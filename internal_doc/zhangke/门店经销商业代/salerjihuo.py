# coding=utf8
# from publicMothon import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
package_namesr = 'winretailsr.net.winchannel.wincrm'
package_namesaler = 'winretailsaler.net.winchannel.wincrm'
class activated():
    #门店激活
    # ment = public_month()
    def __init__(self):
        self.dr = webdriver.Firefox()
        # self.d = atx.connect()
    def salerSr(self,phonesaler,phonename,salercheng,xiangdizhi,biaozhi,hao,yaoma):
        self.d(text=u"ATX助手").click()
        # time.sleep(2)
        self.d(text=u"输入法设置").click()
        # time.sleep(2)
        self.d(resourceId="android:id/summary").click()
        self.d(resourceId="vivo:id/radio").click()
        # time.sleep(1)
        self.d.keyevent("BACK")
        self.d.keyevent("BACK")
        # time.sleep(2)
        self.d.start_app(package_namesr)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的门店").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=6).click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_phone_search").set_text(phonesaler)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_creat").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_username").set_text(phonename)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_store_name").set_text(salercheng)
        time.sleep(2)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_store_type").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_select_region").click()
        self.d(text=u"北京市").click()
        self.d(text=u"北京市").click()
        self.d(text=u"海淀区").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_areaname").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_areaname").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_store_address").set_text(xiangdizhi)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_sign_building").set_text(biaozhi)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_house_num").set_text(hao)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_counter_quantity").click()
        time.sleep(2)
        for i in range(2):
            self.d.swipe(500, 1800, 500, 1600)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_phone_search").set_text(phonesaler)
        oop = self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_store_phone").text
        if oop == phonesaler:
            self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_store_phone").click()
        else:
            self.ment.ttt("(false)没有找到要激活的门店")
            pass
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/iv_store_photo").click()
        time.sleep(2)
        self.d(resourceId="com.android.attachcamera:id/shutter_button").click()
        self.d(resourceId="com.android.attachcamera:id/done_button").click()
        self.d(text=u"确定").click()
        time.sleep(3)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/btn_submit").click()
        time.sleep(2)
        self.d.keyevent("BACK")
        self.d.stop_app(package_namesr)
        time.sleep(2)
        self.d.start_app(package_namesaler)
        self.d(text=u"业代激活").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone").set_text(phonesaler)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_obtain_verify_code").click()
        time.sleep(3)
        quyan = self.ment.databaseSrJiHuo(phonesaler)
        time.sleep(1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_verify_code").set_text(quyan)
        time.sleep(1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_go_invoke_store").click()
        time.sleep(1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_invoke_invoke").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone_num").set_text(yaoma)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_go_invoke_store").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_salesChannel").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_salesCheckoutNum").click()
        time.sleep(2)
        for i in range(2):
            self.d.swipe(500, 1800, 500, 1600)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(3)
        if self.d(text=u"有权查看使用情况的应用").wait.exists():
            self.d.keyevent("BACK")
        else:
            pass
        time.sleep(2)
        if self.d(text=u"优惠下单").wait.exists():
            self.ment.ttt("(true)业代替注册门店激活成功")
        else:
            self.ment.ttt("(false)业代替注册门店激活失败")
            pass
        time.sleep(2)
        #删除im号
        # self.ment.database(phonesaler)
        self.d.stop_app(package_namesaler, clear=True)
        time.sleep(2)
        self.d.start_app(package_namesr)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的门店").click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=6).click()
        time.sleep(1)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/et_phone_search").set_text(phonesaler)
        time.sleep(1)
        if self.d(text=u"已激活").wait.exists():
            self.ment.ttt("(true)业代替注册门店激活在业代确认激活成功")
        else:
            self.ment.ttt("(false)业代替注册门店激活在业代确认激活失败")
        time.sleep(1)
        self.d.keyevent("BACK")
        time.sleep(2)
        self.d.keyevent("HOME")
        time.sleep(2)
        self.d(text=u"ATX助手").click()
        time.sleep(2)
        self.d(text=u"输入法设置").click()
        time.sleep(2)
        self.d(resourceId="android:id/summary").click()
        self.d(resourceId="vivo:id/radio", className="android.widget.RadioButton", instance=2).click()
        time.sleep(1)
        self.d.keyevent("BACK")
        self.d.keyevent("BACK")
        self.d(text=u"惠下单业代").click()
        time.sleep(2)
        self.d.keyevent("BACK")
        time.sleep(1)
        self.d.keyevent("BACK")
        time.sleep(1)
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=3).click()
        self.d(resourceId="winretailsr.net.winchannel.wincrm:id/search_editview").set_text(salercheng)
        time.sleep(2)
        self.d.click(0.943, 0.957)
        time.sleep(1)
        mml = self.d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_store_name").text
        ooos = mml.encode("utf-8")
        if ooos == salercheng:
            self.ment.ttt("(true)业代替注册门店激活之后在我的装机看正常")
        else:
            self.ment.ttt("(false)业代替注册门店激活之后在我的装机看失败")
        time.sleep(2)
        self.d.stop_app(package_namesr)
        time.sleep(1)
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
        self.dr.find_element_by_id("mobile").send_keys(phonesaler)
        self.dr.find_element_by_css_selector("#query_A").click()
        yes = self.dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[21]").text
        if yes == yaoma:
            self.ment.ttt("(true)门店激活类型查看业代邀请码成功")
        else:
            self.ment.ttt("(false)门店激活类型查看业代邀请码失败")
            pass
        self.dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[3]/center/a[2]/img").click()
        time.sleep(2)
        mumst = self.dr.find_element_by_id("longitude")
        zzsmb = mumst.get_attribute("value")
        ttslf = float(zzsmb)
        if ttslf != 0.00000001:
            self.ment.ttt("(true)业代替注册门店激活账号经度上传成功")
        else:
            self.ment.ttt("(false)业代替注册门店激活账号经度上传失败")
        nunsn = self.dr.find_element_by_id("latitude")
        llssn = nunsn.get_attribute("value")
        yyssn = float(llssn)
        if yyssn != 0.00000001:
            self.ment.ttt("(true)业代替注册门店激活账号纬度上传成功")
        else:
            self.ment.ttt("(false)业代替注册门店激活账号纬度上传失败")
        time.sleep(2)
        self.dr.quit()
if __name__ == '__main__':
    # 门店激活
    generation = activated()
    generation.salerSr("14044479911", "滇虹", "天时地利人和店", "雪山之上无极之巅", "悟道大厦北100", "京冀蓝光-009", "14088745623")
