# coding: utf-8
from selenium import webdriver
import uiautomator2 as ut2
import SendKeys as SendKeys
from publicMothon import *
#等待元素出现
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

#双击
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Firefox()
d = ut2.connect()
package_namesaler = 'winretailsaler.net.winchannel.wincrm'
class short_Video():
    look = public_month()
    def demo_visible(self, locator, timeout=80):
        try:
            ui.WebDriverWait(dr, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
    def video_Clips(self, videoname, qqyunname, bonum, videtheir, searched, biaot, duannr, wxqname, beishudemo):
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
        dr.find_element_by_css_selector("#a_menuId_shortTV").click()
        time.sleep(2)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
        dr.find_element_by_css_selector(".MenuList>a:nth-child(1)").click()
        dr.find_element_by_css_selector("#videoName").send_keys(videoname)
        dr.find_element_by_css_selector("#videoCloudName").send_keys(qqyunname)
        dr.find_element_by_css_selector("#playTimes").clear()
        dr.find_element_by_css_selector("#playTimes").send_keys(bonum)
        dr.find_element_by_css_selector("#videoSort").send_keys(videtheir)
        time.sleep(2)
        dr.find_element_by_css_selector("#areaName").click()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.switch_to.frame("modalDialog")
        dr.switch_to.frame("tree")
        time.sleep(1)
        dr.find_element_by_name("saleAreaName").send_keys(searched)
        dr.find_element_by_css_selector("#query_A").click()
        dr.find_element_by_xpath(".//*[@id='brandSaleArea_table']/tbody/tr/td[1]/input").click()
        dr.find_element_by_css_selector("a[href='javascript:ok()']").click()
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        time.sleep(1)
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
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("#file").click()
        time.sleep(2)
        SendKeys.SendKeys(r"C:\Users\zhangke\Desktop\tupin\citroen-C4LshangshiTVC.mp4")
        time.sleep(2)
        SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        dr.find_element_by_css_selector(".list_add>tbody>tr:nth-child(9)>td:nth-child(2)>input:nth-child(3)").click()
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
        time.sleep(2)
        SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        dr.find_element_by_css_selector("div.MenuList>a").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)
        dr.switch_to.default_content()
        dr.switch_to.frame("main1")
        dr.find_element_by_css_selector("#shareFriendTitle").send_keys(biaot)
        dr.find_element_by_css_selector("#shareContent").send_keys(duannr)
        dr.find_element_by_css_selector("#shareGroupTitle").send_keys(wxqname)
        dr.find_element_by_css_selector("#playMultiple").send_keys(beishudemo)
        time.sleep(1)
        dr.find_element_by_css_selector("#save").click()
        time.sleep(2)
        if self.demo_visible(".//*[@id='searchbox']/table/tbody/tr/td[6]/input") == True:
            time.sleep(2)
            dr.find_element_by_name("videoName").send_keys(videoname)
            time.sleep(1)
            dr.find_element_by_css_selector(".MenuList>a:nth-child(2)").click()
        else:
            self.look.yyy("(false)云平台上传惠TV短视频成功失败待确认")
            pass
        time.sleep(2)
        dr.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[1]/input").click()
        time.sleep(2)
        dr.find_element_by_css_selector(".MenuList>a:nth-child(3)").click()
        time.sleep(1)
        dr.switch_to.alert.accept()
        time.sleep(1)


if __name__ == '__main__':
    ppo = short_Video()
    ppo.video_Clips(u"冬至来临", u"冬暖夏凉", u"1", u"0", u"汉东", u"短视频赞", u"好看的视频", u"倚天屠龙",u"1")
