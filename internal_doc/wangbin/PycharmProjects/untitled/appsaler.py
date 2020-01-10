# coding: utf-8
# import atx
import time
import datetime
import os
import shutil
import threading
import re
from assertpy import assert_that
import uiautomator2 as ut2

from appdealer import appdealerInformation

from wangye import wangyeInfomation

package_namesaler = 'winretailsaler.net.winchannel.wincrm'


class appsalerInformation:
    # def __init__(self, ip):
    #     self.d = ut2.connect_wifi(ip)

    def __init__(self, device):
        self.d = ut2.connect_usb(device)

    def assert_saler(self, m):
        assert m.exists

    def start_app(self):
        self.d.app_start(package_namesaler)
        phonebrand = self.d.device_info[u"brand"]
        print(self.d.device_info)
        print(phonebrand)
        print(type(phonebrand))
        time.sleep(5)
        if self.d(resourceId="android:id/up").exists:
            self.d(resourceId="android:id/up").click()
        else:
            pass
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").click()

        else:
            pass
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/message").exists:
            self.salerBack()
            pass
        else:
            pass
        return phonebrand

    def backCommonMethod(self):
        while True:
            if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").exists:
                break
            else:
                self.salerBack()
                continue

    def appsalerHomepage_lunbotu(self):  # 轮播图首页
        for i in range(1, 5):
            self.swipeup()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_back_to_top").click()
        time.sleep(2)
        # homepagetext = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"乳品饮料").info[u"text"]
        # s = "乳品饮料" in homepagetext
        # print(s)
        # assert "乳品饮料" in homepagetext
        # 首页各种类型的点击
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(3)
        assert "全部品牌" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"]
        self.backCommonMethod()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview").click()
        pass

        # if "积分商城" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview").info[u"text"]:
        #     self.d(description=u"参与兑换").click()
        # else:
        #     self.backCommonMethod()

    def appsalerjxs(self):  # 默认经销商

        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_icon",
               className="android.widget.ImageView", instance=1).click()
        # 选择默认经销商
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_brand_bg").click()
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                  instance=5).exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                   instance=5).click()
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                    instance=4).exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                   instance=4).click()
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                    instance=3).exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                   instance=3).click()
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                    instance=2).exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                   instance=2).click()
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                    instance=1).exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon", className="android.widget.CheckBox",
                   instance=1).click()
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/icon").click()

        else:
            pass
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            pass
        else:
            pass
        # self.d.app_stop(package_namesaler)
        # self.d.app_clear(package_namesaler)
        # return salername,salerpwd

    def appsaler_stop(self):  # 退出salerapp
        self.d.app_stop(package_namesaler)
        self.d.app_clear(package_namesaler)

    def salerlogintrue(self, salername, salerpwd):  # 登录saler
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            # time.sleep(3)
            # if self.d("android:id/up").exists:
            # self.d("android:id/up").click()
            # time.sleep(3)
            # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
            # time.sleep(3)
            # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
            # else:
            # pass
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
        else:
            pass
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
        else:
            pass
        return salername, salerpwd

    def salermodifypwd(self, oldpwd, newpwd):  # 修改密码
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview").click()
        self.asserttext("修改密码")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/modify_pwd_edv_old_pwd").set_text(oldpwd)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/modify_pwd_edv_pwd1").set_text(newpwd)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/modify_pwd_edv_pwd2").set_text(newpwd)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/modify_pwd_btv_modify").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(2)
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists
        return oldpwd, newpwd

    def salerloginOff(self):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=6).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()

    #
    # def salerChecknewvison(self):
    #     self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
    #     self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()

    def salerHuionline(self, phonebrand):
        # 客服电话
        kefudianhua = "4006870066"
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠聊").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠聊").click()
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
        else:
            pass
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_im_msg").exists
        # 找客服
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print(phonebrand)
        # print("111111111111")
        # if "OPPO" == phonebrand:
        #     s = self.d(resourceId="com.android.contacts:id/new_contact_name").info[u"text"]
        # elif "huawei" in phonebrand:
        #     s = self.d(resourceId="com.android.contacts:id/new_contact_name").info[u"text"]
        # m = re.sub('\s','',s)
        # if m == kefudianhua:
        #     print (m)
        # else:
        #     print (s)
        #     pass
        time.sleep(3)
        # self.d(resourceId="com.android.systemui:id/back").click()
        self.d.press("back")
        time.sleep(3)
        # 三个导航栏切换
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_system_msg").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_im_friend_state").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_im_msg").click()
        # 通讯录
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        # 通讯录电话
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/call_phone").click()
        time.sleep(3)
        print(phonebrand)
        time.sleep(2)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/search_input").send_keys("14161915041")
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_head").click()
        # 经销商信息
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        # assert self.d(Description=u"配送服务水平").exists
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        self.salerBack()
        # 发送表情，文字，语音，图片，位置
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/buttonMoreFuntionInText").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/textView", text=u"位 置").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()  # 位置
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/textView", text=u"照 片").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/picker_photofolder_cover").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/picker_photo_grid_item_select").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/picker_bottombar_select").click()  # 照片
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/textView").click()
        time.sleep(3)
        self.d.press("camera")
        self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/buttonSend").click()  # 拍照
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/emoji_button").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imgEmoji", className="android.widget.ImageView",
               instance=9).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/buttonSendMessage").click()
        self.d(className="android.widget.ImageButton", instance=1).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/sticker_thumb_image",
               className="android.widget.ImageView", instance=1).click()
        self.d(className="android.widget.ImageButton", instance=2).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/sticker_thumb_image",
               className="android.widget.ImageView", instance=2).click()
        self.d(className="android.widget.ImageButton", instance=3).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/sticker_thumb_image",
               className="android.widget.ImageView", instance=2).click()  # 发送表情
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/editTextMessage").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/editTextMessage").set_text(
            u"fdsjfldsjfld水电费老家的雷锋精神敦伦尽分123")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/buttonSendMessage").click()  # 发送文字和字符
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_chat_head3_saler").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        # self.salerBack()
        time.sleep(3)
        self.d.press("back")
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_chat_head2_saler").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/dialog_call_phone_btn_cancle").click()
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        # self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_chat_head1_saler").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_to_chat").click()#惠议价仓库

    def salerHuionline_youhuiquan(self):  # 惠聊发优惠券
        self.d.app_start(package_namesaler)
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        self.salerBack()
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_msg_title").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_msg_title").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_get_it").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
            print(1111)
        else:
            print(222222)
            pass

    def salerMyinformation(self, name, storeName, Address):  # 我的信息
        photo_brand = (self.d.device_info[u"brand"])
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/wtv_store_name").click()
        # self.asserttext(u"个人中心")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/store_configuration").click()
        # self.asserttext(u"我的信息")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/buns_perfect").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_personPhoto").click()#拍照
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/camera_btn").click()
        # time.sleep(5)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm: id/open_camera").click()
        # time.sleep(5)
        # self.d.press("camera")
        # time.sleep(3)
        # self.d(resourceId="com.huawei.camera:id/shutter_button").click()
        # time.sleep(3)
        #
        #
        #
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/iv_addimg").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        # time.sleep(3)
        # self.d.press("camera")
        # time.sleep(3)
        # #不同手机的点击
        # #huawei
        # if "HUAWEI" in photo_brand:
        #     self.d(resourceId="com.huawei.camera:id/shutter_button").click()
        #     self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
        #     self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定", className="android.widget.ImageButton", instance=1).click()
        # elif "OPPO" in photo_brand:
        #     print(1)
        # elif "xiaomi" in photo_brand:
        #     print(2)
        # else:
        #     print(1)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        # self.salerBack()
        # time.sleep(3)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_salesName").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_text").set_text(name)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_storeName").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_text").set_text(storeName)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_salesAddress").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_text").set_text(Address)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        # time.sleep(2)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        time.sleep(2)
        self.salerBack()

        # 地址管理

    def salerAddrmanage(self, add_name, add_mobile, add_address, add_code):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/address_manager").click()
        self.asserttext(u"地址管理")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_add").click()
        self.asserttext(u"新建地址")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/name_et").set_text(add_name)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/mobile_et").set_text(add_mobile)
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/address_tv").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname", text=u"北京市").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/detail_address_et").set_text(add_address)
        time.sleep(2)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/post_code_et").set_text(add_code)
        time.sleep(2)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/address_save_btn").click()
        time.sleep(2)
        assert_that("地址管理")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()

    def salerAddrdelete(self):  # 地址删除
        begin = len(self.d(className="android.widget.CheckBox"))
        print(begin)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/cb_check",
               className="android.widget.CheckBox").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        end = len(self.d(className="android.widget.CheckBox"))
        print(end)
        assert_that(begin - end == 1)
        pass

    def salerAddshopping_1(self):  # 添加仓库
        for i in range(1, 5):
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/category_item",
               className="android.widget.RelativeLayout", instance=1).click()
        for i in range(1, 2):
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()

    def salerEntershopping_Cart(self):  # 倉庫的選完了
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        pass

    def salerEnterAdveeorder(self):  # 购物车的选完了
        tv_state = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_state").info[u"text"]
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        return tv_state
        pass

    def salerEnterOrder(self):  # 预订单的选完了(不选择优惠券)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(2)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        else:
            pass
        tv_order_money = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_order_money").info[u"text"]
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_order_look").click()  # 查看订单
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_textview").exists:
            self.salerBack()
            print("ok")
            pass
        else:
            self.salerBack()
            print("not_ok")
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_rob").click()
        time.sleep(3)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        return tv_order_money

    def salerEnterOrder_check(self):  # 预订单的选完了(选择优惠券)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/coupons_num_TV").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/mcoupon_select").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_exception").exists:
            tv_exception = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_exception").info[u"text"]
            pass
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_pay_method").exists:
            tv_exception = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_pay_method").info[u"text"]
            pass
        else:
            pass
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_order_look").click()  # 查看订单
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_textview").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/retail_order_count_v").click()
            time.sleep(2)
            ordercode = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/orderid_textview").info[u"text"]
            self.salerBack()
            time.sleep(2)
            self.salerBack()
            print("ok")
            pass
        else:
            self.salerBack()
            print("not_ok")
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_rob").click()  #
        time.sleep(3)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        return tv_exception, ordercode

    def salerAdverorder(self, et_code, et_message):  # 预订单操作
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").click()
        for i in range(1, 3):
            self.swipeup()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_code").set_text(et_code)
        time.sleep(2)
        self.salerBack()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_message").set_text(et_message)
        time.sleep(2)
        self.salerBack()
        sum_money_textview = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/sum_money_textview").info[
            u"text"]
        actual_payment_textview = \
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/actual_payment_textview").info[u"text"]
        return sum_money_textview, actual_payment_textview

    pass

    def salerBack(self):
        self.d.press("back")
        pass

    def salerAddshopping(self, count):  # 惠聊添加商品。。。
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_chat_head1_saler").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text(count)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.d.press("back")
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(2)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        else:
            pass

        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(4)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_chat_head3_saler").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/conect_online_dealer").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_order_count").click()  # 惠聊订单详情

    def salerOrder_problem1(self, tv_count1, tv_count2, tv_count3):  # 异常订单>1500的订单(使用优惠券)
        self.salerEnterstorehouse()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text(tv_count1)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        self.salerEntershopping_Cart()
        self.salerEnterAdveeorder()
        tv_exception1, ordercode = self.salerEnterOrder_check()
        #
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text(tv_count2)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        self.salerEntershopping_Cart()
        self.salerEnterAdveeorder()
        tv_exception2 = self.salerEnterOrder()
        print(1)
        #
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text(tv_count3)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        self.salerEntershopping_Cart()
        self.salerEnterAdveeorder()
        tv_exception3 = self.salerEnterOrder_check()
        return tv_exception1, tv_exception2, tv_exception3, ordercode

    def salerEnterstorehouse(self):  # 进入仓库
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").click()
        else:
            self.salerBack()
        time.sleep(2)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_back_to_top").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_back_to_top").click()
        else:
            pass
        time.sleep(2)
        # self.d.swipe(360,1000,360,100)
        # time.sleep(2)
        # self.d.swipe(360,1000,360,100)
        # time.sleep(2)
        # self.d.swipe(360,1000,360,150)
        # time.sleep(2)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_brand_bg", className="android.widget.ImageView", instance=1).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"食品糖果").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"百事").click()
        time.sleep(2)

    def salerPromotion(self):  # 促销信息
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists:
            shopPromotion1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").info[
                u"text"]  # 商品促销信息
        else:
            shopPromotion1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_discount").exists:  # 品牌促销信息
            banerProtion1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_discount").info[u"text"]
        else:
            banerProtion1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_discount").exists
        # print banerProtion
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
            self.d.press("back")
        else:
            pass
        time.sleep(3)
        assert_that("购物车" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"])
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists:
            shopPromotion2 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").info[u"text"]
        else:
            shopPromotion2 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists
        #
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        assert "提交订单" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"]
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists:
            jxsProtion = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").info[u"text"]
        else:
            jxsProtion = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/promotion_title").exists
        return shopPromotion1, shopPromotion2, banerProtion1, jxsProtion

    def salerjxsStorehouse(self, sousuo, phonebanner):  # 经销商仓库
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/Img_shop_image_logo").click()
        time.sleep(2)
        assert "经销商" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"]
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_call_phone").click()
        time.sleep(3)
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title_img").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt_search").set_text(sousuo)
        if "HUAWEI" in phonebanner:
            self.d.click(0.925, 0.900)
            print("HUAWEI")
        elif "OPPO" in phonebanner:
            self.d.click(0.905, 0.913)
            print("oppo")
        time.sleep(3)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").exists:
            self.salerBack()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title_img").click()
            print("删除搜索记录")
            time.sleep(2)
            assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_del").exists
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_del").click()
            time.sleep(5)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        else:
            print("lllll")

    def salerShoppingCart(self):  # 购物车

        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_decrease").click()  # 减
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()  # 加
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/all_checked").click()  # 全选
        self.d(className="android.widget.CheckBox").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/empty_iv").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/empty_iv").click()
            time.sleep(3)
            self.salerBack()
            pass
        else:
            pass
        time.sleep(2)
        self.salerBack()
        pass

    def salerUpgrade(self, name, phonebrand):  # 升级
        from pymssqlManage import salerSql
        row1 = salerSql.salersql_appinfo(name)
        print(row1[0]), print(row1[1])
        l1 = int(str((row1[1])).replace('.', ''))
        print(l1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=3).click()
        msg = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/dlg_cmmn_alert_msg").info[u"text"]
        print(msg)
        if "最新版本" in str(msg):
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
            row2 = salerSql.salersql_appinfo(name)
            print(row2[0]), print(row2[1])
            assert row1[1] == row2[1]
            pass
        # 升级
        elif self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            pass
            time.sleep(5)
            for i in range(1, 200):
                print(i)
                time.sleep(5)
                if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/progress_title").exists:
                    continue
                else:
                    break
            print("下载完成")
            time.sleep(3)
            self.d(resourceId="com.android.packageinstaller:id/ok_button").click()
            if "OPPO" in phonebrand:
                self.d(resourceId="com.android.packageinstaller:id/bottom_button_two").click()
            elif "huawei" in phonebrand:
                self.d(resourceId="com.android.packageinstaller:id/done _button").click()
            else:
                print("机型=" + phonebrand)
            time.sleep(3)
            row2 = salerSql.salersql_appinfo(name)
            l2 = int(str((row2[1])).replace('.', ''))
            print(l2)
            assert l2 > l1
            pass
            self.salerBack()
        return msg

    def salerNewTv(self, edt_title, edit_info):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠TV").click()
        tvname = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_tittle").info[u"text"]
        name = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_nickname").info[u"text"]
        print(tvname)
        print(name)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/mtv_record_video").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/record").click()
        time.sleep(6)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/record").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/filter_image", className="android.widget.ImageView", instance=3).click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt_title").set_text(edt_title)  # 视频标题
        self.salerBack()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_publish").click()
        time.sleep(1)
        while True:
            if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/upload_thumbnail_img").exists:
                time.sleep(3)
                continue
            else:
                break

        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/dlg_cmmn_alert_msg").exists:
            time.sleep(2)
            result = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/dlg_cmmn_alert_msg").exists
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_left_btn").click()

            print(result)
            pass
        else:
            result = "没有惠现金"
            print(result)
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/msetting").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_sex").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/setting_male").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_signature").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit_info").clear_text()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit_info").set_text(edit_info)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/iv_headimg").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/open_album").click()
        self.d(resourceId="com.android.gallery3d:id/album_cover_image").click()
        self.d(resourceId="com.android.gallery3d:id/gl_root_cover").click()
        self.d(resourceId="com.android.gallery3d:id/head_select_right").click()
        self.d(resourceId="com.android.gallery3d:id/head_select_right").click()
        time.sleep(2)
        self.salerBack()
        return tvname, name, edt_title, edit_info, result

    def salerNewTvshou(self, htvtext):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠TV").click()
        newtvname = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_tittle").info[u"text"]
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_image").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_collect").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_like").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_follow").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_barrage_switch").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_comment_more").click()
        time.sleep(2)
        self.salerBack()
        time.sleep(4)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_commentary").set_text(htvtext)
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_send_commentary").click()
        # self.d(className="com.tencent.liteav.txcvodplayer.h").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_play").click()
        # self.d(className="com.tencent.liteav.txcvodplayer.h").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_play").click()
        # time.sleep(3)
        # self.d(className="com.tencent.liteav.txcvodplayer.h").click()
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_video_fullscreen").click()

        time.sleep(1)
        self.salerBack()
        return newtvname

    def salerNewTv_RecommendingCommodities(self, htvname):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"惠TV").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt_search").send_keys(htvname)
        self.d.click(0.914, 0.913)
        self.d(text=u"视频").click()
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_image").exists
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/new_tv_item_image").click()
        time.sleep(3)
        RecommendingCommodities1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_title").info[u"text"]
        print(RecommendingCommodities1)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/img_buy").click()
        self.backCommonMethod()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").click()
        self.d(className="android.widget.TextView", instance=2).click()
        time.sleep(3)
        RecommendingCommodities2 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_title").info[u"text"]
        assert RecommendingCommodities2 == RecommendingCommodities1
        return RecommendingCommodities1, RecommendingCommodities2

    def finishorder(self):  # 完成订单
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").exists:
            pass
        else:
            self.d.press("back")
            time.sleep(2)
            self.d.press("back")
            time.sleep(2)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(3)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/iv_receiving").click()
        time.sleep(3)
        while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
            time.sleep(3)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(3)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
            time.sleep(3)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
            time.sleep(5)
        else:
            pass
        self.d.press("back")
        time.sleep(3)

    def salerAllorders(self):  # 全部订单
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rl_all_order").click()
        assert "全部订单" in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"]
        time.sleep(3)
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/orderTimeTV").info[u"text"] not in ""
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/orderTypeTV").info[u"text"] not in ""
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_textview").info[u"text"] not in ""
        assert self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/payreceive_money").info[u"text"] not in ""

    def salerGoodsshelves(self, search_name, search_price, search_status, phonebrand):
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title_img").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt_search").set_text(search_name)
        if "OPPO" in phonebrand:
            self.d.click(0.927, 0.956)
        elif "HONOR" in phonebrand:
            self.d.click(0.949, 0.898)
        else:
            pass
        assert search_status in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_state").info[u"text"]
        assert search_price in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_discountprice").info[
            u"text"]
        self.salerBack()
        pass

    def salerjxsManagesaler(self, type):
        if "默认" in type:
            num = len(self.d(className="android.widget.TextView"))
            print(num)
            assert num >= 20
        else:
            num = len(self.d(className="android.widget.TextView"))
            print(num)
            assert 1 <= num <= 10

    def asserttext(self, x, ):
        assert_that(x in self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").info[u"text"])

    def swipeup(self):
        self.d.swipe(500, 1000, 500, 300)

    def salerLog_banben(self, a, b):
        log = open(a, 'a+', encoding='utf-8')
        log.write(
            '\n' + b + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime()) + '\n')
        log.close()

    def appscreenshot(self):  # 截图
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file = r'E:/banben'
        # self.d.screenshot('%s/%s.jpg'%(file,timestamp))
        self.d.screenshot('%s.jpg' % (timestamp))
        # pictruename = '%s\%s.jpg'%(file,timestamp)
        pictruename = '%s.jpg' % (timestamp)
        print(pictruename)
        return pictruename

    def register(self, mobile, shopname,shopusername,address,ydcode,devcode,didcode,imeicode,weburl, username, password):
        import pyodbc
        #UAT
        #conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL_UAT', '192.168.60.3', 'Retail_Uat_AutoTest', 'z1ZjXP6dkkkbScJ4')
        #RETAIL
        conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s' % ('CRM_RETAIL', '118.186.244.9', 'fanhanqing', 'rVbGrebhsFow0NUV')
        cnxn = pyodbc.connect(conn_info)
        sqlname = "SELECT * FROM[dbo].[CRM_WS_CUSTOMER] WITH(nolock) WHERE MOBILE = '" + mobile + "'"
        cursor = cnxn.cursor()
        cursor.execute(sqlname)
        row = cursor.fetchone()
        print(row)
        if row == None:
            self.d.app_start(package_namesaler)
            time.sleep(5)
            if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_register").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_register").click()
                time.sleep(3)
                if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/check_dlg_cmmn_alert_msg").exists:
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
                    print("该设备已经注册过门店账号，请更换设备重试！")
                    webgetimei = wangyeInfomation()
                    webgetimei.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetimei.wangyeclickId("menuGroup_mdglnew")
                    print("点击门店管理")
                    time.sleep(5)
                    webgetimei.wangyeclickId("a_menuId_listCustomerSaler")
                    print("点击门店人员信息管理")
                    time.sleep(5)
                    webgetimei.wangeyqiehuaniframe("main1")
                    webgetimei.browser.find_element_by_xpath("//*[@id='searchbox']/table/tbody/tr[1]/td[12]/input").send_keys(imeicode)
                    print("imei"+imeicode)
                    time.sleep(5)
                    webgetimei.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getimeinum = webgetimei.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getimeinum[2] == "找":
                        print("没有imei记录")
                        pass
                    else:
                        webgetimei.browser.find_element_by_xpath("//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a[2]/img").click()
                        time.sleep(5)
                        webgetimei.browser.find_element_by_name("imei").clear()
                        time.sleep(5)
                        webgetimei.wangyeclickId("save")
                        print("解除imei绑定")
                    time.sleep(5)
                    webgetimei.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    print("登录后台删除登录次数限制")
                    time.sleep(3)
                    webgetdev = wangyeInfomation()
                    webgetdev.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetdev.wangyeclickId("menuGroup_CrmDevLoginWhitelists")
                    print("点击设备登录白名单")
                    time.sleep(5)
                    webgetdev.wangyeclickId("a_menuId_deleteDev")
                    print("点击删除登录次数限制")
                    time.sleep(5)
                    webgetdev.wangeyqiehuaniframe("main1")
                    webgetdev.wangyesend_keysName("devId", devcode)
                    print("输入dev：" + devcode)
                    time.sleep(5)
                    webgetdev.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getnumber = webgetdev.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getnumber[2] == "找":
                        print("没有dev记录")
                        pass
                    elif int(getnumber[2]) > 0:
                        webgetdev.browser.find_element_by_xpath("//*[@id='cloneTable']/table/thead/tr[2]/td[1]/input").click()
                        time.sleep(2)
                        webgetdev.wangyeclickId("delAll")
                        time.sleep(2)
                        webgetdev.browser.switch_to.alert.accept()
                        time.sleep(5)
                        webgetdev.browser.switch_to.alert.accept()
                        print("删除全部设备登录记录")
                        time.sleep(5)
                    webgetdev.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    print("登录后台删除树盟限制")
                    time.sleep(3)
                    webgetdid = wangyeInfomation()
                    webgetdid.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetdid.wangyeclickId("menuGroup_CrmDevLoginWhitelists")
                    print("点击设备登录白名单")
                    time.sleep(5)
                    webgetdid.wangyeclickId("a_menuId_deleteDid")
                    print("点击删除树盟限制")
                    time.sleep(5)
                    webgetdid.wangeyqiehuaniframe("main1")
                    webgetdid.wangyesend_keysName("did", didcode)
                    print("输入did：" + didcode)
                    time.sleep(5)
                    webgetdid.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getdidnumber = webgetdid.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getdidnumber[2] == "找":
                        print("没有did记录")
                        pass
                    elif int(getdidnumber[2]) > 0:
                        webgetdid.browser.find_element_by_xpath("//*[@id='cloneTable']/table/thead/tr[2]/td[1]/input").click()
                        time.sleep(2)
                        webgetdid.wangyeclickId("delAll")
                        time.sleep(2)
                        webgetdid.browser.switch_to.alert.accept()
                        time.sleep(5)
                        webgetdid.browser.switch_to.alert.accept()
                        print("删除全部did记录")
                        time.sleep(5)
                    webgetdid.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    self.d.app_start(package_namesaler)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone").clear_text()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone").send_keys(mobile)
                    print("注册手机号: " + mobile)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_obtain_verify_code").click()
                    print("点击获取验证码")
                    time.sleep(5)
                    webgetcode = wangyeInfomation()
                    webgetcode.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetcode.wangyeclickId("menuGroup_mdglnew")
                    print("点击门店管理")
                    time.sleep(5)
                    webgetcode.wangyeclickId("a_menuId_listCustomerSaler")
                    print("点击门店人员信息管理")
                    time.sleep(5)
                    webgetcode.wangeyqiehuaniframe("main1")
                    webgetcode.wangyesend_keysName("$lk_mobile", mobile)
                    print("输入用户名：" + mobile)
                    time.sleep(5)
                    webgetcode.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(10)
                    vcode = webgetcode.browser.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[19]").text
                    print("手机验证码：" + vcode)
                    time.sleep(5)
                    webgetcode.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    self.d.app_start(package_namesaler)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_verify_code").clear_text()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_verify_code").send_keys(vcode)
                    print("验证码：" + vcode)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").send_keys("auto2018")
                    print("输入新密码:auto2018")
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd_again").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd_again").send_keys("auto2018")
                    print("再次输入密码:auto2018")
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_shop_name").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_shop_name").send_keys(shopname)
                    print("门店名称：" + shopname)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_user_name").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_user_name").send_keys(shopusername)
                    print("店主姓名：" + shopusername)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_area").click()
                    time.sleep(15)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_street").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_street").send_keys(address)
                    print("收货地址：" + address)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_saler_channel").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/camera_btn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/shutter_button").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定",
                           className="android.widget.ImageButton", instance=1).click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/camera_btn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/open_camera").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/shutter_button").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定",
                           className="android.widget.ImageButton", instance=1).click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_invite_code_view").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_invite_code_view").send_keys(ydcode)
                    print("邀请码：" + ydcode)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    print("注册成功")
                    self.d.app_stop(package_namesaler)
                    print("关闭app")
                else:
                    time.sleep(5)
                    webgetimei = wangyeInfomation()
                    webgetimei.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetimei.wangyeclickId("menuGroup_mdglnew")
                    print("点击门店管理")
                    time.sleep(5)
                    webgetimei.wangyeclickId("a_menuId_listCustomerSaler")
                    print("点击门店人员信息管理")
                    time.sleep(5)
                    webgetimei.wangeyqiehuaniframe("main1")
                    webgetimei.browser.find_element_by_xpath("//*[@id='searchbox']/table/tbody/tr[1]/td[12]/input").send_keys(imeicode)
                    print("imei" + imeicode)
                    time.sleep(5)
                    webgetimei.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getimeinum = webgetimei.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getimeinum[2] == "找":
                        print("没有imei记录")
                        pass
                    else:
                        webgetimei.browser.find_element_by_xpath("//*[@id='ec_table']/tbody/tr[1]/td[3]/center/a[2]/img").click()
                        time.sleep(5)
                        webgetimei.browser.find_element_by_name("imei").clear()
                        time.sleep(5)
                        webgetimei.wangyeclickId("save")
                        print("解除imei绑定")
                    time.sleep(5)
                    webgetimei.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    print("登录后台删除登录次数限制")
                    time.sleep(3)
                    webgetdev = wangyeInfomation()
                    webgetdev.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetdev.wangyeclickId("menuGroup_CrmDevLoginWhitelists")
                    print("点击设备登录白名单")
                    time.sleep(5)
                    webgetdev.wangyeclickId("a_menuId_deleteDev")
                    print("点击删除登录次数限制")
                    time.sleep(5)
                    webgetdev.wangeyqiehuaniframe("main1")
                    webgetdev.wangyesend_keysName("devId", devcode)
                    print("输入dev：" + devcode)
                    time.sleep(5)
                    webgetdev.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getnumber = webgetdev.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getnumber[2] == "找":
                        print("没有dev记录")
                        pass
                    elif int(getnumber[2]) > 0:
                        webgetdev.browser.find_element_by_xpath("//*[@id='cloneTable']/table/thead/tr[2]/td[1]/input").click()
                        time.sleep(2)
                        webgetdev.wangyeclickId("delAll")
                        time.sleep(2)
                        webgetdev.browser.switch_to.alert.accept()
                        time.sleep(5)
                        webgetdev.browser.switch_to.alert.accept()
                        print("删除全部设备登录记录")
                        time.sleep(5)
                    webgetdev.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    print("登录后台删除树盟限制")
                    time.sleep(3)
                    webgetdid = wangyeInfomation()
                    webgetdid.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetdid.wangyeclickId("menuGroup_CrmDevLoginWhitelists")
                    print("点击设备登录白名单")
                    time.sleep(5)
                    webgetdid.wangyeclickId("a_menuId_deleteDid")
                    print("点击删除树盟限制")
                    time.sleep(5)
                    webgetdid.wangeyqiehuaniframe("main1")
                    webgetdid.wangyesend_keysName("did", didcode)
                    print("输入did：" + didcode)
                    time.sleep(5)
                    webgetdid.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(5)
                    getdidnumber = webgetdid.browser.find_element_by_xpath("//*[@id='turnPage']/div[3]/table/thead/tr/td/table/tbody/tr/td[1]").text
                    if getdidnumber[2] == "找":
                        print("没有did记录")
                        pass
                    elif int(getdidnumber[2]) > 0:
                        webgetdid.browser.find_element_by_xpath("//*[@id='cloneTable']/table/thead/tr[2]/td[1]/input").click()
                        time.sleep(2)
                        webgetdid.wangyeclickId("delAll")
                        time.sleep(2)
                        webgetdid.browser.switch_to.alert.accept()
                        time.sleep(5)
                        webgetdid.browser.switch_to.alert.accept()
                        print("删除全部did记录")
                        time.sleep(5)
                    webgetdid.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    self.d.app_start(package_namesaler)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone").clear_text()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_phone").send_keys(mobile)
                    print("注册手机号: " + mobile)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_obtain_verify_code").click()
                    print("点击获取验证码")
                    time.sleep(5)
                    webgetcode = wangyeInfomation()
                    webgetcode.wangyeLogin(weburl, username, password)
                    print("登录后台")
                    time.sleep(5)
                    webgetcode.wangyeclickId("menuGroup_mdglnew")
                    print("点击门店管理")
                    time.sleep(5)
                    webgetcode.wangyeclickId("a_menuId_listCustomerSaler")
                    print("点击门店人员信息管理")
                    time.sleep(5)
                    webgetcode.wangeyqiehuaniframe("main1")
                    webgetcode.wangyesend_keysName("$lk_mobile", mobile)
                    print("输入用户名：" + mobile)
                    time.sleep(5)
                    webgetcode.wangyeclickId("query_A")
                    print("点击查询")
                    time.sleep(10)
                    vcode = webgetcode.browser.find_element_by_xpath(".//*[@id='ec_table']/tbody/tr/td[19]").text
                    print("手机验证码：" + vcode)
                    time.sleep(5)
                    webgetcode.wangyeQuit()
                    print("退出后台")
                    time.sleep(2)
                    self.d.app_start(package_namesaler)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_verify_code").clear_text()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_verify_code").send_keys(vcode)
                    print("验证码：" + vcode)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").send_keys("auto2018")
                    print("输入新密码:auto2018")
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd_again").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd_again").send_keys("auto2018")
                    print("再次输入密码:auto2018")
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_shop_name").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_shop_name").send_keys(shopname)
                    print("门店名称：" + shopname)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_user_name").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_user_name").send_keys(shopusername)
                    print("店主姓名：" + shopusername)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_area").click()
                    time.sleep(15)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_areaname").click()
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_street").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_street").send_keys(address)
                    print("收货地址：" + address)
                    time.sleep(2)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_saler_channel").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/camera_btn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/shutter_button").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定",className="android.widget.ImageButton", instance=1).click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/camera_btn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/open_camera").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/shutter_button").click()
                    time.sleep(5)
                    self.d(resourceId="com.huawei.camera:id/btn_review_confirm").click()
                    time.sleep(5)
                    self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定",className="android.widget.ImageButton", instance=1).click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_invite_code_view").clear_text()
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_invite_code_view").send_keys(ydcode)
                    print("邀请码：" + ydcode)
                    time.sleep(5)
                    self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
                    time.sleep(5)
                    print("注册成功")
                    self.d.app_stop(package_namesaler)
                    print("关闭app")
            else:
                print("注册页面加载失败")
                pass
        else:
            print("手机号已被注册，请更换手机号")
            pass

    def cancelorders(self,salername,salerpwd):
        self.d.app_start(package_namesaler)
        print("取消订单初始化")
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("点击全部品牌")
        time.sleep(5)
        if self.d(text=u"百事").exists:
            self.d(text=u"百事").click()
            time.sleep(5)
        else:
            while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                if self.d(text=u"百事").exists:
                    self.d(text=u"百事").click()
                    time.sleep(5)
                    break
                else:
                    continue
        print("选择品牌:百事，进入默认经销商仓库")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").clear_text()
        # time.sleep(10)
        #self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text("1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/prod_cart").click()
        time.sleep(5)
        print("加入购物车")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        time.sleep(5)
        print("购买数量：1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        print("	确定")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("选完了")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.d.press("back")
            time.sleep(5)
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("去结算")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(5)
        print("确认订单")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(5)
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        print("完成订单")
        self.salerBack()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(5)
        ordersum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dot").get_text()
        print("门店待确认订单笔数："+ordersum)
        time.sleep(5)
        dealer = appdealerInformation("QDY7N17405002857")
        dealer.dealerstart_app()
        print("启动经销商app")
        time.sleep(5)
        dealer.dealerlogin("14161915041","915041new")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"订单管理").click()
        time.sleep(5)
        dealerordersum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/num_new_count").get_text()
        print("经销商待确认订单笔数：" + dealerordersum)
        if ordersum == dealerordersum:
            print("门店待确认订单笔数==经销商待确认订单笔数")
        else:
            print("门店待确认订单笔数!=经销商待确认订单笔数")
        self.d.app_start(package_namesaler)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_send_goods").click()
        time.sleep(5)
        print("进入待确认页面")
        while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
            time.sleep(5)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(5)
            self.d(text=u"试试怎么用").click()
            print("取消订单原因：试试怎么用")
            time.sleep(5)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/applybtn").click()
            time.sleep(5)
            if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
                time.sleep(5)
            else:
                pass
        else:
            print("待确认列表无订单")
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("退出登录")
        time.sleep(5)
        dealer.dealerstart_app()
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item").click()
        print("进入经销商待确认页面")
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").exists:
            print("取消订单后，经销商待确认订单数量显示异常")
        else:
            print("取消订单后，经销商待确认订单数量显示正常")
        self.d.press("back")
        dealer.dealerOfflogin()

    def dealercancelorders(self,salername,salerpwd):
        self.d.app_start(package_namesaler)
        print("取消订单初始化")
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("点击全部品牌")
        time.sleep(5)
        if self.d(text=u"百事").exists:
            self.d(text=u"百事").click()
            time.sleep(5)
        else:
            while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                if self.d(text=u"百事").exists:
                    self.d(text=u"百事").click()
                    time.sleep(5)
                    break
                else:
                    continue
        print("选择品牌:百事，进入默认经销商仓库")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").clear_text()
        # time.sleep(10)
        #self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text("1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/prod_cart").click()
        time.sleep(5)
        print("加入购物车")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        time.sleep(5)
        print("购买数量：1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        print("	确定")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("选完了")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.d.press("back")
            time.sleep(5)
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("去结算")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(5)
        print("确认订单")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(5)
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        print("完成订单")
        self.salerBack()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(5)
        ordersum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dot").get_text()
        print("门店待确认订单笔数："+ordersum)
        time.sleep(5)
        dealer = appdealerInformation("QDY7N17405002857")
        dealer.dealerstart_app()
        print("启动经销商app")
        time.sleep(5)
        dealer.dealerlogin("14161915041","915041new")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"订单管理").click()
        time.sleep(5)
        dealerordersum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/num_new_count").get_text()
        print("经销商待确认订单笔数：" + dealerordersum)
        if ordersum == dealerordersum:
            print("门店待确认订单笔数==经销商待确认订单笔数")
        else:
            print("门店待确认订单笔数!=经销商待确认订单笔数")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item").click()
        print("进入经销商待确认页面")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").click()
        print("进入经销商待确认-订单详情页")
        time.sleep(5)
        self.d.swipe(360, 1000, 360, 100)
        print("滑动订单至详情页底部")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/cancel_button").click()
        print("经销商取消订单")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("经销商确认取消订单")
        time.sleep(5)
        self.d(text=u"无此门店").click()
        print("经销商取消订单原因：无此门店")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/applybtn").click()
        print("提交")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        print("确认")
        time.sleep(5)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").exists:
            print("经销商取消订单失败，经销商待确认列表有订单")
        else:
            print("经销商取消订单成功，经销商待确认列表无订单")
        time.sleep(5)
        print("启动门店app")
        self.d.app_start(package_namesaler)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_send_goods").click()
        time.sleep(5)
        print("进入待确认页面")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").exists:
            print("经销商取消订单失败，门店待确认列表有订单")
        else:
            print("经销商取消订单成功，门店待确认列表无订单")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("退出登录")
        time.sleep(5)
        dealer.dealerstart_app()
        self.d.press("back")
        dealer.dealerOfflogin()

    def overrideorders(self,salername,salerpwd):
        print("经销商修改订单商品数量，单价初始化")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("点击全部品牌")
        time.sleep(5)
        if self.d(text=u"百事").exists:
            self.d(text=u"百事").click()
            time.sleep(5)
        else:
            while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                if self.d(text=u"百事").exists:
                    self.d(text=u"百事").click()
                    time.sleep(5)
                    break
                else:
                    continue
        print("选择品牌:百事，进入默认经销商仓库")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").clear_text()
        # time.sleep(10)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text("1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/prod_cart").click()
        time.sleep(5)
        print("加入购物车")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        time.sleep(5)
        print("购买数量：1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        print("确定")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("选完了")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.d.press("back")
            time.sleep(5)
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("去结算")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(5)
        print("确认订单")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(5)
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        print("完成订单")
        self.salerBack()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(5)
        ordersum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dot").get_text()
        print("门店待确认订单笔数：" + ordersum)
        time.sleep(5)
        dealer = appdealerInformation("QDY7N17405002857")
        dealer.dealerstart_app()
        print("启动经销商app")
        time.sleep(5)
        dealer.dealerlogin("14161915041", "915041new")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",
               text=u"订单管理").click()
        time.sleep(5)
        dealerordersum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/num_new_count").get_text()
        print("经销商待确认订单笔数：" + dealerordersum)
        if ordersum == dealerordersum:
            print("门店待确认订单笔数==经销商待确认订单笔数")
        else:
            print("门店待确认订单笔数!=经销商待确认订单笔数")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item").click()
        print("进入经销商待确认页面")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_order_button").click()
        print("进入修改订单页面")
        time.sleep(5)
        oldsum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").get_text()
        print("订单商品修改前的数量为："+oldsum)
        time.sleep(5)
        oldprice = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/price_edit_text_one").get_text()
        print("订单商品修改前的单价为：" +oldprice)
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_num_view").clear_text()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_num_view").set_text("5")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        newsum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").get_text()
        print("订单商品修改后的数量为：" + newsum)
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/price_edit_text_one").click()
        time.sleep(5)
        temp = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_change_money_warn").get_text()
        print(temp)
        minprice = int(temp[7]+temp[8])
        maxprice = int(temp[11]+temp[12])
        newprice = minprice+1
        if newprice>=minprice and newprice<=maxprice:
            print("价格修改成功，在价格修改区间内")
        else:
            print("价格修改失败，不在价格修改区间内")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_money_view").clear_text()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_money_view").set_text(newprice)
        print("订单商品修改后的单价为："+str(newprice))
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        self.d.swipe(360, 1000, 360, 100)
        print("滑动订单至底部")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        print("确认修改")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(5)
        self.d(text=u"经销商缺货").click()
        print("修改原因:经销商缺货")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/applybtn").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        print("提交成功")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        print("确认订单")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/cb_reason").click()
        print("选择送货司机")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        print("确认")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item",className="android.widget.ImageView",instance=1).click()
        print("进入待发货页面")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_order_button").click()
        print("进入修改订单页面")
        time.sleep(5)
        oldsum1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").get_text()
        print("订单商品修改前的数量为：" + oldsum1)
        time.sleep(5)
        oldprice1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/price_edit_text_one").get_text()
        print("订单商品修改前的单价为：" + oldprice1)
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_num_view").clear_text()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_num_view").set_text(str(int(newsum)-1))
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        newsum1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_count_one").get_text()
        print("订单商品修改后的数量为：" + newsum1)
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/price_edit_text_one").click()
        time.sleep(5)
        temp1 = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_change_money_warn").get_text()
        print(temp1)
        minprice1 = int(temp1[7] + temp1[8])
        maxprice1 = int(temp1[11] + temp1[12])
        newprice1 = maxprice1 - 1
        if newprice1 >= minprice1 and newprice1 <= maxprice1:
            print("价格修改成功，在价格修改区间内")
        else:
            print("价格修改失败，不在价格修改区间内")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_money_view").clear_text()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/wgt_input_prod_money_view").set_text(newprice1)
        print("订单商品修改后的单价为：" + str(newprice1))
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        self.d.swipe(360, 1000, 360, 100)
        print("滑动订单至底部")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        print("确认修改")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(5)
        self.d(text=u"经销商缺货").click()
        print("修改原因:经销商缺货")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/applybtn").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        print("提交成功")
        time.sleep(5)
        self.d.app_start(package_namesaler)
        print("启动门店app，检查经销商修改后的订单与门店是否显示一致")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/iv_receiving").click()
        print("进入待收货页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/retail_order_count_v").click()
        print("进入订单详情页面")
        time.sleep(5)
        odernum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/number_one_textview").get_text()
        print("门店订单数量："+odernum)
        time.sleep(5)
        oderprice = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/price_one_textview").get_text()
        print("门店订单单价：" + oderprice)
        time.sleep(5)
        if odernum == newsum1 and oderprice == newprice1:
            print("门店订单数量，单价==经销商订单数量，单价")
        else:
            print("门店订单数量，单价==经销商订单数量，单价")
        self.salerBack()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")
        time.sleep(5)
        dealer.dealerstart_app()
        print("启动经销商app")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").click()
        print("进入订单详情页面")
        time.sleep(5)
        self.d.swipe(360, 1000, 360, 100)
        print("滑动订单至底部")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/cancel_button").click()
        print("经销商待发货取消订单")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("取消订单")
        time.sleep(5)
        self.d(text=u"无此门店").click()
        print("经销商取消订单原因：无此门店")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/applybtn").click()
        print("提交")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        print("确认")
        time.sleep(5)
        if self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").exists:
            print("经销商待发货列表取消订单失败")
        else:
            print("经销商待发货列表取消订单成功")
        time.sleep(5)
        self.d.press("back")
        dealer.dealerOfflogin()

    def closeorders(self,salername,salerpwd):
        print("经销商待发货列表取消订单")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("点击全部品牌")
        time.sleep(5)
        if self.d(text=u"百事").exists:
            self.d(text=u"百事").click()
            time.sleep(5)
        else:
            while self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").exists:
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
                time.sleep(5)
                if self.d(text=u"百事").exists:
                    self.d(text=u"百事").click()
                    time.sleep(5)
                    break
                else:
                    continue
        print("选择品牌:百事，进入默认经销商仓库")
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").clear_text()
        # time.sleep(10)
        # self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_count").set_text("1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/prod_cart").click()
        time.sleep(5)
        print("加入购物车")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        time.sleep(5)
        print("购买数量：1")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        print("确定")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("选完了")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.d.press("back")
            time.sleep(5)
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        time.sleep(5)
        print("去结算")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button", text=u"确认订单").click()
        time.sleep(5)
        print("确认订单")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
            time.sleep(5)
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        time.sleep(5)
        print("完成订单")
        self.salerBack()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        time.sleep(5)
        ordersum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dot").get_text()
        print("门店待确认订单笔数：" + ordersum)
        time.sleep(5)
        dealer = appdealerInformation("QDY7N17405002857")
        dealer.dealerstart_app()
        print("启动经销商app")
        time.sleep(5)
        dealer.dealerlogin("14161915041", "915041new")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/component_maintab_tab_textview",
               text=u"订单管理").click()
        time.sleep(5)
        dealerordersum = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/num_new_count").get_text()
        print("经销商待确认订单笔数：" + dealerordersum)
        if ordersum == dealerordersum:
            print("门店待确认订单笔数==经销商待确认订单笔数")
        else:
            print("门店待确认订单笔数!=经销商待确认订单笔数")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item").click()
        print("进入经销商待确认页面")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        print("确认订单")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/cb_reason").click()
        print("选择送货司机")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/rightbtn").click()
        print("确认")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item", className="android.widget.ImageView",
               instance=1).click()
        print("进入待发货页面")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        print("点击送货完成")
        time.sleep(5)
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
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/pay_check", className="android.widget.ImageView",
               instance=2).click()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        time.sleep(5)
        self.d.app_start(package_namesaler)
        print("登录门店app")
        waitnum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dot").get_text()
        print("待收货"+waitnum)
        time.sleep(5)
        dealer.dealerstart_app()
        print("启动经销商app")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/retail_order_count_v").click()
        print("进入订单详情页")
        time.sleep(5)
        self.d.swipe(360, 1000, 360, 100)
        print("滑动订单至底部")
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/close_button").click()
        print("关闭订单")
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        time.sleep(5)
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/bg_item", className="android.widget.ImageView", instance=2).click()
        print("进入已完成列表")
        time.sleep(5)
        closemsg = self.d(resourceId="winretaildealer.net.winchannel.wincrm:id/tv_time").get_text()
        print("经销商订单关闭信息："+closemsg)
        time.sleep(5)
        self.d.press("back")
        dealer.dealerOfflogin()
        self.d.app_start(package_namesaler)
        print("启动门店app")
        time.sleep(5)
        self.d(text=u"全部订单").click()
        print("进入全部订单列表")
        time.sleep(5)
        closemsg1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/orderTimeTV").get_text()
        print("门店订单关闭信息：" + closemsg1)
        print("订单关闭成功")
        self.salerBack()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")


    def checkCoupon(self,salername,salerpwd):
        print("检查我的优惠券页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        couponnum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/wtv_coupon_num").get_text()
        print("我的优惠券数量：" + couponnum)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ll_coupon").click()
        print("点击进入我的优惠券页面")
        time.sleep(5)
        viableCouponNum = self.d(className="android.view.View", instance=1).get_text()
        print("可使用优惠券数量：" + viableCouponNum)
        alreadyUsedCouponNum = self.d(className="android.view.View", instance=2).get_text()
        print("已使用优惠券数量：" + alreadyUsedCouponNum)
        expiredCouponNum = self.d(className="android.view.View", instance=3).get_text()
        print("已过期优惠券数量：" + expiredCouponNum)
        if couponnum == viableCouponNum[4]:
            print("我的页面优惠券显示数量==我的优惠券页面可使用数量")
        else:
            print("优惠券数量显示异常")
        if int(viableCouponNum[4]) > 0:
            couponType = self.d(className="android.view.View", instance=8).get_text()
            couponMoney = self.d(className="android.view.View", instance=12).get_text()
            couponStartDate = self.d(className="android.view.View", instance=24).get_text()
            couponEndDate = self.d(className="android.view.View", instance=25).get_text()
            coupontag = self.d(className="android.view.View", instance=26).get_text()
            print("打印可使用优惠券列表优惠券详情：")
            print("优惠券类型：" + couponType)
            print("优惠券金额：" + couponMoney)
            print("优惠券开始时间：" + couponStartDate)
            print("优惠券结束时间：" + couponEndDate)
            print("优惠券状态：" + coupontag)
            starttime = couponStartDate[0:4] + couponStartDate[5:7] + couponStartDate[8:10]
            endtime = couponEndDate[0:4] + couponEndDate[5:7] + couponEndDate[8:10]
            nowTime = (datetime.datetime.now()).strftime('%Y%m%d')
            print("当前日期：" + nowTime)
            if nowTime > starttime and nowTime < endtime:
                print("优惠券在可使用期限内")
            else:
                print("优惠券不在可使用期限内，数据显示异常")
                pass
        else:
            print("当前没有可使用的优惠券")
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkHuimoney(self,salername,salerpwd):
        print("检查惠币页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        huimoneyout = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/wtv_huimoney_num").get_text()
        print("我的页面惠币显示为"+huimoneyout)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ll_huimoney").click()
        print("点击进入惠币页面")
        time.sleep(5)
        huimoneyin = self.d(className="android.view.View", instance=4).get_text()
        print("惠币详情页惠币显示为"+huimoneyin)
        if huimoneyout == huimoneyin:
            print("我的页面，惠币详情页，惠币数值显示一致")
        else:
            print("我的页面，惠币详情页，惠币数值显示不一致")
            pass
        time.sleep(5)
        huimi = self.d(className="android.view.View", instance=7).get_text()
        print("惠币详情页惠米显示为"+huimi)
        time.sleep(5)
        self.d(text=u"积分商城").click()
        print("点击进入积分商城页面")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").exists:
            print("进入积分商城页面成功")
        else:
            print("进入积分商城页面失败")
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回惠币页面")
        time.sleep(5)
        self.d(text=u"兑换记录").click()
        print("点击进入兑换记录页面")
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").exists:
            print("进入兑换记录页面成功")
        else:
            print("进入兑换记录页面失败")
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回惠币页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkPrize(self,salername,salerpwd):
        print("检查我的中奖页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        prizenum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/wtv_win_num").get_text()
        print("我的中奖数量："+prizenum)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ll_win").click()
        print("点击进入我的中奖页面")
        time.sleep(5)
        psum1 = self.d(className="android.view.View", instance=1).get_text()
        print("我的奖品详情页-可使用数量："+psum1[4])
        time.sleep(5)
        psum2 = self.d(className="android.view.View", instance=2).get_text()
        print("我的奖品详情页-已过期数量：" + psum2[4])
        time.sleep(5)
        if prizenum == psum1[4]:
            print("我的页面，奖品详情页可使用奖品数量显示一致")
        else:
            print("我的页面，奖品详情页可使用奖品数量显示不一致")
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkPay(self,salername,salerpwd):
        print("检查我的预付页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        paynum = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/wtv_pay_num").get_text()
        print("我的预付数量：" + paynum)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/ll_pay").click()
        print("点击进入我的预付页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click_exists(0)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click_exists(0)
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkShop(self,salername,salerpwd):
        print("检查积分商城页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        print("点击进入积分商城页面")
        time.sleep(5)
        if self.d(text=u"loading").exists:
            print("暂未开通活动")
        else:
            pass
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        print("点击进入兑换记录页面")
        time.sleep(5)
        if self.d(text=u"您暂时没有兑换记录").exists:
            print("您暂时没有兑换记录")
        else:
            pass
        self.d(text=u"联系客服").click()
        print("点击联系客服,拨打电话")
        time.sleep(5)
        self.d.press("back")
        print("返回兑换记录页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回积分商城")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkBrand(self,salername,salerpwd):
        print("检查品牌信息页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=2).click()
        print("点击进入品牌信息页面")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").exists:
            print("品牌信息页面加载成功")
        else:
            pass
        time.sleep(5)
        self.d(text=u"B", className="android.view.View", instance=1).click()
        print("点击右侧楼层B")
        time.sleep(5)
        if self.d(text=u"百事").exists:
            print("品牌百事展示正常")
        else:
            pass
        self.d(text=u"百事").click()
        print("点击品牌百事")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").exists:
            print("品牌详情页面加载成功")
        else:
            pass
        time.sleep(5)
        brandtext = self.d(className="android.view.View", instance=4).get_text()
        print("打印品牌介绍："+brandtext)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回品牌信息页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkSchool(self,salername,salerpwd,weburl, username, password):
        import os
        from selenium.webdriver.support.ui import Select
        print("后台品牌学院上传文章")
        webupload = wangyeInfomation()
        webupload.wangyeLogin(weburl, username, password)
        print("登录后台")
        time.sleep(5)
        webupload.wangyeclickId("menuGroup_pinpaixueyuanmananer")
        print("点击品牌学院")
        time.sleep(5)
        webupload.wangyeclickId("a_menuId_articlemanaer")
        print("点击文章管理")
        time.sleep(5)
        webupload.wangeyqiehuaniframe("main1")
        webupload.browser.find_element_by_xpath("//*[@id='status']/form/div/div[1]/div/a[1]").click()
        print("点击新增")
        time.sleep(5)
        webupload.browser.find_element_by_id("formTitle").clear()
        webupload.browser.find_element_by_id("formTitle").send_keys("AutoTest")
        print("文件名称:AutoTest")
        time.sleep(5)
        Select1 = webupload.browser.find_element_by_name("articleType")
        Select(Select1).select_by_index(9)
        print("文件类型:生意经")
        time.sleep(5)
        print("文章来源:后台发布")
        webupload.browser.find_element_by_id("formUserName").clear()
        webupload.browser.find_element_by_id("formUserName").send_keys("AutoTestUser")
        print("发布人:AutoTestUser")
        time.sleep(5)
        webupload.browser.find_element_by_id("cont").clear()
        webupload.browser.find_element_by_id("cont").send_keys("hello world")
        print("内容:hello world")
        time.sleep(5)
        webupload.wangyeclickId("addImg")
        print("点击增加")
        time.sleep(5)
        webupload.browser.find_element_by_xpath("//input[@value='文件上传']").click()
        print("点击文件上传")
        time.sleep(5)
        webupload.browser.switch_to.frame("uploadIframe")
        webupload.browser.switch_to.frame("page_interface_frame")
        time.sleep(5)
        webupload.browser.find_element_by_xpath("//input[@id='mainfile']").click()
        print("点击上传主文件")
        time.sleep(5)
        uploadFile = r"D:\upload.exe"
        os.system(uploadFile)
        print("调用自己编译的exe上传文件控件")
        time.sleep(5)
        webupload.browser.find_element_by_xpath("//input[@id='thumbnail']").click()
        print("点击上传缩略图")
        time.sleep(5)
        uploadFile = r"D:\upload.exe"
        os.system(uploadFile)
        print("调用自己编译的exe上传文件控件")
        time.sleep(5)
        webupload.browser.find_element_by_xpath("//*[@id='status']/div/div[1]/div/a").click()
        print("点击确定")
        time.sleep(5)
        webupload.browser.switch_to.alert.accept()
        print("alert确定")
        time.sleep(5)
        webupload.browser.switch_to.default_content()
        webupload.wangeyqiehuaniframe("main1")
        # time.sleep(5)
        # iconUrl = webupload.browser.find_element_by_id("url1").text
        # time.sleep(5)
        #头像链接写死
        webupload.browser.find_element_by_id("formIconURL").clear()
        webupload.browser.find_element_by_id("formIconURL").send_keys("http://cdn.winhxd.com/files/winretailsaler/180608/6eb5d60da2814bc49fb304d7b099ce48_23x23.png")
        print("发布人头像链接:"+"http://cdn.winhxd.com/files/winretailsaler/180608/6eb5d60da2814bc49fb304d7b099ce48_23x23.png")
        time.sleep(5)
        #webupload.browser.find_element_by_css_selector("a[href='javascript:save();']").click()
        webupload.browser.find_element_by_css_selector(".MenuList>a:nth-child(1)").click()
        print("保存")
        time.sleep(5)
        #webupload.wangyeQuit()
        print("退出后台")
        time.sleep(5)
        print("检查品牌学院页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=3).click()
        print("点击进入品牌学院页面")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/title").exists:
            print("品牌学院页面加载成功")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_brand_name").click()
        print("点击生意经")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/hgs_img").click()
        print("点击生活小常识")
        time.sleep(5)
        msgnum1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_comment_desc").get_text()
        print("评论前的评论总数"+msgnum1)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_comment_desc").click()
        print("点击评论")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt").clear_text()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edt").set_text("hello world")
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/report").click()
        print("提交评论完成，评论内容：hello world")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回生活小常识页面")
        time.sleep(5)
        msgnum2 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_comment_desc").get_text()
        print("评论后的评论总数" + msgnum2)
        time.sleep(5)
        if msgnum1 == msgnum2:
            print("发表评论成功，总评论数量未增加")
        else:
            print("发表评论成功，总评论数量增加")
        time.sleep(5)
        goodnum1 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_collection_desc").get_text()
        print("点赞前的总赞数量"+goodnum1[2])
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_collection_desc").click()
        print("点击点赞按钮")
        time.sleep(5)
        goodnum2 = self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_collection_desc").get_text()
        print("点赞后的总赞数量"+goodnum2[2])
        time.sleep(5)
        if goodnum1[2] == goodnum2[2]:
            print("此文章已经点过赞，总赞数量未增加")
        elif int(goodnum2[2]) == int(goodnum1[2])+1:
            print("点赞成功")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/article_share_desc").click()
        print("点击分享")
        time.sleep(5)
        if self.d(text=u"微信好友").exists and self.d(text=u"微信朋友圈").exists and self.d(text=u"QQ").exists and self.d(text=u"信息").exists:
            print("分享渠道显示正常：微信好友分享，微信朋友圈分享,QQ分享,信息分享")
        else:
            print("分享渠道显示异常")
            pass
        time.sleep(5)
        self.d(text=u"取消").click()
        print("点击取消分享")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回生意经页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回品牌学院页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")

    def checkFeedback(self,salername,salerpwd):
        print("检查意见反馈页面")
        self.d.app_start(package_namesaler)
        print("登录门店app")
        time.sleep(5)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").exists:
            time.sleep(5)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_username").set_text(salername)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/et_pwd").set_text(salerpwd)
            self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_login").click()
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="android:id/action_bar_title").exists:
            self.backCommonMethod()
            print("忽略权限设置")
        else:
            pass
        time.sleep(10)
        if self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").exists:
            self.backCommonMethod()
            print("忽略完善信息")
        else:
            pass
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        print("点击进入我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=4).click()
        print("点击进入意见反馈页面")
        time.sleep(5)
        self.d(text=u"A）APP使用意见与反馈").click()
        print("反馈类型:APP使用意见与反馈")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit").clear_text()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit").set_text("hello world")
        time.sleep(5)
        self.d.press("back")
        print("反馈内容:hello world")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit", text=u"3.联系电话").click()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit", text=u"3.联系电话").clear_text()
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/edit", text=u"3.联系电话").set_text("13393345531")
        time.sleep(5)
        self.d.press("back")
        print("联系电话:14161915041")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/applybtn").click()
        print("提交")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        print("确定")
        print("提交成功")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        print("点击反馈记录")
        time.sleep(5)
        feedbackType = self.d(className="android.view.View", instance=5).get_text()
        feedbackDate = self.d(className="android.view.View", instance=6).get_text()
        feedbackMsg = self.d(className="android.view.View", instance=7).get_text()
        print("打印反馈记录："+feedbackType+" "+feedbackDate+" "+feedbackMsg)
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回意见反馈页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        print("返回我的页面")
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=7).click()
        time.sleep(5)
        self.d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_right_btn").click()
        print("门店app退出登录")
        self.d.press("home")

if __name__ == '__main__':
    #bb = appsalerInformation("172.18.201.202:7912")
    bb = appsalerInformation("009b4aa1")
    #注册

    #bb.register("14161915047","注册五分钟，编程两小时","自动化注册","北京东升软件园","14561915041","00000000-3460-c818-0000-000035cca63e","DuvIFg5Zpp3DWK5hLisE7EbbA055RROMbAFEmtrB+uYvTBteCcv4hAuw1r/ZfrhrgjXYpA+7/MWqBnj1aZL2j13Q","efbeb424-037e-4fb9-884b-b5103b3eb641","http://retail.winhxd.com:8203/", "fanhanqingsaler", "28158116")
    #门店待确认列表取消订单
    #bb.cancelorders("14161915041","915041new")
    #经销商待确认列表取消订单
    #bb.dealercancelorders("14161915041","915041new")
    #经销商修改订单数量，单价；对比门店app，经销商app修改后的订单数据；待发货列表取消订单
    #bb.overrideorders("14161915041","915041new")
    #经销商待发货列表关闭订单
    #bb.closeorders("14161915041","915041new")
    #门店检查页面-优惠券
    #bb.checkCoupon("14161915041","915041new")
    #门店检查页面-惠币
    #bb.checkHuimoney("14161915041","915041new")
    #检查我的中奖页面
    #bb.checkPrize("14161915041","915041new")
    #检查我的预付页面
    #bb.checkPay("14161915041","915041new")
    #检查积分商城页面
    #bb.checkShop("14161915041","915041new")
    #检查品牌信息页面
    #bb.checkBrand("14161915041","915041new")
    #检查品牌学院页面
    #bb.checkSchool("14161915041","915041new","http://retail.winhxd.com:8203/", "fanhanqingsaler", "28158116")
    #检查意见反馈页面
    bb.checkFeedback("13393345531","345531")





