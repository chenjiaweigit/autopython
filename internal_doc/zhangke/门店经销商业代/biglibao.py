# coding: utf-8
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from publicMothon import *

package_namesaler = 'winretailsaler.net.winchannel.wincrm'
package_namesr = 'winretailsr.net.winchannel.wincrm'
dr = webdriver.Firefox()
d = atx.connect()
# 大礼包
class big_GigLiBao():
    demo = public_month()
    def gift_Packs(self,libaoname,libaobiaoqian,youhuishuoming,libaomingcheng,quyu,phones,pws):
        dr.implicitly_wait(10)
        url = "http://retail.wincrm.net:8203/"
        dr.get(url)
        dr.find_element_by_css_selector("#userAccount").send_keys("zhangkesaler")
        dr.find_element_by_css_selector("input.login_pwd").send_keys("11111111")
        dr.find_element_by_css_selector("li.login_on>a").click()
        dr.find_element_by_css_selector("#menuId_hxdplatform").click()
        dr.switch_to.frame("menu1")
        time.sleep(2)
        dr.maximize_window()
        dr.find_element_by_css_selector("div.promptHeader>a").click()
        time.sleep(2)
        for i in range(1, 5):
            dr.find_element_by_xpath(".//*[@id='menuScrollAuto']").send_keys(Keys.DOWN)
        dr.find_element_by_link_text("促销管理").click()
        dr.find_element_by_css_selector("#a_menuId_yhqmbgl").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("div.MenuList>a:nth-child(3)").click()
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='titleId']").send_keys(libaoname)
        time.sleep(2)
        # 仅限移动支付
        sel = dr.find_element_by_xpath(".//*[@id='SollAuto']/div/table/tbody/tr[3]/td[2]/select")
        Select(sel).select_by_value('2')
        time.sleep(1)
        # 订单
        sel = dr.find_element_by_id("couponConditionType")
        Select(sel).select_by_value('1')
        dr.find_element_by_xpath(".//*[@id='couponLabel']").send_keys(libaobiaoqian)
        dr.find_element_by_css_selector("#memoId").send_keys(youhuishuoming)
        for i in range(1, 6):
            dr.find_element_by_css_selector("div.sheet_div").send_keys(Keys.DOWN)
        dr.find_element_by_css_selector("#priceId").send_keys(u"200")
        dr.find_element_by_css_selector("#scoreId").send_keys(u"10")
        time.sleep(1)
        dr.find_element_by_xpath(".//*[@id='s2id_brandCode']/a/span[2]/b").click()
        time.sleep(1)
        dr.find_element_by_css_selector("input#s2id_autogen2_search").send_keys(u"脉动")
        time.sleep(1)
        dr.find_element_by_css_selector("span.select2-match").click()
        dr.find_element_by_css_selector("#doModifyId").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a[2]").click()
        current_window = dr.current_window_handle  # 获取当前窗口handle name
        all_windows = dr.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                dr.switch_to.window(window)
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("_DialogFrame_0")
        dr.find_element_by_css_selector("input#cityName").click()
        time.sleep(2)
        dr.find_element_by_css_selector("input#cityName").send_keys(quyu)
        time.sleep(1)
        dr.find_element_by_xpath(".//*[@id='pc_table']/tbody/tr/td[1]/input").click()
        dr.switch_to.default_content()
        dr.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("menu1")
        dr.find_element_by_css_selector("#a_menuId_crmSpree").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[1]").click()
        dr.find_element_by_css_selector("#name").send_keys(libaomingcheng)
        dr.find_element_by_css_selector("#cityName").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.switch_to.frame("modalDialog")
        time.sleep(1)
        dr.switch_to.frame("tree")
        time.sleep(1)
        dr.find_element_by_name("saleAreaName").send_keys(quyu)
        dr.find_element_by_id("query_A").click()
        dr.find_element_by_xpath(".//*[@id='brandSaleArea_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[2]").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(2)
        dr.find_element_by_css_selector("#title").click()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.switch_to.frame("modalDialog")
        time.sleep(1)
        dr.switch_to.frame("tree")
        time.sleep(1)
        dr.find_element_by_name("title").send_keys(libaoname)
        dr.find_element_by_id("query_A").click()
        dr.find_element_by_xpath(".//*[@id='userCouponsCycle_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[2]").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("#couponValidity").send_keys(u"1")
        time.sleep(2)
        dr.find_element_by_css_selector("#startTime").click()
        dr.switch_to.default_content()
        time.sleep(1)
        dr.switch_to.frame(dr.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(2)
        dr.find_element_by_css_selector("#dpTodayInput").click()
        dr.switch_to.default_content()
        time.sleep(2)
        dr.switch_to.frame("main1")
        time.sleep(2)
        dr.find_element_by_css_selector("#endTime").click()
        time.sleep(1)
        dr.switch_to.default_content()
        time.sleep(1)
        dr.switch_to.frame(dr.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(1)
        qqq = dr.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr[6]/td[4]")
        ActionChains(dr).double_click(qqq).perform()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.find_element_by_css_selector("#save").click()
        time.sleep(2)
        d.start_app(package_namesaler)
        d(text=u"登录").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(phones)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(pws)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        if d(text=u"有权查看使用情况的应用").wait.exists():
            d.keyevent("BACK")
        else:
            pass
        time.sleep(2)
        if d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_main").wait.exists():
            nns = d(resourceId="winretailsaler.net.winchannel.wincrm:id/coupon_memo").text
            if nns == youhuishuoming:
                self.demo.uuu("(true)首页页面优惠券大礼包弹出来成功")
                d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").click
            else:
                self.demo.uuu("(false)首页页面优惠券大礼包没有弹出来失败")
                d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").click
        else:
            pass
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        d(text=u"优惠券").click()
        sss = d(description=u"春节快乐").description
        if sss == youhuishuoming:
            self.demo.uuu("(true)我的，优惠券，看大礼包成功")
        else:
            self.demo.uuu("(true)我的，优惠券，看大礼包失败")
        time.sleep(2)
        d.stop_app(package_namesaler, clear=True)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a[3]/img").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)
        dr.quit()
if __name__ == '__main__':
    # 大礼包
    demo1 = big_GigLiBao()
    demo1.gift_Packs(u"此卷勿动", u"天时地利", u"春节快乐", u"李白的包", u"汉西", "14036958563", "958563")
