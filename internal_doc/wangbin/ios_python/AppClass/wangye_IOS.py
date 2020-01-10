#-*- coding: UTF-8 -*-

from selenium import webdriver
import time
import Commonvariable
# import win32gui
import unittest
# import win32con
# from dateCheck import change_shuliang
from selenium.webdriver.support.ui import Select
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class wangyeInfomation_Tvnew:#惠tv后台
    def __init__(self):
        self.driver = webdriver.Chrome()
        pass
#封装click
    def wangyeclickId(self,id):
        self.driver.find_element_by_id(id).click()
    def wangyeclickClassName(self,id):
        self.driver.find_element_by_class_name(id).click()
    def wangyeclickCSS(self,id):
        self.driver.find_element_by_css_selector(id).click()
    def wangyeclickName(self,id):
        self.driver.find_element_by_name(id).click()
    def wangyeclickXpath(self,id):
        self.driver.find_element_by_xpath(id).click()

    def wangyeclickgetElemnet(self,tag,id):
        if tag =='id':
            self.driver.find_element_by_id(id).click()
        elif tag == 'name':
            self.driver.find_element_by_name(id).click()
        elif tag == 'classname':
            self.driver.find_element_by_class_name(id).click()
        elif tag == 'xpath':
            self.driver.find_element_by_xpath(id).click()
        elif tag =='css':
            self.driver.find_element_by_css_selector(id).click()
        else:
            print(".................................")

# 封装sendkeys
    def wangyesend_keysId(self,id,text):
        self.driver.find_element_by_id(id).send_keys(text)
    def wangyesend_keysClassName(self,id,text):
        self.driver.find_element_by_class_name(id).send_keys(text)
    def wangyesend_keysCSS(self,id,text):
        self.driver.find_element_by_css_selector(id).send_keys(text)
    def wangyesend_keysName(self,id,text):
        self.driver.find_element_by_name(id).send_keys(text)
    def wangyesend_keysXpath(self,id,text):
        self.driver.find_element_by_xpath(id).send_keys(text)

    def wangyesend_keysgetElemnet(self,tag,id,text):
        if tag =='id':
            self.driver.find_element_by_id(id).send_keys(text)
        elif tag == 'name':
            self.driver.find_element_by_name(id).send_keys(text)
        elif tag == 'classname':
            self.driver.find_element_by_class_name(id).send_keys(text)
        elif tag == 'xpath':
            self.driver.find_element_by_xpath(id).send_keys(text)
        elif tag =='css':
            self.driver.find_element_by_css_selector(id).send_keys(text)
        else:
            print(".................................")


    def wangyeLogin_newTv(self,a,username,password):
        self.driver.get(a)  # 输入url
        self.driver.maximize_window()  # 最大化
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("submit").click()
        time.sleep(2)
        pass

    def wangyetvNew_iframe(self,mainFrame):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(mainFrame)
        time.sleep(3)
        pass

    def wangyetvNew_offiframe(self):
        self.driver.switch_to.default_content()
        time.sleep(3)
        pass

    def wangyeNew_elementId(self,id):#id
        elementIds = self.driver.find_elements_by_id(id)
        for elementId in elementIds:
            if elementId.is_displayed():
                elementId.click()
                pass
            pass
        pass
    def wangyeNew_elementName(self,name):#name
        elementNames = self.driver.find_elements_by_class_name(name)
        for elementName in elementNames:
            if elementName.is_displayed():
                elementName.click()
                pass
            pass
        pass




# #新增视频
#     def  wangyetvNew_add(self,easyui_textbox_input1,easyui_textbox_input10,tv,tvphoto,easyui_textbox_input8):
#         self.driver.find_element_by_class_name("sider-nav-title").click()
#         # self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[1]/ul/li/a").click()
#         self.driver.find_element_by_class_name("sider-nav-s").click()
#         self.wangyetvNew_iframe("mainFrame")
#         time.sleep(2)
#         self.driver.find_element_by_id("add").click()
#         time.sleep(3)
#         self.driver.find_element_by_id("_easyui_textbox_input1").send_keys(easyui_textbox_input1)
#         self.driver.find_element_by_id("_easyui_textbox_input2").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("_easyui_textbox_input10").send_keys(easyui_textbox_input10)
#         time.sleep(2)
#         self.wangyeNew_elementId("_btn_search_dialog")#查询
#         time.sleep(2)
#         self.driver.find_element_by_name("ck").click()
#         time.sleep(2)
#         self.wangyeNew_elementId("_button_confirm_dialog")#确认
#         time.sleep(1)
#         self.driver.find_element_by_id("videoFile").click()
#         time.sleep(2)
#         dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
#         ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
#         ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
#         Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
#         button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
#
#         win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
#         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
#         self.driver.find_element_by_id("submitBtn").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("_easyui_textbox_input4").click()
#         self.driver.find_element_by_id("_easyui_textbox_input8").send_keys(easyui_textbox_input8)
#         time.sleep(2)
#         self.wangyeNew_elementId("_btn_search_dialog")
#         time.sleep(2)
#         self.driver.find_element_by_name("ck").click()
#         time.sleep(1)
#         self.wangyeNew_elementId("_button_confirm_dialog")
#         time.sleep(2)
#         self.wangyeNew_elementId("btn_save")
#         return easyui_textbox_input1,easyui_textbox_input10

    def wangeytvNew_examine(self,easyui_textbox_input1,value,easyui_textbox_input9):#审核视频
        self.driver.find_element_by_class_name("sider-nav-title").click()
        # self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[1]/ul/li/a").click()
        self.driver.find_element_by_class_name("sider-nav-s").click()
        self.wangyetvNew_iframe("mainFrame")
        self.driver.find_element_by_id("_easyui_textbox_input1").send_keys(easyui_textbox_input1)
        videoStatus = self.driver.find_element_by_name("videoStatus")
        Select(videoStatus).select_by_value(value)
        self.wangyeNew_elementId("btn_search")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[1]/div/a[1]/span").click()
        self.driver.find_element_by_id("_easyui_textbox_input12").click()
        self.driver.find_element_by_id("_easyui_combobox_i1_2").click()
        self.driver.find_element_by_id("_easyui_textbox_input5").click()
        time.sleep(3)
        self.driver.find_element_by_id("_easyui_textbox_input9").send_keys(easyui_textbox_input9)
        self.wangyeNew_elementId("_btn_search_dialog")
        time.sleep(2)
        self.driver.find_element_by_name("ck").click()
        time.sleep(2)
        self.wangyeNew_elementId("_button_confirm_dialog")
        time.sleep(2)
        self.wangyeNew_elementId("btn_save")

    def wangyetvNew_topstick(self,easyui_textbox_input1):#视频置顶
        self.driver.find_element_by_id("_easyui_textbox_input1").send_keys(easyui_textbox_input1)
        self.wangyeNew_elementId("btn_search")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[1]/div/a[4]/span").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # self.wangyeNew_elementName("wangyeNew_elementName")
        self.driver.find_element_by_xpath("/html/body/div[20]/div[3]/a/span/span").click()
        pass

    def wangeytvNew_UploadAwards(self,easyui_textbox_input7,easyui_textbox_input3,easyui_textbox_input4,easyui_textbox_input5):#视频上传奖励
        self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[3]/a").click()
        self.driver.find_element_by_css_selector("a[href='/rewardRule/upload']").click()
        self.wangyetvNew_iframe("mainFrame")
        time.sleep(2)
        print (1)
        add = self.driver.find_elements_by_class_name("l-btn-text")
        add[1].click()
        self.driver.find_element_by_id("_easyui_textbox_input2").click()
        self.driver.find_element_by_id("_easyui_textbox_input7").send_keys(easyui_textbox_input7)#区域-汉西
        time.sleep(3)
        self.wangyeNew_elementId("_btn_search_dialog")
        time.sleep(3)
        self.driver.find_element_by_name("ck").click()
        time.sleep(3)
        self.wangyeNew_elementId("_button_confirm_dialog")
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input3").send_keys(easyui_textbox_input3)
        self.driver.find_element_by_id("_easyui_textbox_input4").send_keys(easyui_textbox_input4)
        self.driver.find_element_by_id("_easyui_textbox_input5").send_keys(easyui_textbox_input5)
        self.driver.find_element_by_id("_easyui_textbox_input10").click()
        self.driver.find_element_by_class_name("datebox-button-a").click()
        self.driver.find_element_by_id("_easyui_textbox_input11").click()
        time.sleep(3)
        self.wangyeNew_elementName("datebox-button-a")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='dlg-buttons1']/a[2]").click()
        pass

    def wangeytvNew_shouloadAwards(self,quyu,dayjl,qijianjl):#视频观看奖励
        self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[3]/a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("a[href='/rewardRule/watch']").click()
        time.sleep(1)
        self.wangyetvNew_iframe("mainFrame")
        time.sleep(3)
        adds = self.driver.find_elements_by_css_selector("a[href='javascript:void(0)']")
        adds[1].click()
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input2").click()
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input6").send_keys(quyu)
        time.sleep(2)
        self.wangyeNew_elementId("_btn_search_dialog")
        time.sleep(2)
        self.driver.find_element_by_name("ck").click()
        time.sleep(1)
        self.wangyeNew_elementId("_button_confirm_dialog")
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input3").send_keys(dayjl)
        self.driver.find_element_by_id("_easyui_textbox_input4").send_keys(qijianjl)
        self.driver.find_element_by_id("_easyui_textbox_input9").click()
        self.driver.find_element_by_class_name("datebox-button-a").click()
        self.driver.find_element_by_id("_easyui_textbox_input10").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='dlg-buttons1']/a[2]").click()
        pass

    def wangyeNewtv_Barragereview(self,Barragereview_name,value):#弹幕审核
        self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[2]/a").click()
        self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[2]/ul/li/a").click()
        self.wangyetvNew_iframe("mainFrame")
        self.driver.find_element_by_id("_easyui_textbox_input1").send_keys(Barragereview_name)
        status = self.driver.find_element_by_id("status")
        Select(status).select_by_value(value)
        time.sleep(2)
        self.wangyeNew_elementId("btn_search")
        self.driver.find_element_by_xpath("//*[@id='row']/div[2]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='search_form']/div/a[1]").click()
        pass

    def wangyeNewtv_RecommendingCommodities(self,name_RecommendingCommodities,value,code,pinpainame,spname):#推荐商品
        self.driver.find_element_by_class_name("sider-nav-title").click()
        # self.driver.find_element_by_xpath("//*[@id='pf-sider']/ul/li[1]/ul/li/a").click()
        self.driver.find_element_by_class_name("sider-nav-s").click()
        self.wangyetvNew_iframe("mainFrame")
        self.driver.find_element_by_id("_easyui_textbox_input1").send_keys(name_RecommendingCommodities)
        videoStatus = self.driver.find_element_by_name("videoStatus")
        Select(videoStatus).select_by_value(value)
        self.wangyeNew_elementId("btn_search")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[13]/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input5").click()
        self.driver.find_element_by_id("_easyui_textbox_input14").send_keys(code)
        self.driver.find_element_by_id("_easyui_textbox_input15").send_keys(pinpainame)
        self.wangyeNew_elementId("_btn_search_dialog")
        time.sleep(3)
        self.driver.find_element_by_name("ck").click()
        self.wangyeNew_elementId("_button_confirm_dialog")
        time.sleep(3)
        self.driver.find_element_by_id("_easyui_textbox_input6").click()
        time.sleep(2)
        self.driver.find_element_by_id("_easyui_textbox_input17").send_keys(spname)
        self.wangyeNew_elementId("_btn_search_dialog")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r3-2-0']/td[1]/div/input").click()
        self.wangyeNew_elementId("_button_confirm_dialog")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='dlg-buttons1']/a[2]").click()
        return spname
    def wangyeNewtv_RecommendingCommodities_del(self):
        self.driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[13]/div/a[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[20]/div[3]/a[1]").click()

'''惠下单后台'''
class wangyeInfomation:
    def __init__(self):
        self.browser = webdriver.Firefox()
    def wangeyqiehuaniframe(self,a):#切换iframe
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame(a)
        time.sleep(3)
    def wangyeQuit(self):
        self.browser.quit()
        pass

    # 封装click
    def wangyeclickId(self, id):
        self.browser.find_element_by_id(id).click()

    def wangyeclickClassName(self, id):
        self.browser.find_element_by_class_name(id).click()

    def wangyeclickCSS(self, id):
        self.browser.find_element_by_css_selector(id).click()

    def wangyeclickName(self, id):
        self.browser.find_element_by_name(id).click()

    def wangyeclickXpath(self, id):
        self.browser.find_element_by_xpath(id).click()

    def wangyeclickgetElemnet(self, tag, id):
        if tag == 'id':
            self.browser.find_element_by_id(id).click()
        elif tag == 'name':
            self.browser.find_element_by_name(id).click()
        elif tag == 'classname':
            self.browser.find_element_by_class_name(id).click()
        elif tag == 'xpath':
            self.browser.find_element_by_xpath(id).click()
        elif tag == 'css':
            self.browser.find_element_by_css_selector(id).click()
        else:
            print(".................................")

            # 封装sendkeys

    def wangyesend_keysId(self, id, text):
        self.browser.find_element_by_id(id).send_keys(text)

    def wangyesend_keysClassName(self, id, text):
        self.browser.find_element_by_class_name(id).send_keys(text)

    def wangyesend_keysCSS(self, id, text):
        self.browser.find_element_by_css_selector(id).send_keys(text)

    def wangyesend_keysName(self, id, text):
        self.browser.find_element_by_name(id).send_keys(text)

    def wangyesend_keysXpath(self, id, text):
        self.browser.find_element_by_xpath(id).send_keys(text)

    def wangyesend_keysgetElemnet(self, tag, id, text):
        if tag == 'id':
            self.browser.find_element_by_id(id).send_keys(text)
        elif tag == 'name':
            self.browser.find_element_by_name(id).send_keys(text)
        elif tag == 'classname':
            self.browser.find_element_by_class_name(id).send_keys(text)
        elif tag == 'xpath':
            self.browser.find_element_by_xpath(id).send_keys(text)
        elif tag == 'css':
            self.browser.find_element_by_css_selector(id).send_keys(text)
        else:
            print(".................................")

    def wangyeSwipetodown(self):#滑动到底部
        jsl = 'document.getElementById("menuScrollAuto").scrollTop=2000'
        self.browser.execute_script(jsl)
        pass

    def wangyeWhiteaccounts(self,mobile,id):
        self.browser.find_element_by_id("menuGroup_CrmDevLoginWhitelists").click()
        self.browser.find_element_by_id("a_menuId_129130").click()
        self.wangeyqiehuaniframe("main1")
        # assert assertLocation
        self.browser.find_element_by_id("mobile").send_keys(mobile)
        self.browser.find_element_by_xpath("//*[@id='searchbox']/table/tbody/tr/td[8]/input[2]").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.switch_to.frame("jd_iframe")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='ec_table']/tbody/tr/td[1]/input").click()
        self.browser.find_element_by_id(id).send_keys("王斌自动化")
        self.browser.find_element_by_css_selector("a[href='###']").click()
        self.browser.switch_to.alert.accept()
        time.sleep(2)
        self.browser.switch_to.alert.accept()




    def wangyeLogin(self,a,b,c):#登录
        self.browser.get(a)  # 输入url
        self.browser.maximize_window()  # 最大化
        self.browser.find_element_by_css_selector("#userAccount").send_keys(b)  # 输入账号
        self.browser.find_element_by_css_selector(".login_pwd").send_keys(c)  # 输入密码
        self.browser.implicitly_wait(5)  # 等待时间
        self.browser.find_element_by_css_selector(".login_on").click()  # 登陆按钮
        self.browser.find_element_by_css_selector("#menuId_hxdplatform").click()
        self.browser.switch_to.frame('menu1')
        time.sleep(10)
        self.browser.find_element_by_css_selector(".promptHeader>a").click()
        pass

    #经销商首次登陆
    #经销商名称,姓名，账号，密码，经度，纬度，最小启动金额，联系电话，地址;查询省市,查询居委会，
    def dealerJxsOneLogin(self,poiName,nickName,mobile,password,longitude,latitude,minOrderAmount,telephone,address,provinceName,villageName):
        self.wangyeclickId("menuGroup_jxsglnew")
        self.wangyeclickId("a_menuId_jxsxxglnew")
        self.wangeyqiehuaniframe("main1")
        self.wangyeclickCSS("a[href='/crmPoiInfo/crmPoiInfoAction.do?method=toAddDealer']")
        self.wangyesend_keysId("poiName",poiName)
        self.wangyesend_keysId("nickName",nickName)
        self.wangyesend_keysId("mobile",mobile)
        self.wangyesend_keysId("password",password)
        self.wangyesend_keysId("longitude",longitude)
        self.wangyesend_keysId("latitude",latitude)
        self.wangyesend_keysId("rate","0")
        self.wangyesend_keysId("minOrderAmount",minOrderAmount)
        self.wangyesend_keysId("telephone",telephone)
        self.wangyesend_keysId("address",address)
        jxsType = self.browser.find_element_by_id("dealerSourceType")
        jxsType.click()
        Select(jxsType).select_by_value("普通经销商")#选择普通经销商或者镇镇通经销商
        self.wangyeclickId("countyName")
        self.wangyeqiehuanifrme2()
        self.wangyesend_keysName("provinceName",provinceName)
        self.wangyeclickId("query_A")
        self.wangyesend_keysName("villageName",villageName)
        self.wangyeclickName("rdo1")
        self.wangyeclickCSS("a[href='javascript:ok()']")
        self.wangeyqiehuaniframe("main1")
        self.wangyeclickId("save")
        return poiName,nickName,mobile,password,longitude,latitude,minOrderAmount,telephone,address,provinceName,villageName





#传入查询的门店手机号
    def wangyeSalerdefaultdealer(self,salername):#门店默认经销商
        self.browser.find_element_by_id("menuGroup_mdglnew").click()
        self.browser.find_element_by_id("a_menuId_mdxgppgl").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_name("$eq_storePhone").send_keys(salername)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/delete.gif']").click()#删除
        self.browser.switch_to.alert.accept()

    def wangyeHomepage(self,hanxi):#首页管理
        self.browser.find_element_by_id("menuGroup_cxgl").click()
        self.browser.find_element_by_id("a_menuId_42042").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("cityName").click()
        self.wangeyqiehuaniframe("_DialogFrame_0")
        self.browser.find_element_by_id("cityName").send_keys(hanxi)
        self.browser.find_element_by_name("rd_cityId").click()
        self.browser.switch_to.default_content()
        self.browser.find_element_by_class_name("buttonStyle").click()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_id("query_A").click()

#新增首页：名称，param1,类型，门店是否可见，经销商是否可见,排序
    def wangyeHomepage_add(self,adTitle,param1,homeType,salerisFlaog,jxsisFlag,sort,tupianlujin,xiaoshouquyu):
        self.browser.find_element_by_css_selector("a[href='/crm/adposition.do?method=toAdd']").click()
        self.browser.find_element_by_id("adTitle").send_keys(adTitle)
        self.browser.find_element_by_id("param1").send_keys(param1)
        adtype = self.browser.find_element_by_name("adType")
        self.browser.find_element_by_name("adType").click()
        Select(adtype).select_by_value(homeType)
        wholesaleFlag= self.browser.find_element_by_id("wholesaleFlag")
        self.browser.find_element_by_id("wholesaleFlag").click()
        Select(wholesaleFlag).select_by_value(salerisFlaog)
        visual = self.browser.find_element_by_id("visual")
        self.browser.find_element_by_id("visual").click()
        Select(visual).select_by_value(jxsisFlag)
        self.browser.find_element_by_id("sort").send_keys(sort)
        self.browser.find_element_by_css_selector("input[value='文件上传']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.switch_to.frame("uploadIframe")
        time.sleep(2)
        self.browser.switch_to.frame("page_interface_frame")
        time.sleep(2)
        self.browser.find_element_by_id("mainfile").click()
        time.sleep
        # dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        #
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        self.browser.find_element_by_css_selector("a[href='javascript:submitData();']").click()
        time.sleep(2)
        self.browser.switch_to.alert.accept()
        time.sleep(2)
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.find_element_by_id("startTime").click()
        time.sleep(2)
        self.browser.switch_to.default_content()
        iframestatime = self.browser.find_element_by_xpath("//iframe[@src='http://uat.wincrm.net:8218/widgets/My97DatePicker/My97DatePicker.htm']")
        self.browser.switch_to.frame(iframestatime)
        time.sleep(3)
        self.browser.find_element_by_id("dpTodayInput").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("endTime").click()
        time.sleep(2)
        self.browser.switch_to.default_content()
        iframeendime = self.browser.find_element_by_xpath("//iframe[@src='http://uat.wincrm.net:8218/widgets/My97DatePicker/My97DatePicker.htm']")
        self.browser.switch_to.frame(iframeendime)
        time.sleep(3)
        self.browser.find_element_by_id("dpTodayInput").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("cityName").click()
        time.sleep(2)
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("_DialogFrame_0")
        time.sleep(3)
        self.browser.find_element_by_id("cityName").send_keys(xiaoshouquyu)
        self.browser.find_element_by_name("rd_cityId").click()
        self.browser.switch_to.default_content()
        self.browser.find_element_by_class_name("buttonStyle").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("save").click()

#将该设置的首页置为无效
    def wangyeHomepage_no(self):
        self.wangeyqiehuaniframe("menu1")
        self.browser.find_element_by_id("a_menuId_42042").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_css_selector("a[href='javascript:query();']").click()
        time.sleep(2)
        self.browser.find_element_by_css_selector("img[src='/images/delete.gif']").click()
        self.browser.switch_to.alert.accept()
#清除缓存
    def wangyeHomepage_clear(self):
        self.wangeyqiehuaniframe("menu1")
        self.browser.find_element_by_id("a_menuId_122122").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_css_selector("a[href='/crm/redisKey.do?method=del&key=Helper399:WR_HOME']").click()
        time.sleep(5)

# 门店经销商渠道新增
    def wangyeQudao(self,a,b):
        self.browser.find_element_by_css_selector("#menuId_hxdplatform").click()
        self.browser.switch_to.frame('menu1')
        time.sleep(3)
        self.browser.find_element_by_css_selector(".promptHeader>a").click()
        self.browser.find_element_by_id("menuGroup_jxsglnew").click()
        self.browser.find_element_by_id("a_menuId_storeDistPricetypeList").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_css_selector("a[href='/crm/storeDistPricetype.do?method=edit']").click()
        self.browser.find_element_by_id("storeName").click()
        self.browser.switch_to.default_content()
        time.sleep(2)
        self.browser.switch_to.frame("main1")
        time.sleep(3)
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.switch_to.frame("tree")
        time.sleep(3)
        self.browser.find_element_by_name("poiCode").send_keys(a)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_id("pricetypeName").click()
        time.sleep(3)
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.switch_to.frame("tree")
        time.sleep(3)
        self.browser.find_element_by_name("id").send_keys(b)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.find_element_by_id("save").click()  # AB渠道保存成功

    def wangyeQudaoshop(self,a):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        time.sleep(2)
        self.browser.find_element_by_id("a_menuId_dealerProductPricetypeList").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(5)
        self.browser.find_element_by_id("pricetypeName").click()
        self.browser.switch_to.default_content()
        time.sleep(2)
        self.browser.switch_to.frame("main1")
        time.sleep(3)
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.switch_to.frame("tree")
        time.sleep(3)
        self.browser.find_element_by_name("id").send_keys(a)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_name("$eq_issale").click()
        qdsxj = self.browser.find_element_by_name("$eq_issale")
        Select(qdsxj).select_by_value("1")
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()
        self.browser.find_element_by_id("price").clear()
        self.browser.find_element_by_id("price").send_keys(u"33")#修改渠道价格
        self.browser.find_element_by_css_selector("a[href='javascript:save();']").click()
        qdprice = str(round(float(self.browser.find_element_by_css_selector(".odd>td:nth-child(7)").text),2))  # 修改渠道价格
        return qdprice

    def wangyeQudaodelete(self):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        self.browser.find_element_by_id("a_menuId_storeDistPricetypeList").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_id("sid").click()
        self.browser.find_element_by_css_selector("a[href='javascript:batchDel();']").click()
        self.browser.switch_to.alert.accept()

    def wangyeMendianxinxi_wx(self,a,b):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        self.browser.find_element_by_id("menuGroup_mdglnew").click()
        self.browser.find_element_by_id("a_menuId_mdxxgl").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        # 门店置为无效：(0)
        self.browser.find_element_by_id("mobile").send_keys(a)
        self.browser.find_element_by_id("query_A").click()
        time.sleep(2)
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()
        md_zt = self.browser.find_element_by_id("status")
        self.browser.find_element_by_id("status").click()
        Select(md_zt).select_by_value("0")
        self.browser.find_element_by_id("statusReason").clear()
        self.browser.find_element_by_id("statusReason").send_keys(b)
        self.browser.find_element_by_id("save").click()
        time.sleep(2)

    def wangyeMendianxinxi_yx(self):
        mdzt_ht = self.browser.find_element_by_name("$eq_status")
        self.browser.find_element_by_name("$eq_status").click()
        Select(mdzt_ht).select_by_value("0")
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()
        self.browser.find_element_by_id("status").click()
        wx_yx = self.browser.find_element_by_id("status")
        Select(wx_yx).select_by_value("1")
        self.browser.find_element_by_id("save").click()

    def mdmorenjxs(self,a,b):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        time.sleep(2)
        self.browser.find_element_by_id("a_menuId_mdxgppgl").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.find_element_by_name("$eq_storePhone").send_keys(a)
        self.browser.find_element_by_id("dealerName").click()
        self.browser.switch_to.default_content()  # 退出frame
        current_window = self.browser.current_window_handle  # 获取当前窗口handle name
        all_windows = self.browser.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.browser.switch_to.window(window)
        time.sleep(2)
        self.browser.switch_to.frame('main1')
        time.sleep(2)
        self.browser.switch_to.frame('modalDialog')
        time.sleep(2)
        self.browser.switch_to.frame('tree')
        time.sleep(2)
        self.browser.find_element_by_name("poiName").send_keys(b)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.browser.switch_to.default_content()  # 退出frame
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_id("sid").click()
        self.browser.find_element_by_css_selector("a[href='javascript:batchDel();']").click()
        self.browser.switch_to.alert.accept()

# 网页经销商代理商品：
    def jxsDailishop_qdl(self,a,b):
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        time.sleep(2)
        self.browser.find_element_by_css_selector("#menuGroup_jxsglnew").click()
        self.browser.find_element_by_css_selector("#a_menuId_jxsspsj").click()
        self.browser.switch_to.default_content()  # 退出frame
        self.browser.switch_to.frame('main1')
        time.sleep(3)
        self.browser.find_element_by_css_selector("#poiCode").send_keys(a)
        self.browser.find_element_by_css_selector("#prodNameZh").send_keys(b)
        time.sleep(2)
        self.browser.find_element_by_css_selector("#query_A").click()  # 查询
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()  # 编辑
        self.browser.find_element_by_css_selector("#minOrderQuantity").clear()  # 清空
        # qidingliang = change_shuliang()
        # qidingbeishu = change_shuliang()
        # self.browser.find_element_by_css_selector("#minOrderQuantity").send_keys(qidingliang)  # 最小起订量
        # self.browser.find_element_by_css_selector("#minOrderRatio").clear()  # 清空
        # self.browser.find_element_by_css_selector("#minOrderRatio").send_keys(qidingbeishu)  # 最小起订倍数
        self.browser.find_element_by_css_selector("#save").click()  # 保存
        m = int(self.browser.find_element_by_css_selector(".odd>td:nth-child(17)").text)  # 最小起订量
        return m

    def jxsDailishop_qdbs(self):
        n = int(self.browser.find_element_by_css_selector(".odd>td:nth-child(18)").text)  # 最小启动倍数
        return n

    def jxsDailishop_wh(self,a):
        self.browser.find_element_by_css_selector("#prodNameZh").clear()
        self.browser.find_element_by_css_selector("#prodNameZh").send_keys(a)
        self.browser.find_element_by_css_selector("#query_A").click()  # 查询
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()  # 编辑
        zt_jxssp = self.browser.find_element_by_name("stockStatus")
        Select(zt_jxssp).select_by_value("-1")  # 无货设置
        self.browser.find_element_by_css_selector("#save").click()  # 保存
        sp_zt = str(self.browser.find_element_by_css_selector(".odd>td:nth-child(19)").text)
        return sp_zt

    def wangyeqiehuanifrme2(self):
        #切换iframe2
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.switch_to.frame("modalDialog")
        time.sleep(2)
        self.browser.switch_to.frame("tree")
        time.sleep(2)

    def wangyePromotion_banner(self,poiName,brandName,linkDesc):  #代理品牌促销信息
        self.browser.find_element_by_id("menuGroup_jxsglnew").click()
        time.sleep(2)
        self.browser.find_element_by_id("a_menuId_jxsdlppgl").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("orgName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("poiName").send_keys(poiName)
        time.sleep(2)
        self.browser.find_element_by_id("query_A").click()
        # self.browser.find_element_by_name("rdo1").click()
        time.sleep(4)
        self.browser.find_element_by_xpath("//*[@id='poiDealerList_table']/tbody/tr/td[1]/input").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("brandName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("brandName").send_keys(brandName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_css_selector("a[href='javascript:query();']").click()
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.switch_to.frame("jd_iframe")
        time.sleep(2)
        self.browser.find_element_by_name("linkDesc").clear()
        self.browser.find_element_by_name("linkDesc").send_keys(linkDesc)
        time.sleep(2)
        self.browser.find_element_by_name("btnUpload").click()
        time.sleep(3)
        self.browser.switch_to.alert.accept()
        return linkDesc

    def wangyePromotion_jxs(self,lk_poiName,promotionSimpleDesc):
        self.browser.find_element_by_id("a_menuId_jxsxxglnew").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_name("$lk_poiName").send_keys(lk_poiName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()
        self.browser.find_element_by_name("promotionSimpleDesc").clear()
        self.browser.find_element_by_name("promotionSimpleDesc").send_keys(promotionSimpleDesc)
        self.browser.find_element_by_id("save").click()
        return promotionSimpleDesc

    def wangyePromotion_shop(self,poiName,prodName,prodPromotion,v):#商品上下架促销信息
        self.browser.find_element_by_id("a_menuId_dealerProductPricetypeList").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("orgName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("poiName").send_keys(poiName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_name("$eq_prodName").send_keys(prodName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_xpath("//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a/img").click()
        self.browser.find_element_by_id("prodPromotion").clear()
        self.browser.find_element_by_id("prodPromotion").send_keys(prodPromotion)
        self.browser.find_element_by_id("showPlatformPromotioned").click()
        showPlatformPromotioned = self.browser.find_element_by_id("showPlatformPromotioned")
        Select(showPlatformPromotioned).select_by_value(v)
        self.browser.find_element_by_css_selector("a[href='javascript:save();']").click()
        self.browser.find_element_by_id("query_A").click()
        return prodPromotion



    def jxsDailipinpai_cxxx(self,a,b):

        self.browser.find_element_by_id("a_menuId_jxsdlppgl").click()
        time.sleep(2)
        self.browser.switch_to.default_content()
        current_window = self.browser.current_window_handle  # 获取当前窗口handle name
        all_windows = self.browser.window_handles  # 获取所有窗口handle name
        for window in all_windows:
            if window != current_window:
                self.browser.switch_to.window(window)
        time.sleep(2)
        self.browser.switch_to.frame('main1')
        self.browser.find_element_by_id("orgName").click()
        time.sleep(3)
        self.browser.switch_to.frame('modalDialog')
        time.sleep(3)
        self.browser.switch_to.frame('tree')
        time.sleep(2)
        self.browser.find_element_by_css_selector("input[name='poiCode']").send_keys(a)
        self.browser.find_element_by_css_selector("#query_A").click()
        self.browser.find_element_by_css_selector("input[name='rdo1']").click()
        # browser.find_element_by_css_ selector("a:javascript:ok()").click()
        self.browser.find_element_by_css_selector(".MenuList>a:nth-child(2)").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame('main1')
        time.sleep(2)
        self.browser.find_element_by_css_selector("#query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()  # 编辑
        self. browser.switch_to.frame("jd_iframe")
        self.browser.find_element_by_css_selector("textarea[name='linkDesc']").clear()
        self.browser.find_element_by_css_selector("textarea[name='linkDesc']").send_keys(b)
        self.browser.find_element_by_css_selector("a[name='btnUpload']").click()
        time.sleep(3)
        self.browser.switch_to.alert.accept()  # 处理alert弹窗
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        table = self.browser.find_element_by_css_selector(".tableBody")  # 获取table
        table_rows = table.find_elements_by_tag_name("tr")  # 获取table总行数
        list_jxspinpai = []
        for i in range(0, len(table_rows)):
            list_jxspinpai.append(table_rows[i].find_elements_by_tag_name("td")[6].text)  # 将该经销商所有的品牌加入列表
        jxs_pp_cxxx = table_rows[0].find_elements_by_tag_name("td")[7].text  # 经销商代理品牌促销信息
        return jxs_pp_cxxx

    def jxsDaipinshangpin_jz(self,a,b):
        # 设置为商品紧张
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("menu1")
        time.sleep(3)
        self.browser.find_element_by_id("a_menuId_jxsspsj").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(3)
        self.browser.find_element_by_css_selector("#poiCode").send_keys(a)
        self.browser.find_element_by_css_selector("#prodNameZh").send_keys(b)
        self.browser.find_element_by_css_selector("#query_A").click()  # 查询
        self.browser.find_element_by_css_selector("img[src='/images/edit.gif']").click()  # 编辑
        zt_jxssp = self.browser.find_element_by_name("stockStatus")
        Select(zt_jxssp).select_by_value("2")  # 无货设置
        self.browser.find_element_by_css_selector("#save").click()  # 保存
        sp_zt_jz = str(self.browser.find_element_by_css_selector(".odd>td:nth-child(19)").text)
        return sp_zt_jz

    # def wangyeOrder_problem_

    def wangyeOrder_problem_salerleixing(self,ruleName,limitPrice,limitNum,limitRate,value):#异常订单门店类型
        time.sleep(3)
        self.browser.find_element_by_id("menuGroup_orderException").click()
        self.browser.find_element_by_id("a_menuId_threshold4store").click()
        self.wangeyqiehuaniframe("main1")
        time.sleep(2)
        self.browser.find_element_by_css_selector("a[href='/crm/threshold.do?method=toEditThreshold&thresholdType=storeType']").click()
        self.browser.find_element_by_id("ruleName").send_keys(ruleName)
        self.browser.find_element_by_id("limitPrice").send_keys(limitPrice)
        self.browser.find_element_by_id("limitNum").send_keys(limitNum)
        self.browser.find_element_by_id("limitRate").send_keys(limitRate)
        limitRateUnit= self.browser.find_element_by_id("limitRateUnit")
        Select(limitRateUnit).select_by_value(value)#(0,1,2)
        self.browser.find_element_by_id("limitValueNames").click()
        time.sleep(9)
        self.wangeyqiehuaniframe("main1")
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.find_element_by_id("selAll").click()
        self.browser.find_element_by_css_selector("input[onclick='ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("save").click()
        time.sleep(2)
        self.browser.switch_to.alert.accept()
        return ruleName


    def wangyeOrder_problem_Setarea(self,ruleName1,ruleName2,provinceName,areaThresholdName,Environmental1,Environmental2,limitPrice):#异常订单设置区域
        self.browser.find_element_by_id("menuGroup_orderException").click()
        self.browser.find_element_by_id("a_menuId_areaThresholdList").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_css_selector("a[href='/crm/orderAreaThreshold.do?method=areaThresholdAdd']").click()
        self.browser.find_element_by_id("ruleName").send_keys(ruleName1)
        self.browser.find_element_by_id("storeTypeRuleName").click()
        self.wangeyqiehuaniframe("_DialogFrame_0")
        self.browser.find_element_by_id("ruleName").send_keys(ruleName2)
        self.browser.find_element_by_css_selector("a[href='javascript:query();']").click()
        self.browser.find_element_by_class_name("tableHeader").click()
        self.browser.switch_to.default_content()
        time.sleep(5)
        self.browser.find_element_by_id("_ButtonOK_0").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("regionName").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.switch_to.frame("modalDialog")
        time.sleep(3)
        self.browser.switch_to.frame("tree")
        time.sleep(2)
        self.browser.find_element_by_name("provinceName").send_keys(provinceName)
        self.browser.find_element_by_css_selector("a[href='javascript:baseDialogForm.region_p.value=1;query()']").click()
        self.browser.find_element_by_css_selector("input[idtxt='810000000000']").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("startTime").click()
        self.browser.switch_to.default_content()
        iframestartime = self.browser.find_element_by_xpath(Environmental1)
        self.browser.switch_to.frame(iframestartime)
        time.sleep(2)
        self.browser.find_element_by_id("dpTodayInput").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("endTime").click()
        self.browser.switch_to.default_content()
        iframeendime = self.browser.find_element_by_xpath(Environmental2)
        self.browser.switch_to.frame(iframeendime)
        self.browser.find_element_by_id("dpTodayInput").click()
        self.wangeyqiehuaniframe("main1")
        self.wangyesend_keysgetElemnet("id", "limitPrice", limitPrice)
        self.browser.find_element_by_id("save").click()
        time.sleep(2)
        self.browser.find_element_by_id("areaThresholdName").send_keys(areaThresholdName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/check-on2.jpg']").click()
        time.sleep(4)
        queren = self.browser.find_elements_by_class_name("ui-button-text")
        queren[1].click()

    def wangyeOrderproblem_look(self,eq_orderNo,reason):#不通过
        self.browser.find_element_by_id("menuGroup_ddglnew").click()
        self.browser.find_element_by_id("a_menuId_crmExceptionOrderReview").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_name("$eq_orderNo").send_keys(eq_orderNo)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_xpath("//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a[2]").click()
        self.browser.find_element_by_id("reviewOrderDesc").send_keys(reason)
        self.browser.find_element_by_id("btnSure").click()
#删除执行规则
    def wangyeOrderproblem_X(self,areaThresholdName):
        self.browser.find_element_by_id("menuGroup_orderException").click()
        self.browser.find_element_by_id("a_menuId_areaThresholdList").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("areaThresholdName").send_keys(areaThresholdName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("img[src='/images/delete.png']").click()
        time.sleep(2)
        queren = self.browser.find_elements_by_class_name("ui-button-text")
        queren[1].click()
        pass


    #组合商品sku
    def wangyeShopgroup(self,catName,prodNameZh,prodSku,brandName,s2id_autogen1_search,prodBarCode,prodPrice,prodSize,value,costPrice,presentPrice,skuNum,tupianlujin):
        self.browser.find_element_by_id("menuGroup_productmamagernew").click()
        self.browser.find_element_by_id("a_menuId_productinfonew").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_id("catName").send_keys(catName)
        self.browser.find_element_by_id("prodNameZh").send_keys(prodNameZh)
        self.browser.find_element_by_id("prodSku").send_keys(prodSku)
        self.browser.find_element_by_id("s2id_brandCode").click()

        self.browser.find_element_by_id("s2id_autogen1_search").send_keys(s2id_autogen1_search)
        self.browser.find_element_by_class_name("select2-result-label").click()
        self.browser.find_element_by_id("brandName").send_keys(brandName)
        self.browser.find_element_by_id("prodBarCode").send_keys(prodBarCode)
        self.browser.find_element_by_id("prodPrice").send_keys(prodPrice)
        self.browser.find_element_by_id("prodSize").send_keys(prodSize)
        isCombinationSku = self.browser.find_element_by_id("isCombinationSku")
        self.browser.find_element_by_id("isCombinationSku").click()
        Select(isCombinationSku).select_by_value(value)
        self.browser.find_element_by_id("singgleSkuAdd").click()
        self.browser.find_element_by_class_name("skuBrand").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("brandName").send_keys(u"王老吉")
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("input[nametxt='王老吉']").click()
        # self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_class_name("skuName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("prodNameZh").send_keys(u"王老吉藕汁310ml*24/箱")
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_name("rdo1").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_class_name("costPrice").clear()
        self.browser.find_element_by_class_name("costPrice").send_keys(costPrice)
        self.browser.find_element_by_class_name("presentPrice").clear()
        self.browser.find_element_by_class_name("presentPrice").send_keys(presentPrice)
        self.browser.find_element_by_class_name("skuNum").clear()
        self.browser.find_element_by_class_name("skuNum").send_keys(skuNum)

        self.browser.find_element_by_css_selector("input[value='文件上传']").click()
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        time.sleep(2)
        self.browser.switch_to.frame("uploadIframe")
        time.sleep(2)
        self.browser.switch_to.frame("page_interface_frame")
        time.sleep(2)
        self.browser.find_element_by_id("mainfile").click()
        time.sleep(3)
        # dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        #
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        self.browser.find_element_by_css_selector("a[href='javascript:submitData();']").click()
        time.sleep(2)
        self.browser.switch_to.alert.accept()
        time.sleep(2)
        self.browser.switch_to.default_content()
        self.browser.switch_to.frame("main1")
        self.browser.find_element_by_id("save").click()
        return prodSku

    def wangyeShopExcelgrounding(self,excel):  #經銷商商品excel上下架
        self.browser.find_element_by_id("menuGroup_jxsglnew").click()
        self.browser.find_element_by_id("a_menuId_dealerProductPricetypeList").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_css_selector("a[href='javascript:doImport();']").click()
        self.wangeyqiehuaniframe("_DialogFrame_0")
        self.browser.find_element_by_id("excelFile").click()
        # dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        #
        # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        # time.sleep(5)
        self.browser.find_element_by_id("import").click()
        pass

    def wangyeshopBindingManagement(self,poiName,brandCode):#經銷商綁定管理
        self.browser.find_element_by_id("menuGroup_jxsglnew").click()
        self.browser.find_element_by_id("a_menuId_jxsspsj").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_class_name("Im80").click()
        d_stype = self.browser.find_element_by_id("select_file_or_sys")
        self.browser.find_element_by_id("select_file_or_sys").click()
        Select(d_stype).select_by_value("2")
        self.browser.find_element_by_id("orgName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("poiName").send_keys(poiName)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_id("selectAllbox").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("brandName").click()
        self.wangyeqiehuanifrme2()
        self.browser.find_element_by_name("brandCode").send_keys(brandCode)
        self.browser.find_element_by_id("query_A").click()
        self.browser.find_element_by_css_selector("input[idtxt=lebaishi]").click()
        self.browser.find_element_by_css_selector("a[href='javascript:ok()']").click()
        self.wangeyqiehuaniframe("main1")
        self.browser.find_element_by_id("save_brand_prod_btn").click()
        pass













