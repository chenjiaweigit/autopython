# coding: utf-8
import time
import random
import uiautomator2 as ut2
import decimal
import os
import shutil
PATH = lambda p: os.path.abspath(p)

package_namedealer = 'winretaildealer.net.winchannel.wincrm'

class appdealerInformation:
    # def __init__(self,ip):
    #     self.d = ut2.connect(ip)

    def __init__(self,device):
        self.d = ut2.connect_usb(device)

    def dealerstart_app(self):#启动经销商app
        self.d.app_start(package_namedealer)
        phonebrand = self.d.device_info[u"brand"]
        return phonebrand


    def dalerstop_app(self):
        self.d.app_stop(package_namedealer,True)

    def dealerBack(self):
        self.d(resourceId="com.android.systemui:id/back").click()

    #启动登录app
    def dealerlogin(self,username,password):
        self.d.app_start(package_namedealer)
        time.sleep(2)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").exists:
            a = self.d(className="android.widget.EditText")
            a[0].set_text(username)
            a[1].set_text(password)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview").click()
            assert self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview").exists
            pass
        else:

            pass
        return username

    def  dealerOfflogin(self):#退出登录
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        # num = self.d(className="android.widget.ImageView")
        # print(len(num))
        # if len(num) == 15 or len(num) == 11:
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=3).click()
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=2).click()
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        #     pass
        # elif len(num)==9 or len(num) == 10:
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=2).click()
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=2).click()
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        #     pass
        time.sleep(3)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=4).click()
        time.sleep(3)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",instance=2).click()
        time.sleep(3)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("logout")




    def dealerModifypwd(self,old_pws,pwd1,pwd2):#修改密码
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=4).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_pwd_edv_old_pwd").clear_text()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_pwd_edv_old_pwd").set_text(old_pws)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_pwd_edv_pwd1").set_text(pwd1)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_pwd_edv_pwd2").set_text(pwd2)
        print(old_pws,pwd1,pwd2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_pwd_btv_modify").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(3)
        assert self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").exists
        return old_pws,pwd1,pwd2




    def dealerHuionline(self):
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠聊").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠聊").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_message").click()

    def dealerHuionline_youhuiquan(self):
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/buttonMoreFuntionInText").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/textView", text=u"优惠券").click()
        time.sleep(2)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/mtv_lookinfo").exists:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_coupon_title").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_send").click()
            pass
        else:
            self.dealerBack()
            pass

    def  dealerUpgrade(self,name):#检查新版本
        from pymssqlManage import dealerSql
        row1= dealerSql.dealersql_appinfo(name)
        print(row1[0]),print(row1[1])
        l1 = int(str((row1[1])).replace('.',''))
        print(l1)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=5).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview").click()
        msg = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dlg_cmmn_alert_msg").info[u"text"]
        print (msg)
        if "最新版本" in str(msg):
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
            row2 = dealerSql.dealersql_appinfo(name)
            l2 = int(str((row1[1])).replace('.',''))
            assert l1 == l2
            if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").exists:
                self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
            else:
                pass
        else:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            for i in range(1,100):
                print (i)
                time.sleep(5)
                if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/download_close").exists:
                    continue
                else:
                    break
            print ("下载完成")
            self.d(resourceId="com.android.packageinstaller:id/ok_button").click()
            time.sleep(4)
            self.d(resourceId="com.android.packageinstaller:id/launch_button").click()
            row2 = dealerSql.dealersql_appinfo(name)
            l2 = int(str((row1[1])).replace('.',''))
            assert l2 - l1 ==1


    def  dealerAlterorder(self):
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_order_button").click()
        time.sleep(2)
        self.d.swipe(400, 900, 400, 300)
        while True:
            sumprice = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/total_textview").info[u"text"]
            if float(sumprice) > 1500.0:
                print (1)
                break
            else:
                # float(sumprice) <= 1500.0:
                self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_increase_one").click()
                continue
                pass
            pass
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        result = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title_buy_count_tv").exists
        print (result)
        return result

    def dealerOrder_confirm(self):#经销商确认订单
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview").click()
        #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item", className="android.widget.ImageView",instance=0).click()
        time.sleep(3)
        #elementnum = len(self.d(className="android.widget.ImageView"))
        #print(elementnum)
        #for i in range(0,elementnum):
        while self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").exists:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
            time.sleep(3)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/cb_reason").click()
            time.sleep(3)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
            time.sleep(3)
        else:
            pass
        time.sleep(3)
        #self.dealerBack()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        time.sleep(3)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item", className="android.widget.ImageView", instance=1).click()
        time.sleep(5)
        #while self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button",text=u"送货完成").exists:
        while self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button", text=u"送货完成").exists:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button",text=u"送货完成").click()
            time.sleep(3)
            # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").click()
            # for i in range(1,3):
            #     self.swipeup()
            # time.sleep(2)
            #UAT
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_cancel_photo").click()
            #retail
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_store_photo").click()
            time.sleep(5)
            self.d(resourceId="com.huawei.camera:id/shutter_button").click()
            time.sleep(5)
            self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
            time.sleep(5)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_addPhoto_one").click()
            time.sleep(5)
            self.d(resourceId="com.huawei.camera:id/shutter_button").click()
            time.sleep(5)
            self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
            time.sleep(5)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_to_pay").click()
            time.sleep(5)
            time.sleep(3)
            # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/plantime").click()
            # if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_date").exists:
            #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_date").click()
            #     self.d(resourceId="android:id/increment", description=u"增大日期值").click()
            #     self.d(resourceId="android:id/button1").click()
            #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
            #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
            #
            # else:
            #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
            #     pass
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/pay_check", className="android.widget.ImageView", instance=2).click()
            time.sleep(3)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
            time.sleep(3)
            self.d.swipe(400, 800, 400, 180)
            time.sleep(3)
        else:
            pass
        self.d.press("back")
        time.sleep(3)


    def dealerRolePower(self,custtitle):#经销商权限
        # self.appscreenshot()
        result1=""
        result2=""
        print(custtitle)
        print(type(custtitle))
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"门店管理").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview").click()
        if "经销商" in custtitle:
            time.sleep(2)
            num1 = self.d(className="android.widget.ImageView")
            print(len(num1))
            # time.sleep(3)
            assert len(num1)>=15
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
            result1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result1)
            assert result1 is True
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",
                   text=u"门店管理").click()
            result2 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result2)
            assert result2 is True
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
            num2 = self.d(className="android.widget.ImageView")
            print(len(num2))
            assert len(num2) == 11
            self.appscreenshot()
        elif "收单员" in custtitle:
            time.sleep(2)
            num1 = self.d(className="android.widget.ImageView")
            print(len(num1))
            #assert len(num1) == 15
            assert len(num1) == 13
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
            result1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result1)
            assert result1 is True
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",
                   text=u"门店管理").click()
            result2 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result2)
            assert result2 is True
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
            num2 = self.d(className="android.widget.ImageView")
            print(len(num2))
            #assert len(num2) == 9
            assert len(num2) == 13
            # self.appscreenshot()
        elif "车销司机" in custtitle:
            time.sleep(2)
            num1 = self.d(className="android.widget.ImageView")
            print(len(num1))
            #assert len(num1) == 14
            assert len(num1) == 13
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
            result1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dragItemIV").exists
            print(result1)
            assert result1 is False
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",text=u"门店管理").click()
            result2 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result2)
            assert result2 is False
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
            num2 = self.d(className="android.widget.ImageView")
            print(len(num2))
            #assert len(num2) == 10
            assert len(num2) == 11
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",text=u"我的").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=3).click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=2).click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        elif "送货司机" in custtitle:
            time.sleep(2)
            num1 = self.d(className="android.widget.ImageView")
            print(len(num1))
            #assert len(num1) == 12
            assert len(num1) == 11
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
            result1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dragItemIV").exists
            print(result1)
            assert result1 is False
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",
                   text=u"门店管理").click()
            result2 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
            print(result2)
            assert result2 is False
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
            num2 = self.d(className="android.widget.ImageView")
            print(len(num2))
            #assert len(num2) == 10
            assert len(num2) == 11
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",text=u"我的").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=3).click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview",className="android.widget.ImageView", instance=2).click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        elif "配送商" in custtitle:
            time.sleep(2)
            print(6)
        else:
            time.sleep(2)
            print(7)
        return result1,result2

    def dealerRoleManage(self,name,phone,mobile,id,loginname,loginpwd,loginnamejxs,loginpwdjxs,del_mobile):#人员管理
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        #self.dealerBack()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",instance=2).click()
        time.sleep(1)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_retail_add").click()
        self.d(text=u"请输入").set_text(name)
        self.d(text=u"请输入").set_text(phone)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/et_update_identity").click()
        #self.dealerBack()
        #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        # tv_retail_name = (self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_retail_name").info[u"text"])
        # tv_retail_identity = (self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_retail_identity").info[u"text"])
        # tv_retail_phone = (self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_retail_phone").info[u"text"])
        # assert name in tv_retail_name
        # assert phone in tv_retail_phone
        #assert "收单员" in tv_retail_identity
        if "收单员" in name:
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_retail_arrow").click()
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_check", className="android.widget.RadioButton", instance=0).click()
            self.dealerBack()
        #assert "送货司机" in self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").info[u"text"]
        elif "送货司机" in name:
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_check", className="android.widget.RadioButton", instance=1).click()
            self.dealerBack()
        #assert "配送商" in self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").info[u"text"]
        elif "配送商" in name:
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_check", className="android.widget.RadioButton", instance=2).click()
            self.dealerBack()
        #assert "车销司机" in self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_identity").info[u"text"]
        elif "车销司机" in name:
            #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_reset_pwd").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_check", className="android.widget.RadioButton", instance=3).click()
        #assert self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").exists
        #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(2)
        #self.dealerBack()
        #time.sleep(2)
        #self.dealerBack()
        #self.dealerOfflogin()
        #time.sleep(5)
        #assert self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_login").exists
        #网页新增账号白名单
        # from wangye import wangyeInfomation
        # aa = wangyeInfomation()
        # aa.wangyeLogin("http://retail.wincrm.net:8203", "wangbinsaler", "71028863")
        # aa.wangyeSwipetodown()
        # time.sleep(3)
        # aa.wangyeWhiteaccounts(mobile,id)
        # self.dealerlogin(loginname,loginpwd)
        # self.dealerOfflogin()
        # self.dealerlogin(loginnamejxs,loginpwdjxs)
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/iv_retail_arrow").click()
        # if del_mobile in self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_update_phone").info[u"text"]:
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_delete_person").click()
        #     self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        #     assert del_mobile not in self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_retail_phone").info[u"text"]
        # else:
        #     print(u"有问题")

    def dealerGoodsshelves(self,goodname,code,price,ip,phonebrand):#货架管理
        #脉动（青柠）1L*12瓶/箱,6902538004632,54
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"货架管理").click()
        time.sleep(5)
        assert self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/search_image").exists
        if self.d(text=u"搜索").exists:
            self.d(text=u"搜索").set_text(goodname)
            #self.d(text=goodname).clear_text()
            #self.dealerBack()
            self.d.press("back")
        else:
            pass
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dragItemIV").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/lowStockRB").click()#库存状态
        dealerstatus = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/lowStockRB").info[u"text"]
        print(dealerstatus)
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/winedittext").set_text("12321")

        #b,c = self.dealerPricecalculate(64.95)
        b, c = self.dealerPricecalculate(150.200)
        print(b)
        print(c)
        print(len(self.d(className="android.widget.EditText")))
        edittexts = self.d(className="android.widget.EditText")
        edittexts[0].set_text(code)
        edittexts[1].set_text(price)

        if b <= float(price)<=c:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
            pass
        else:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
            edittexts[1].clear_text()
            price1 = self.dealerPricerandom(b,c)
            print(price1)
            edittexts[1].set_text(price1)
            time.sleep(3)
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/title").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
            pass

        self.d(text=u"价格排序").click()
        self.d(text=u"价格排序").click()
        self.d(text=u"品牌").click()
        self.d(text=u"品牌").click()
        time.sleep(3)
        # from appsaler import appsalerInformation
        # bb = appsalerInformation(ip)
        # bb.start_app()
        # print(1)
        # bb.salerEnterstorehouse()
        # bb.salerGoodsshelves(goodname,str(price1),dealerstatus,phonebrand)
        pass

    def dealerorder_search(self,searchinfo,phonebrand):#经销商订单搜索
        #self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item").click()
        time.sleep(5)
        self.d(text=u"只看今天").click()
        self.d(text=u"最近三天").click()
        self.d(text=u"一周之内").click()
        self.d(text=u"查看全部").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/edt_search").set_text(searchinfo)
        # if "HONOR" in phonebrand:
        #     self.d.click(0.949, 0.898)
        # elif "OPPO" in phonebrand:
        #     self.d.click(0.91, 0.958)
        # time.sleep(3)
        # self.dealerBack()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_keyword").exists:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/img_del").click()
            if "HONOR" in phonebrand:
                self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            elif "OPPO" in phonebrand:
                self.d.click(0.716, 0.56)
            # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(3)
            self.dealerBack()
            pass
        else:
            self.dealerBack()
            pass
        time.sleep(3)
        #self.dealerBack()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        time.sleep(2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        time.sleep(2)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=3).click()
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/shopIconIV").exists:
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").click()
            self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/navigation_imageView").click()
            self.dealerBack()
            self.dealerBack()
            pass
        else:
            pass
        #self.d(className="android.widget.TextView", instance=3).click()
        time.sleep(4)
        self.appscreenshot()
        # time.sleep(2)
        # self.dealerBack()
        pass

    def dealerManagesalers(self,salername,ip):
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"门店管理").click()
        while True:
            if self.d(text=u"搜索").exists:
                self.d(text=u"搜索").set_text(salername)
                break
            else:
                break
        salertype = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_dealer_type").info[u"text"]
        print(salertype)
        print(type(salertype))
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/list_jiantou").click()
        print(self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dealer_type").info[u"text"])
        assert salertype in (self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dealer_type").info[u"text"])
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dealer_type").click()
        c = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/name", text=u"AB店").info[u"text"]
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/name", text=u"AB店").click()
        print(c)
        # from appsaler import appsalerInformation
        # bb = appsalerInformation(ip)
        # bb.start_app()
        # bb.salerEnterstorehouse()
        # bb.salerjxsManagesaler(c)
        # bb.salerBack()
        # time.sleep(2)
        # bb.salerBack()
        # time.sleep(2)
        # self.dealerstart_app()
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/dealer_type").click()
        # m = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/name").info[u"text"]
        # self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/name").click()
        # bb.start_app()
        # bb.salerEnterstorehouse()
        # bb.salerjxsManagesaler(m)










    def dealerLog_banben(self,a,b):
        log = open(a, 'a+', encoding='utf-8')
        log.write(
            '\n' + b + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime()) + '\n')
        log.close()

    def dealerPricerandom(self,e, f):
        s = random.uniform(e, f)
        return round(s,2)

    def dealerPricecalculate(self,a):
        b = a-a*0.3
        c = a+a*0.3
        return b,c

    def swipeup(self):
        self.d.swipe(500, 1000, 500, 300)
        pass

    def appscreenshot(self):#截图
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        print(timestamp)
        name = timestamp + ".png"
        print(name)
        self.d.screenshot(name)
        file = r"D:\excel"
        if os.path.exists(name):
            print(1)
            if os.path.isdir(file):
                pass
            else:
                os.mkdir(file)
                pass
            shutil.copy(name, file)
        else:
            print(2)
            pass
        l = file + "/" + timestamp + ".png"
        print(l)
        if os.path.exists(l):
            print(1)
            if os.path.exists(name):
                os.remove(name)
        else:
            print(2)

if __name__ == '__main__':
    cc =appdealerInformation()
    cc.appscreenshot()


















