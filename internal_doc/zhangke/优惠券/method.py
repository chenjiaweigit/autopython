# coding=utf8
import time

class public_method(object):
    def __init__(self, driver):
        self.driver = driver
    #设置区域
    def method_1(self):
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("_DialogFrame_0")
        self.driver.find_element_by_css_selector("input#cityName").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("input#cityName").send_keys(u"汉西")
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='pc_table']/tbody/tr/td[1]/input").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("main1")
        time.sleep(2)
    #批量发放
    def method_2(self):
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("_DialogFrame_0")
        self.driver.find_element_by_xpath(".//*[@id='searchbox']/table/tbody/tr/td[4]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='searchbox']/table/tbody/tr/td[4]/input").send_keys(u"14036958563")
        self.driver.find_element_by_css_selector("a#queryId").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bc_table']/tbody/tr/td[2]/input").click()
        self.driver.find_element_by_css_selector("input#startTime").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(1)
        self.driver.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr[2]/td[4]").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("_DialogFrame_0")
        time.sleep(1)
        self.driver.find_element_by_css_selector("input#overTime").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(".//*[@id='_my97DP']/iframe"))
        time.sleep(1)
        self.driver.find_element_by_xpath("html/body/div[1]/div[3]/table/tbody/tr[6]/td[5]").click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='_Draghandle_0']/td[2]/div[2]").click()
    #设置赠品
    def method_3(self):
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        self.driver.switch_to.frame("jd_iframe")
        self.driver.find_element_by_css_selector("#quantity0").send_keys(u"2")
        self.driver.find_element_by_css_selector("#productName0").click()
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("_DialogFrame_0")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='searchbox']/input[2]").send_keys(u"脉动")
        self.driver.find_element_by_css_selector("#query_A").click()
        self.driver.find_element_by_xpath(".//*[@id='ac_table']/tbody/tr[3]/td[1]/input").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(2)
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        time.sleep(1)
        self.driver.switch_to.frame("main1")
        self.driver.switch_to.frame("jd_iframe")
        time.sleep(1)
        self.driver.find_element_by_css_selector(".MenuList>a").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    #指定商品范围
    def method_4(self):
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        self.driver.switch_to.frame("jd_iframe")
        self.driver.find_element_by_css_selector("#productName0").click()
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("_DialogFrame_0")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='searchbox']/input[2]").send_keys(u"脉动")
        self.driver.find_element_by_css_selector("#query_A").click()
        self.driver.find_element_by_xpath(".//*[@id='ac_table']/tbody/tr[3]/td[1]/input").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(2)
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[0])
        self.driver.switch_to.frame("main1")
        self.driver.switch_to.frame("jd_iframe")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='products']/tbody/tr/td[2]/input[3]").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#productName1").click()
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[0])
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("_DialogFrame_0")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='searchbox']/input[2]").send_keys(u"脉动")
        self.driver.find_element_by_css_selector("#query_A").click()
        self.driver.find_element_by_xpath(".//*[@id='ac_table']/tbody/tr[9]/td[1]/input").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector("#_ButtonOK_0").click()
        time.sleep(2)
        current_window = self.driver.current_window_handle  # 获取当前窗口handle name
        all_windows = self.driver.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("main1")
        self.driver.switch_to.frame("jd_iframe")
        time.sleep(1)
        self.driver.find_element_by_css_selector("div.MenuList>a:nth-child(3)").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.switch_to.alert.accept()




