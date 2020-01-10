# coding: utf-8
from selenium import webdriver
import uiautomator2 as ut2
import SendKeys as SendKeys
from xinyiqi.publicMothon import *

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
#双击
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
dr = webdriver.Firefox()
d = ut2.connect()
package_namesaler = 'winretailsaler.net.winchannel.wincrm'
package_namedealer = 'winretaildealer.net.winchannel.wincrm'
# 惠TV
class saler_tv():
    pool = public_month()
    def is_visible(self, locator, timeout=80):
        try:
            ui.WebDriverWait(dr, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
    def beneficial_TV(self,shipinname,yunname,cishu,quyuname,biaoti,neirong,weixinquanbiaoti,beishu,danmu,nicheng):
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
        jsl = 'document.getElementById("menuScrollAuto").scrollTop=1000'
        dr.execute_script(jsl)
        dr.find_element_by_link_text("品牌学院").click()
        dr.find_element_by_css_selector("#a_menuId_huitv").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[2]").click()
        dr.find_element_by_id("videoName").send_keys(shipinname)
        time.sleep(1)
        dr.find_element_by_css_selector("#videoCloudName").send_keys(yunname)
        dr.find_element_by_css_selector("#videoSort").send_keys(cishu)
        sel = dr.find_element_by_id("labelId")
        Select(sel).select_by_value('2')
        dr.find_element_by_css_selector("#areaName").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.switch_to.frame("modalDialog")
        time.sleep(1)
        dr.switch_to.frame("tree")
        time.sleep(1)
        dr.find_element_by_name("saleAreaName").send_keys(quyuname)
        dr.find_element_by_css_selector("#query_A").click()
        time.sleep(1)
        dr.find_element_by_xpath(".//*[@id='brandSaleArea_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_css_selector("div.MenuList>a:nth-child(2)").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(2)
        dr.find_element_by_css_selector("#startTime").click()
        time.sleep(1)
        dr.switch_to.default_content()
        time.sleep(1)
        # dr.switch_to.frame(dr.find_element_by_css_selector("div#_my97DP>iframe"))
        dr.switch_to.frame(dr.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(2)
        dr.find_element_by_css_selector("#dpTodayInput").click()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("#endTime").click()
        time.sleep(1)
        dr.switch_to.default_content()
        time.sleep(1)
        dr.switch_to.frame(dr.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(1)
        dr.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr[7]/td[6]").click()
        # eee = dr.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr[7]/td[6]")
        # ActionChains(dr).double_click(eee).perform()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.find_element_by_css_selector("#file").click()
        time.sleep(2)
        SendKeys.SendKeys(r"C:\Users\zhangke\Desktop\tupin\citroen-C4LshangshiTVC.mp4")
        time.sleep(2)
        SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        dr.find_element_by_css_selector(".list_add>tbody>tr:nth-child(10)>td:nth-child(2)>input:nth-child(3)").click()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.switch_to.frame("uploadIframe")
        time.sleep(1)
        dr.switch_to.frame("page_interface_frame")
        time.sleep(1)
        dr.find_element_by_css_selector("#mainfile").click()
        time.sleep(2)
        SendKeys.SendKeys(r"C:\Users\zhangke\Desktop\tupin\5.jpg")
        time.sleep(4)
        SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        dr.find_element_by_css_selector("div.MenuList>a").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("#shareFriendTitle").send_keys(biaoti)
        dr.find_element_by_css_selector("#shareContent").send_keys(neirong)
        dr.find_element_by_css_selector("#shareGroupTitle").send_keys(weixinquanbiaoti)
        dr.find_element_by_css_selector("#playMultiple").send_keys(beishu)
        dr.find_element_by_name("sysc").click()
        time.sleep(2)
        dr.find_element_by_css_selector("#save").click()
        time.sleep(2)
        if self.is_visible("html/body/form/div/div[1]/div/a[3]")==True:
            time.sleep(2)
            dr.find_element_by_name("videoName").send_keys(shipinname)
            dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[3]").click()
        else:
            self.pool.sss("(false)云平台上传惠TV短视频失败")
            pass
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[4]").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)
        d.app_start(package_namesaler)
        if d(text=u"有权查看使用情况的应用").wait(timeout=3.0):
            d.press("back")
        else:
            pass
        if d(resourceId="winretailsaler.net.winchannel.wincrm:id/dlg_cmmn_alertIV").wait(timeout=3.0):
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").click()
            time.sleep(1)
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview",
              text=u"惠TV").click_exists(timeout=10.0)
        else:
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠TV").click()
        time.sleep(4)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/video_name_tv", text=shipinname).click_exists(
            timeout=4.0)  # 这个名字要改成变量
        time.sleep(1)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_commentary").set_text(danmu)  # 弹幕
        time.sleep(2)
        d(className="com.tencent.liteav.txcvodplayer.h").click()
        time.sleep(2)
        d.click(0.928, 0.301)
        self.pool.sss("(true)惠TV全屏成功")
        d.press("back")
        time.sleep(2)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_send_commentary").click_exists(timeout=3.0)
        time.sleep(2)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_update_name").click()
        time.sleep(1)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/edtInput").set_text(nicheng)  # 昵称
        time.sleep(1)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/dialog_sure").click()
        time.sleep(3)
        zi = d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_video_play_total_num").info.get("text")[0:1]
        time.sleep(1)
        zan = d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_video_like_num").info.get("text")
        time.sleep(2)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_like").click()
        time.sleep(1)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_share").click()
        time.sleep(2)
        d(text=u"微信好友").click()
        time.sleep(2)
        if d(resourceId="com.tencent.mm:id/kh", text=u"测试团队~新").exists:
            d(resourceId="com.tencent.mm:id/kh", text=u"测试团队~新").click_exists(timeout=2.0)
            self.pool.sss("(true)惠TV分享微信成功")
        else:
            self.pool.sss("(false)惠TV分享微信失败")
            pass
        d(resourceId="com.tencent.mm:id/alo").click_exists(timeout=1.0)
        d(resourceId="com.tencent.mm:id/aln").click_exists(timeout=1.0)
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.swipe(234, 600, 234, 1700)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/video_name_tv", text=shipinname).click_exists(
            timeout=4.0)  # 名字变量改
        time.sleep(2)
        zi1 = d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_video_play_total_num").info.get("text")[0:1]
        time.sleep(1)
        if int(zi) + 1 == int(zi1):
            self.pool.sss("(true)惠TV播放次数增加成功")
        else:
            self.pool.sss("(false)惠TV播放次数增加失败")
            pass
        zan1 = d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_video_like_num").info.get("text")
        if int(zan) + 1 == int(zan1):
            self.pool.sss("(true)惠TV点赞增加成功")
        else:
            self.pool.sss("(false)惠TV点赞增加失败")
            pass
        time.sleep(2)
        d.press("back")
        time.sleep(1)
        d.press("back")
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("menu1")
        dr.find_element_by_css_selector("#a_menuId_video_audit").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(2)
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[3]").click()
        time.sleep(2)
        mig = dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr[1]/td[5]").text
        if mig == danmu:
            self.pool.sss("(true)惠TV发送弹幕和云平台效验弹幕成功")
        else:
            self.pool.sss("(false)惠TV发送弹幕和云平台效验弹幕失败")
            pass
        time.sleep(2)

        dr.switch_to.default_content()
        dr.switch_to.frame("menu1")
        dr.find_element_by_css_selector("#a_menuId_dealertv").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_name("videoName").send_keys(shipinname)
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[3]").click()
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[4]").click()
        time.sleep(2)
        dr.switch_to.alert.accept()
        time.sleep(2)

        d.app_start(package_namedealer)
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview").click_exists(timeout=3.0)
        time.sleep(2)
        for i in range(2):
            d.swipe(234, 1650, 234, 420)
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
          instance=2).click()
        time.sleep(2)
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/video_icon_play").click_exists(timeout=3.0)
        time.sleep(2)
        ui = d(resourceId="winretaildealer.net.winchannel.wincrm:id/video_play_total_num").info.get("text")[0:1]
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/video_share_btn").click()
        d(text=u"微信好友").click()
        time.sleep(1)
        if d(resourceId="com.tencent.mm:id/kh", text=u"测试团队~新").exists:
            d(resourceId="com.tencent.mm:id/kh", text=u"测试团队~新").click_exists(timeout=2.0)
            self.pool.sss("(true)经销商惠TV分享微信成功")
        else:
            self.pool.sss("(false)经销商惠TV分享微信失败")
            pass
        d(resourceId="com.tencent.mm:id/alo").click_exists(timeout=1.0)
        d(resourceId="com.tencent.mm:id/aln").click_exists(timeout=1.0)
        time.sleep(2)
        d.press("back")
        time.sleep(2)
        d.swipe(234, 600, 234, 1700)
        time.sleep(2)
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/video_icon_play").click_exists(timeout=3.0)
        time.sleep(2)
        ui1 = d(resourceId="winretaildealer.net.winchannel.wincrm:id/video_play_total_num").info.get("text")[0:1]
        time.sleep(1)
        if int(ui) + 1 == int(ui1):
            self.pool.sss("(true)经销商惠TV播放次数增加成功")
        else:
            self.pool.sss("(false)经销商惠TV播放次数增加失败")
            pass
        time.sleep(1)
        d.press("back")
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_css_selector(".cancel").click()
        time.sleep(2)
        dr.switch_to.alert.accept()
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[3]/center/a[2]/img").click()
        time.sleep(2)
        dr.switch_to.alert.accept()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("menu1")
        time.sleep(2)
        dr.find_element_by_css_selector("#a_menuId_huitv").click()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(2)
        dr.find_element_by_name("videoName").send_keys(shipinname)
        dr.find_element_by_xpath("html/body/form/div/div[1]/div/a[3]").click()
        dr.find_element_by_name("videoId").click()
        dr.find_element_by_css_selector(".cancel").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[3]/center/a[2]/img").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(2)
        dr.quit()
if __name__ == '__main__':
    sdTV = saler_tv()
    sdTV.beneficial_TV(u"春眠不觉晓", u"不止往来", u"0", u"汉东", u"美的电视", u"好啦好啦", u"看看吧挺好的", u"1", u"艾欧尼亚", "历史")



