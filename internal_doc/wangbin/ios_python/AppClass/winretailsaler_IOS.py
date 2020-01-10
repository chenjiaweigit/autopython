#-*- coding: UTF-8 -*-
from decimal import Decimal
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Commonvariable

import atx
import time
import Commonvariable
package_namesaler = 'com.winchannel.winretailsaler'

class appsalerInformation_IOS:
    def __init__(self,ip):
        self.d = atx.connect(ip)

    def assert_saler(self,m):
        assert m.exists
        pass
#封装click（）+set_text方法
    def salerClick_ios(self,iosID):
        self.d(label=iosID).click()
        pass

    def salerSet_text_ios(self,iosID,iosSet_text):
        self.d(label=iosID).set_text(iosSet_text)
        pass

    def salerbackone_ios(self):
        self.d.click_image(Commonvariable.All_PHOTO_LIST+"fanhui.1334x750.png")
        pass

    def salerBack_ios(self):
        while True:
            if self.d(label=u"优惠下单").exists:
                break
            else:
                self.d(type="Button").click()
                continue


#启动登陆门店app
    def saler_startapp_ios(self,loginphone,loginpwd):
        self.d.start_app(package_namesaler)
        # if "惠下单" in d.session.alert.text:
        #     d.session.alert.accept()
        # else:
        #     pass
        if self.d(label=u"登录").exists:
            self.d(label=u"登录").click()
            self.d(className="TextField").set_text(loginphone)
            self.d(className="SecureTextField").set_text(loginpwd)
            self.d(label=u"登录", name=u"登录", type="Button").click()
        else:
            pass
        if self.d(label=u"联系客服").exists:
            print "该手机登陆账号太多，请更换手机"
            self.d(label=u"取消").click()
        else:
            pass
        # if "惠下单" in self.d.session.alert.text:
        #     self.d.session.alert.accept()
        # else:
        #     pass
        if self.d(label=u"10 跳过").exists:
            time.sleep(10)
            print("10")
        elif self.d(label=u"9 跳过").exists:
            time.sleep(9)
            print("9")
        elif self.d(label=u"8 跳过").exists:
            time.sleep(8)
            print("8")
        elif self.d(label=u"7 跳过").exists:
            time.sleep(7)
            print("7")
        elif self.d(label=u"6 跳过").exists:
            time.sleep(6)
            print("6")
        elif self.d(label=u"5 跳过").exists:
            time.sleep(5)
            print("5")
        elif self.d(label=u"4 跳过").exists:
            time.sleep(4)
            print("4")
        elif self.d(label=u"3 跳过").exists:
            time.sleep(3)
            print("3")
        elif self.d(label=u"2 跳过").exists:
            time.sleep(2)
            print("2")
        elif self.d(label=u"1 跳过").exists:
            time.sleep(1)
            print("1")
        else:
            pass
        time.sleep(5)
        if self.d(label=u"去完善").exists:
            self.d(label=u"去完善").click()
            print "完善个人信息功能未完成"
        else:
            print "个人信息齐全，不需要完善"
            pass


        self.salerUpdate()
        self.d(label=u"优惠下单").click()
        assert self.d(label=u"优惠下单").exists
        # return phonebrand
        pass

#退出登陆
    def salerOffLogin(self,loginphone,loginpwd):
        self.saler_startapp_ios(loginphone, loginpwd)
        if self.d(label=u"我的").exists:
            self.d(label=u"我的").click()
            self.salertupian(Commonvariable.All_PHOTO_LIST+"saler_set.1334x750.png")
            self.salertupian(Commonvariable.All_PHOTO_LIST+"saler_offlogin.1334x750.png")
            self.d(label=u"确定").click()
        else:
            pass


#门店首页管理
    def salerHomepage_ios(self,sousuo):
        self.d(label=u"优惠下单").click()
        assert u"米面粮油" in self.d(label=u"米面粮油").text
        self.d(className="SearchField").click()
        self.d(className="StaticText").set_text(sousuo)
        self.d(label=u"Search").click()
        assert self.d(label=u"商品").exists
        assert self.d(label=u"品牌").exists
        assert self.d(label=u"经销商").exists
        self.salerbackone_ios()
        self.salerbackone_ios()
        # time.sleep(2)
        # for i in range(1,6):
        #     self.d.swipe(800,1500,800,500)
        # time.sleep(3)
        # self.d(className="Button").click()
        time.sleep(3)
        # self.d.click(0.37, 0.351)
        self.d.click_image(Commonvariable.All_PHOTO_LIST+"1.1334x750.png")
        self.d.click_image(Commonvariable.All_PHOTO_LIST+"2.1334x750.png")
        time.sleep(2)
        assert self.d(label=u"去结算").exists
        pass

#门店仓库
    def salerWarehouse_ios(self,num,sousuo):
        # self.d(label=u"custSerIcon@2x", name=u"custSerIcon@2x", type="Button").click()
        # time.sleep(2)
        # assert self.d(label=u"拨打电话", name=u"拨打电话", type="Button").exists
        # self.salerbackone_ios()
        # self.d(label=u"telIcon@2x", name=u"telIcon@2x", type="Button").click()
        #
        # self.salertupian(Commonvariable.All_PHOTO_LIST+"saler_cannelbutton.1334x750.png")
        self.d(label=u"num big add new@2x", name=u"num big add new@2x", type="Button").click()
        self.d(label=u"num big add new@2x", name=u"num big add new@2x", type="Button").click()
        self.d(label=u"num big minus new@2x", name=u"num big minus new@2x", type="Button").click()
        assert "1"==self.d(type="TextField", index=1).text
        self.d(type="Image", index=2).click()
        time.sleep(2)
        assert self.d(label=u"代理品牌", name=u"代理品牌", type="StaticText").exists
        self.salerbackone_ios()
        time.sleep(3)
        if self.d(className="StaticText",index=3).exists:
            self.d(className="StaticText",index=3).click()
            time.sleep(4)
            self.d(label=u"wc goods chatBtn", name=u"wc goods chatBtn", type="Button").click()
            print(4)
        else:
            print("dddd")
            pass
        self.d(type="Button", index=2).click()
        self.d(type="TextField", index=1).set_text(sousuo)
        self.d(label=u"Search").click()
        self.salerbackone_ios()
        pass


#立即升级提示取消
    def salerUpdate(self):
        if self.d(label=u"立即升级").exists:
            self.d(label=u"coupon button cancel@2x").click()
        else:
            pass




# 购物车
    def salerShoppingCart_ios(self,loginname,loginpwd,num_ck):
        self.saler_startapp_ios(loginname,loginpwd)
        self.salertupian(Commonvariable.All_PHOTO_LIST+"1.1334x750.png")
        time.sleep(2)
        self.salertupian(Commonvariable.All_PHOTO_LIST+"2.1334x750.png")
        self.d(type="TextField", index=1).set_text(num_ck)
        self.d(label=u"完成", name=u"完成", type="Button").click()
        self.d(label=u"num big add new@2x", name=u"num big add new@2x", type="Button", index=2).click()
        time.sleep(2)
        self.salerUpdate()

        if "¥" in self.d(className="StaticText", index=29).text:
            good1 = self.salerStrtoDou(self.d(className="StaticText", index=29))
            good2 = self.salerStrtoDou(self.d(className="StaticText", index=34))
            print(1)

        else:
            good1 = self.salerStrtoDou(self.d(className="StaticText", index=29))
            good2 = self.salerStrtoDou(self.d(className="StaticText", index=34))
            print(2)
        print(good1,good2)

        sumPrice_ck = good1 * int(num_ck)+good2

        print(sumPrice_ck)
        self.d(label=u"去结算", name=u"去结算", type="Button").click()
        time.sleep(3)
        sum_gwc = self.d(className="StaticText",index=2).text
        print(sum_gwc)
        sumPrice_gwc1 = float(sum_gwc.strip(u'合计: ¥'))
        print(sumPrice_ck,sumPrice_gwc1)
        assert str(sumPrice_ck) in str(sumPrice_gwc1)
        #购物车
        self.d(label=u"carSelect yes@2x", name=u"carSelect yes@2x", type="Button",index=3).click()
        self.d(label=u"d8c3b16f5ba24a1dadb72e453b6fef", name=u"d8c3b16f5ba24a1dadb72e453b6fef", type="Button").click()
        self.d(label=u"确定", name=u"确定", type="Button").click()
        self.d(label=u"num big add new@2x", name=u"num big add new@2x", type="Button").click()
        print self.d(className="StaticText", index=2).text
        sumPrice_gwc2 = Decimal(float((self.d(className="StaticText", index=2).text).strip(u'合计: ¥'))).quantize(Decimal('0.00'))

        print self.d(className="StaticText", index=5).text
        Price2 = self.salerStrtoDou(self.d(className="StaticText", index=5))
        print self.d(type="TextField", index=1).text
        num2 = self.salerStrtoDou(self.d(type="TextField", index=1))
        sum_gwc2js = num2*Price2
        assert sum_gwc2js == sumPrice_gwc2
        self.d(label=u"去结算", name=u"去结算", type="Button").click()
        return sumPrice_ck,sumPrice_gwc1,sum_gwc2js,sumPrice_gwc2

    #预订单
    def salerAgoorder_IOS(self,gwcprice):
        print("预订单======")
        print self.d(className="StaticText", index=2).text#合计
        agoorderprice1 =self.salerStrtoDou2(self.d(className="StaticText", index=2).text,"合计: ¥")
        print(agoorderprice1)
        print self.d(className="StaticText", index=15).text# 总金额
        agoorderprice2 = self.salerStrtoDou2(self.d(className="StaticText", index=15).text,"¥")
        print agoorderprice2
        assert agoorderprice1 == agoorderprice2
        assert gwcprice == agoorderprice1
        self.d(label=u"确认订单", name=u"确认订单", type="Button").click()
        #不选择优惠券
        if self.d(label=u"是", name=u"是", type="Button").exists:
            self.d(label=u"是", name=u"是", type="Button").click()
        else:
            pass
        self.d(label=u"抢优惠", name=u"抢优惠", type="Button").click()
        time.sleep(3)
        self.salerbackone_ios()
        self.d(label=u"查看订单", name=u"查看订单", type="Button").click()
        self.salerbackone_ios()
        self.d(label=u"完成", name=u"完成", type="Button").click()
        assert self.d(label=u"telIcon@2x", name=u"telIcon@2x", type="Button").exists
        pass

#地址管理
    def salerAddrmanage(self,addrName,addrPhone,addrinfo,addrcode):
        self.d(label=u"我的", name=u"我的", type="Button").click()
        # self.d(type="Button").click()
        self.d(label=u"arrow white@2x", name=u"arrow white@2x", type="Button").click()
        self.d(label=u"地址管理").click()
        self.d(label=u"+ 新建地址", name=u"+ 新建地址", type="StaticText").click()
        self.d(type="TextField", index=4).set_text(addrcode)
        self.d(type="TextField", index=1).set_text(addrName)
        self.d(type="TextField", index=2).set_text(addrPhone)
        # self.d(type="TextField", index=3).set_text("")
        self.d(label=u"请填写详细地址", name=u"请填写详细地址", type="StaticText").set_text(addrinfo)
        # self.d(label=u"完成", name=u"完成", type="Button").click()
        self.d(label=u"更多信息", name=u"更多信息", type="Button").click()
        time.sleep(5)
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        # print("5")
        self.d(label=u"北京市").click()
        self.d(label=u"北京市").click()
        self.d(label=u"海淀区").click()
        self.d(label=u"东升地区办事处").click()
        self.d(label=u"前屯社区居委会").click()
        time.sleep(2)
        print self.d( type="StaticText",index=7).text
        assert self.d( type="StaticText",index=7).text is not ""
        self.d(label=u"保存", name=u"保存", type="Button").click()
        #左划右划
        self.d.swipe(400, 200, 100, 200, 1.0)
        self.d.click_image("/Users/wangbin/Desktop/4.1334x750.png")
        pass

    #门店信息
    def salerMyinfo(self,info_name,info_storename,info_addr):
        self.d(label=u"我的", name=u"我的", type="Button").click()
        self.d(label=u"arrow white@2x", name=u"arrow white@2x", type="Button").click()
        self.d(label=u"更多信息").click()
        self.d(label=u"姓名", name=u"姓名", type="StaticText").click()
        self.d.click_image("/Users/wangbin/Desktop/6.1334x750.png")
        self.d(type="TextView").clear_text()
        self.d(type="TextView").set_text(info_name)
        self.d(label=u"保存", name=u"保存", type="Button").click()
        self.d(label=u"手机号", name=u"手机号", type="StaticText").click()
        assert self.d(label=u"400-687-0066", name=u"400-687-0066", type="Button").exists
        self.salerbackone_ios()
        self.d(label=u"门店名称", name=u"门店名称", type="StaticText").click()
        self.d.click_image("/Users/wangbin/Desktop/6.1334x750.png")
        self.d(type="TextView").clear_text()
        self.d(type="TextView").set_text(info_storename)
        self.d(label=u"保存", name=u"保存", type="Button").click()
        self.d(label=u"所在地区", name=u"所在地区", type="StaticText").click()
        assert self.d(label=u"400-687-0066", name=u"400-687-0066", type="Button").exists
        self.salerbackone_ios()
        self.d(label=u"详细地址", name=u"详细地址", type="StaticText").click()
        self.d.click_image("/Users/wangbin/Desktop/6.1334x750.png")
        self.d(type="TextView").clear_text()
        self.d(type="TextView").set_text(info_addr)
        self.d(label=u"保存", name=u"保存", type="Button").click()
        self.d(label=u"上传门店照片", name=u"上传门店照片", type="StaticText").click()
        # self.d(type="Image",index=2).click()
        # self.d.click_image("/Users/wangbin/Desktop/5.1334x750.png")
        self.d(type="Image").click()
        time.sleep(2)
        self.d(label=u"相机选取器").click()
        time.sleep(2)
        self.d(label=u"拍照").click()
        time.sleep(2)
        self.d(label=u"使用照片").click()
        time.sleep(3)
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break


#修改密码
    def salerModifypwd(self,oldpwd,newpwdOne,newpwdTwo,loginphone):
        self.d(label=u"我的", name=u"我的", type="Button").click()
        self.salertupian(Commonvariable.All_PHOTO_LIST+"7.1334x750.png")
        self.salertupian(Commonvariable.All_PHOTO_LIST + "modifypwd.1334x750.png")
        self.d(type="SecureTextField", index=1).set_text(oldpwd)
        self.d(type="SecureTextField", index=2).set_text(newpwdOne)
        self.d(type="SecureTextField", index=3).set_text(newpwdTwo)
        self.d(label=u"修改密码", name=u"修改密码", type="Button").click()
        self.d(label=u"确定", name=u"确定", type="Button").click()
        time.sleep(3)
        assert self.d(label=u"登录", name=u"登录", type="Button").exists
        self.saler_startapp_ios(loginphone,newpwdTwo)
        pass

#注册
    def salerRegister_IOS(self,type,reg_phone,reg_name,jh_phone,phoneup):
        from excelManage_ios import salerSql_IOS
        if type == "普通注册":
            print(type)
            self.d.start_app(package_namesaler)
            assert self.d(label=u"免费注册", name=u"免费注册", type="Button").exists
            self.d(label=u"免费注册", name=u"免费注册", type="Button").click()
            while True:
                if self.d(type="StaticText", index=4).text is not "":
                    break
                else:
                    time.sleep(2)
                    continue
            self.d(label=u"下一步", name=u"下一步", type="Button").click()
            self.d(type="TextField", index=1).set_text(reg_phone)
            self.d(label=u"获取验证码", name=u"获取验证码", type="Button").click()
            code = salerSql_IOS.salersql_register_ios(reg_phone)
            self.d(type="TextField", index=2).set_text(code)
            self.d(type="SecureTextField", index=1).set_text("aa248163")
            self.d(type="SecureTextField", index=2).set_text("aa248163")
            self.d(label=u"完成").click()
            self.d(label=u"下一步").click()
            time.sleep(5)
            self.d(type="TextField", index=1).set_text("自动化门店名称")
            self.d(type="TextField", index=2).set_text(reg_name)
            time.sleep(2)
            self.d(type="TextField", index=3).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).set_text("25")
            self.d(label=u"完成").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(label=u"请选择所在地区").click()
            time.sleep(5)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"北下关街道办事处").click()
            self.d(label=u"广通苑社区居委会").click()
            time.sleep(2)
            self.d(label=u"街道，楼牌号等").set_text("自动化门店名称ios街道")
            self.d(type="TextField", index=1).set_text("门牌号")
            self.d(type="TextField", index=2).set_text("标准建筑")
            time.sleep(2)
            self.d(label=u"完成").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(label=u"addpicture@2x").click()
            while True:
                if self.d(label=u"确定").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(label=u"addpicture@2x").click()
                    continue
            self.d(label=u"确定").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=2).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=2).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=3).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=3).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=4).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=4).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=2).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=3).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).click()
            self.d(label=u"确定").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=2).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=3).click()
            self.d(label=u"饮料乳品").click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=5).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=6).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=7).click()
            self.d(label=u"确定").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).set_text("14778785560")
            self.d(label=u"完成").click()
            self.d(label=u"完成").click()
            while True:
                if self.d(label=u"优惠下单").exists:
                    break
                else:
                    self.d(label=u"完成").click()
                    time.sleep(2)
            time.sleep(5)
            loc = salerSql_IOS.salersql_finish_regInfo_ios(reg_phone)
            assert float(loc) > 0
            from excelManage_ios import excelInit_ios
            excelInit_ios.excelUpdatereg(phoneup)

        elif type == "邀请注册":
            self.d(type="TextField", index=1).set_text("自动化门店名称")
            self.d(type="TextField", index=2).set_text(reg_name)
            time.sleep(2)
            self.d(type="TextField", index=3).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).set_text("25")
            self.d(label=u"完成").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(label=u"请选择所在地区").click()
            time.sleep(5)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"北下关街道办事处").click()
            self.d(label=u"广通苑社区居委会").click()
            time.sleep(2)
            self.d(label=u"请输入详细地址").set_text("自动化门店名称ios街道")
            self.d(type="TextField", index=1).set_text("门牌号")
            self.d(type="TextField", index=2).set_text("标准建筑")
            time.sleep(2)
            self.d(label=u"完成").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(label=u"addpicture@2x").click()
            while True:
                if self.d(label=u"确定").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(label=u"addpicture@2x").click()
                    continue
            self.d(label=u"确定").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=2).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=2).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=3).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=3).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"addpicture@2x", name=u"addpicture@2x", type="Button", index=4).click()
            while True:
                if self.d(label=u"打开照相机").exists:
                    break
                else:
                    time.sleep(2)
                    self.d(type="Image", index=4).click()
                    continue
            self.d(label=u"打开照相机").click()
            time.sleep(2)
            self.d(label=u"相机选取器").click()
            time.sleep(2)
            self.d(label=u"拍照").click()
            time.sleep(2)
            self.d(label=u"使用照片").click()
            time.sleep(3)
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=2).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=3).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).click()
            self.d(label=u"确定").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=2).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=3).click()
            self.d(label=u"饮料乳品").click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=4).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=5).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=6).click()
            self.d(label=u"确定").click()
            self.d(type="TextField", index=7).click()
            self.d(label=u"确定").click()
            self.d(label=u"下一步").click()
            time.sleep(2)
            self.d(type="TextField", index=1).set_text("14778785560")
            self.d(label=u"完成").click()
            self.d(label=u"完成").click()
            while True:
                if self.d(label=u"优惠下单").exists:
                    break
                else:
                    self.d(label=u"完成").click()
                    time.sleep(2)
            time.sleep(5)
            loc = salerSql_IOS.salersql_finish_regInfo_ios(reg_phone)
            assert float(loc) > 0
            from excelManage_ios import excelInit_ios
            excelInit_ios.excelUpdatereg(phoneup)

        elif type == "业代激活":
            self.d.start_app(package_namesaler)
            if self.d(label=u"业代激活").exists:
                self.d(label=u"业代激活").click()
                self.d(type="TextField", index=1).set_text(jh_phone)
                self.d(label=u"获取验证码").click()
                jh_code = salerSql_IOS.salersql_register_ios(jh_phone)
                self.d(type="TextField", index=2).set_text(jh_code)
                self.d(label=u"去激活").click()
                self.d(label=u"输入激活码").click()
                self.d(type="TextField", index=1).set_text("14778785560")
                self.d(label=u"激活").click()
                time.sleep(3)
                while True:
                    if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                        time.sleep(3)
                        continue
                    else:
                        break
                self.salertupian(Commonvariable.All_PHOTO_LIST+"saler_alive.1334x750.png")

                time.sleep(3)
                while True:
                    if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                        time.sleep(3)
                        continue
                    else:
                        break
                self.d(label=u"确定").click()
                time.sleep(3)
                while True:
                    if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                        time.sleep(3)
                        continue
                    else:
                        break
                assert self.d(label=u"优惠下单").exists
                time.sleep(5)
                # loc = salerSql_IOS.salersql_finish_regInfo_ios(jh_phone)
                # assert loc is not "0.0"
            else:
                print "请先退出门店app在进行测试"
            from excelManage_ios import excelInit_ios
            excelInit_ios.excelUpdatereg(jh_phone)

#进入仓库
    def salerEnterstorehouse_ios(self):
        self.salertupian(Commonvariable.All_PHOTO_LIST+"1.1334x750.png")
        self.salertupian(Commonvariable.All_PHOTO_LIST+"2.1334x750.png")


#add仓库添加商品到购物车
    def salerAddShopsTogwc_ios(self):
        num1 = self.salerNumrandom(1,10)
        self.d(type="TextField", index=1).set_text(str(num1))
        self.d(label=u"完成").click()
        time.sleep(3)
        num2 = self.salerNumrandom(1, 10)
        self.d(type="TextField", index=2).set_text(str(num2))
        self.d(label=u"完成").click()
        time.sleep(3)
        for i in range(1,3):
            self.d.swipe(500, 500, 500, 1500)
        print("判断并且计算总金额")
        if "¥" in self.d(className="StaticText", index=31).text:
            goodprice1 = self.salerStrtoDou(self.d(className="StaticText", index=31))
            if "¥" in self.d(className="StaticText", index=36).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=36))
            elif "¥" in self.d(className="StaticText", index=35).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=35))
            elif "¥" in self.d(className="StaticText", index=34).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=34))
        elif "¥" in self.d(className="StaticText", index=28).text:
            goodprice1 = self.salerStrtoDou(self.d(className="StaticText", index=28))
            if "¥" in self.d(className="StaticText", index=33).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=33))
            elif "¥" in self.d(className="StaticText", index=32).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=32))
            elif "¥" in self.d(className="StaticText", index=31).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=31))
        elif "¥" in self.d(className="StaticText", index=29).text:
            goodprice1 = self.salerStrtoDou(self.d(className="StaticText", index=29))
            if "¥" in self.d(className="StaticText", index=34).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=34))
            elif "¥" in self.d(className="StaticText", index=33).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=33))
            elif "¥" in self.d(className="StaticText", index=32).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=32))
        elif "¥" in self.d(className="StaticText", index=30).text:
            goodprice1 = self.salerStrtoDou(self.d(className="StaticText", index=30))
            if "¥" in self.d(className="StaticText", index=35).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=35))
            elif "¥" in self.d(className="StaticText", index=34).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=34))
            elif "¥" in self.d(className="StaticText", index=33).text:
                goodprice2 = self.salerStrtoDou(self.d(className="StaticText", index=33))

        print goodprice1, goodprice2
        sum = goodprice1*num1+goodprice2*num2
        time.sleep(2)
        self.d(label=u"去结算").click()
        return sum

#购物车to预订单
    def salerAddShopsToydd(self,sumck):
        time.sleep(3)
        print self.d(className="StaticText", index=2).text
        sumgwc = self.salerStrtoDou2(self.d(className="StaticText", index=2).text,"合计: ¥")
        print(sumgwc)

        assert sumck == sumgwc
        self.d(label=u"去结算").click()
        time.sleep(3)
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        return sumgwc

#预订单to完成订单
    def saleraddyddToorder(self,sumggwc,type):
        sumydd = self.salergwcStrtoDou(self.d(className="StaticText", index=2))
        assert sumggwc == sumydd
        time.sleep(5)
        print(self.d(className="StaticText", index=14).text)
        if self.d(className="StaticText", index=14).text in "优惠券(请点击选取)   已选0/0张 ":
            print "无优惠券"
            sumydd = self.salergwcStrtoDou(self.d(className="StaticText", index=2))
            print(sumydd)
            assert sumggwc == sumydd
            self.d(label=u"确认订单").click()
            self.d(label=u"完成").click()

            pass

        else:
            print("you 优惠券")
            import Commonvariable
            if type == Commonvariable.SALER_ISSELECT_a:#选择
                print(type)
                self.d(label=u"确认订单").click()
                if self.d(label=u"是").exists:
                    self.d(label=u"否").click()
                    if "优惠券(请点击选取)" in self.d(className="StaticText", index=14).text:
                        self.d(className="StaticText", index=14).click()
                    else:
                        self.d(className="StaticText", index=13).click()
                    time.sleep(5)
                    self.d(label=u"可选择").click()
                    time.sleep(3)
                    sumydd1 =self.saleryddStrtoDou(self.d(className="StaticText", index=3))
                    print sumydd1
                    self.d(label=u"去结算").click()
                    time.sleep(2)
                    sumydd2 = self.salergwcStrtoDou(self.d(className="StaticText", index=2))
                    print sumydd2
                    assert sumydd1 == sumydd2
                    self.d(label=u"确认订单").click()
                    self.d(label=u"完成").click()
                    sumydd = sumydd1
                    pass
            elif type == Commonvariable.SALLER_NOSELECT_b:#不选择
                print(type)
                sumydd = self.salergwcStrtoDou(self.d(className="StaticText", index=3))
                print(sumydd)
                self.d(label=u"确认订单").click()
                time.sleep(3)
                self.salertupian("/Users/wangbin/Desktop/banbentupian/yes.1334x750.png")
                assert sumydd == sumggwc
                self.d(label=u"完成").click()
        return sumydd,type




# 促销信息
    def salerPromotion_ios(self):
        if self.d(className="StaticText", index=28).text is not "":
            shopPromotion1 = self.d(className="StaticText", index=29).text  # 商品促销信息

        else:
            shopPromotion1 = self.d(className="StaticText", index=29).exists
        print(shopPromotion1)
        if self.d(className="StaticText",index=3).exists:  # 品牌促销信息
            banerProtion1 = self.d(className="StaticText",index=3).text

        else:
            banerProtion1 = self.d(className="StaticText",index=3).exists
        print(banerProtion1)
        self.d(label=u"num big add new@2x").click()
        self.d(label=u"去结算").click()
        time.sleep(3)

        if self.d(className="StaticText", index=5).exists:
            shopPromotion2 = self.d(className="StaticText", index=5).text

        else:
            shopPromotion2 = self.d(className="StaticText", index=5).exists
        print(shopPromotion2)
        self.d(label=u"去结算").click()
        time.sleep(3)
        if self.d(className="StaticText", index=15).exists:
            jxsProtion = self.d(className="StaticText", index=15).text
            print(jxsProtion)
        else:
            jxsProtion = self.d(className="StaticText", index=15).exists
        print(jxsProtion)
        return shopPromotion1, shopPromotion2, banerProtion1, jxsProtion

#惠聊
    def salerHuiliao_ios(self,name,message):
        # 客服电话
        self.d(label=u"惠聊", name=u"惠聊", type="Button").click()
        self.d(label=u"惠聊", name=u"惠聊", type="Button").click()
        assert self.d(label=u"通知").exists
        # 找客服
        # self.salertupian(Commonvariable.All_PHOTO_LIST+"zhaokufu.1334x750.png")
        # time.sleep(3)
        # self.d(label=u"取消").click()
        # 三个导航栏切换
        self.d(label=u"通知").click()
        self.d(label=u"动态").click()
        self.d(label=u"消息").click()
        # 通讯录
        self.salertupian(Commonvariable.All_PHOTO_LIST+"tongxunlu.1334x750.png")
        # 通讯录电话
        self.d(type="TextField", index=1).set_text(name)
        # self.d(label=u"wc icon contactCall").click()
        # self.d(label=u"取消").click()
        time.sleep(3)
        self.d(type="Cell").click()
        # 经销商信息
        self.salertupian(Commonvariable.All_PHOTO_LIST+"jxsinfo.1334x750.png")
        time.sleep(4)
        self.salerWebWait(self.d(label=u"代理品牌"))
        self.salerbackone_ios()
        # 发送表情，文字，语音，图片，位置
        self.d(type="TextView").set_text(message)
        self.d(label=u"Send").click()
        self.d(label=u"icon toolview emotion normal").click()
        self.d(label=u"emoji 04").click()
        self.d(label=u"ajmd s normal@2x").click()
        self.d(label=u"ajmd003@2x").click()
        self.d(label=u"icon toolview add normal").click()
        self.d(label=u"位置").click()
        while True:
            if self.d(type="StaticText", index=4).text is not "":
                break
            else:
                time.sleep(2)
                continue
        self.salertupian(Commonvariable.All_PHOTO_LIST+"saler_fasong.1334x750.png")
        self.d(label=u"icon toolview add normal").click()
        self.d(label=u"相册").click()
        if self.d(label=u"好").exists:
            self.d(label=u"好").click()
        else:
            pass
        self.d(type="Image", index=14).click()

        self.d(label=u"完成").click()
        self.d(label=u"icon toolview add normal").click()
        self.d(label=u"拍摄").click()
        if self.d(label=u"好").exists:
            self.d(label=u"好").click()
        else:
            pass
        self.d(label=u"相机选取器").click()
        time.sleep(3)
        self.d(label=u"拍照").click()
        time.sleep(3)
        self.d(label=u"使用照片").click()
        self.d(label=u"icon toolview voice normal").click()
        self.d(label=u"按住说话").tap_hold(5)
        self.salerbackone_ios()
        if self.d.exists(Commonvariable.All_PHOTO_LIST+"tankuang.1334x750.png"):
            time.sleep(6)
        self.d(label=u"关闭").click()
        time.sleep(4)
        self.d(label=u"我的").click()
        time.sleep(5)
        startNum = int(self.d(className="StaticText", index=4).text)
        time.sleep(3)
        print startNum
        return startNum

    def salerhuiliaoyouhuiquan(self):
        self.d(label=u"惠聊", name=u"惠聊", type="Button").click()
        self.d(type="Cell",index=2).click()
        assert self.d(label=u"查看优惠券").exists
        self.salertupian(Commonvariable.All_PHOTO_LIST+"scan.1334x750.png")
        self.salertupian(Commonvariable.All_PHOTO_LIST+"lijilingqu.1334x750.png")
        time.sleep(6)
        self.d(label=u"WCSendCoupon close").click()
        self.salerbackone_ios()
        self.d(label=u"我的").click()
        endNum = int(self.d(className="StaticText", index=4).text)
        print endNum
        return endNum

#门店管理
    def salerStoreManage_ios(self,a):
        self.saler_startapp_ios("14778786561","aa248163")
        self.salerEnterstorehouse_ios()
        time.sleep(5)
        print(a)
        if a in "AB店":
            print (a)
            assert self.d(label=u"num big add new@2x").exists == False
        elif a in "默认":
            print (a)
            assert self.d(label=u"num big add new@2x").exists == True
        else:
            print("其他类型")
#进入订单（进入四个订单列表）
    def salerEnter_ios(self,orderliebiao):
        if self.d(label=u"确定").exists:
            self.d(label=u"取消").click()
        else:
            pass
        self.d(label=u"我的").click()
        self.d(label=orderliebiao).click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        return orderliebiao





#获取订单信息比较订单
    def salerOrderinfo_ios(self,ordertype,ordertype2):
        if str(ordertype) =="待确认":
            assert self.d(label=u"取消订单").exists ==True
            print self.d(type="StaticText", index=2).text#页面标题
            assert "待确认" in self.d(type="StaticText", index=2).text
            print self.d(type="StaticText", index=3).text#状态
            assert self.d(type="StaticText", index=3).text == "订单待确认"
            print self.d(type="StaticText", index=4).text#下单时间
            print self.d(type="StaticText", index=5).text#商品数量和种类
            print self.d(type="StaticText", index=8).text#支付方式和金额
            print self.d(type="StaticText", index=10).text#经销商名称
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=4).text
            orderCode = self.d(type="StaticText", index=4).text
            self.salerbackone_ios()

        elif str(ordertype) =="待收货":
            assert self.d(label=u"再来一单").exists ==True
            assert self.d(label=u"确认收货").exists == True
            print self.d(type="StaticText", index=2).text#页面标题
            assert "待收货" in self.d(type="StaticText", index=2).text
            print self.d(type="StaticText", index=3).text#状态
            assert self.d(type="StaticText", index=3).text == "订单待收货"
            print self.d(type="StaticText", index=4).text#下单时间
            print self.d(type="StaticText", index=5).text#商品数量和种类
            print self.d(type="StaticText", index=8).text#支付方式和金额
            print self.d(type="StaticText", index=10).text#经销商名称
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=4).text
            orderCode = self.d(type="StaticText", index=4).text
            self.salerbackone_ios()
            import Commonvariable
            if ordertype2 == Commonvariable.SALER_ISRECEIPTGOODS:
                self.d(label=u"确认收货").click()
                self.d(label=u"确定").click()
                self.d(label=u"star no select@2x", name=u"star no select@2x", type="Button", index=4).click()
                self.d(label=u"star no select@2x", name=u"star no select@2x", type="Button", index=4).click()
                self.d(label=u"star no select@2x", name=u"star no select@2x", type="Button", index=4).click()
                self.d(label=u"完成").click()
                self.d(label=u"确定").click()
            elif ordertype2 ==Commonvariable.SALER_NOTRECEIPTGOODS:
                pass
            else:
                pass

        elif str(ordertype) == "已收货":
            assert self.d(label=u"再来一单").exists == True
            print self.d(type="StaticText", index=2).text#页面标题
            assert "已收货" in self.d(type="StaticText", index=2).text
            print self.d(type="StaticText", index=3).text#状态
            assert self.d(type="StaticText", index=3).text == "订单已收货"
            print self.d(type="StaticText", index=4).text#下单时间
            print self.d(type="StaticText", index=5).text#商品数量和种类
            print self.d(type="StaticText", index=8).text#支付方式和金额
            print self.d(type="StaticText", index=10).text#经销商名称
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=4).text
            orderCode = self.d(type="StaticText", index=4).text

        elif str(ordertype) == "全部订单":
            # assert self.d(label=u"再来一单").exists ==True
            print self.d(type="StaticText", index=2).text#页面标题
            print self.d(type="StaticText", index=3).text#状态
            print self.d(type="StaticText", index=4).text#下单时间
            print self.d(type="StaticText", index=5).text#商品数量和种类
            print self.d(type="StaticText", index=8).text#支付方式和金额
            print self.d(type="StaticText", index=10).text#经销商名称
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=4).text
            orderCode = self.d(type="StaticText", index=4).text
        return  orderCode


#门店取消订单
    '''原因，'''
    def salerCancleOrder(self,review):
        self.d(type="Cell").click()
        time.sleep(2)
        print self.d(type="StaticText", index=3).text
        orderCode_dqr = self.d(type="StaticText", index=3).text
        self.salerbackone_ios()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.d(label=u"取消订单").click()
        self.d(label=u"确定").click()
        time.sleep(3)
        self.d(type="Button", index=6).click()
        self.d(type="TextView").set_text(review)
        self.d(label=u"完成").click()
        self.salertupian(Commonvariable.All_PHOTO_LIST+"qxwc_saler.1334x750.png")
        self.d(label=u"确定").click()
        self.salerbackone_ios()
        self.d(label=u"全部订单").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        time.sleep(3)
        self.d(type="Cell").click()
        time.sleep(2)
        print self.d(type="StaticText", index=3).text
        orderCode_qbdd = self.d(type="StaticText", index=3).text
        self.salerbackone_ios()
        time.sleep(3)
        print self.d(type="StaticText", index=5).text  # 状态
        print self.d(type="StaticText", index=4).text  # 下单时间
        assert "订单已取消" in self.d(type="StaticText", index=5).text
        assert "取消时间" in self.d(type="StaticText", index=4).text
        assert orderCode_dqr == orderCode_qbdd

#再来一单-jxs 取消订单
    def salerOrderAgain(self):
        self.d(label=u"再来一单").click()
        self.d(label=u"去结算").click()
        self.d(label=u"确认订单").click()
        if self.d(label=u"是").exists:
            self.d(label=u"是").click()
        self.d(label=u"完成").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.salerbackone_ios()
        time.sleep(3)
        self.d(label=u"全部订单").click()
        time.sleep(2)
        print self.d(type="StaticText", index=3).text  # 状态
        assert self.d(type="StaticText", index=3).text == "订单待确认"
        print self.d(type="StaticText", index=4).text  # 下单时间
        print self.d(type="StaticText", index=5).text  # 商品数量和种类
        print self.d(type="StaticText", index=8).text  # 支付方式和金额
        print self.d(type="StaticText", index=10).text  # 经销商名称
        self.d(type="Cell").click()
        time.sleep(2)
        print self.d(type="StaticText", index=4).text
        orderCode_zlyd = self.d(type="StaticText", index=4).text
        self.salerbackone_ios()
        time.sleep(2)
        self.salerBack_ios()
        from winretaildealer_IOS import appdealerInformation_IOS
        cc = appdealerInformation_IOS("http://localhost:8100")
        cc.dealer_startapp_ios("14778786566","aa248163")
        jxs_code = cc.dealerCancleOrder(u"经销商取消订单")
        assert jxs_code == orderCode_zlyd
        self.saler_startapp_ios("14778786561","aa248163")
        self.d(label=u"我的").click()
        self.d(label=u"全部订单").click()
        time.sleep(2)
        print self.d(type="StaticText", index=3).text  # 状态
        assert self.d(type="StaticText", index=3).text == "订单已取消"
        print self.d(type="StaticText", index=4).text  # 下单时间
        print self.d(type="StaticText", index=5).text  # 商品数量和种类
        print self.d(type="StaticText", index=8).text  # 支付方式和金额
        print self.d(type="StaticText", index=10).text  # 经销商名称
        self.d(type="Cell").click()
        time.sleep(2)
        if self.d(label=u"您有一条新消息").exists:
            self.d(label=u"取消").click()
        print self.d(type="StaticText", index=4).text
        orderCode_zlyd_qx = self.d(type="StaticText", index=4).text
        assert orderCode_zlyd_qx == orderCode_zlyd

#我的优惠券
    def salerMycoupon(self,mobile):
        self.d(label=u"我的").click()
        self.d(label=u"优惠券").click()
        time.sleep(3)
        sum1 = self.d(className="StaticText", index=3).text#可使用
        sum2 = self.d(className="StaticText", index=5).text#已使用
        sum3 = self.d(className="StaticText", index=7).text#已过期
        print(sum1)
        print(sum2)
        print(sum3)
        self.d(label=u"可使用").click()
        from excelManage_ios import salerSql_IOS
        sumksy = salerSql_IOS.salerSUMMyCoupon(mobile,"可使用")
        print(sumksy)
        self.d(label=u"已使用").click()
        sumysy = salerSql_IOS.salerSUMMyCoupon(mobile, "已使用")
        print(sumysy)
        self.d(label=u"已过期").click()
        sumygq = salerSql_IOS.salerSUMMyCoupon(mobile, "已过期")
        assert  sumksy in sum1
        assert  sumysy in sum2
        assert  sumygq in sum3

#意见反馈
    def salerView(self,viewconnect,viewphone):
        self.d(label=u"我的").click()
        self.salertupian(Commonvariable.All_PHOTO_LIST+"salerview.1334x750.png")
        self.d(label=u"C）积分商城问题与反馈").click()
        self.d(type="TextView").set_text(viewconnect)
        self.d(label=u"完成").click()
        self.d(type="TextView", index=2).set_text(viewphone)
        self.d(label=u"完成").click()
        self.salertupian(Commonvariable.All_PHOTO_LIST + "qxwc_saler.1334x750.png")
        self.d(label=u"确定").click()














#随机数整数
    def salerNumrandom(self,m,n):
        import random
        s = random.randint(m,n)
        print  s
        print(type(s))
        return s


    def salerWebWait(self,x):
        i = 1
        while True:
            if x.exists:
                if i == 5:
                    print(".....")
                    break
                print(i)
                break
            else:
                time.sleep(2)
                i += 1



    def salertupian(self,a):
        #/Users/wangbin/Desktop/7.1334x750.png
        self.d.click_image(a)
        pass

    def salerStrtoDou(self,id):
        a = id.text
        c = a.strip(u'¥')
        b = float(c)
        return b

    def salerStrtoDou2(self,id,name):
        c = str(id).strip(name)
        b = float(c)
        return b
#购物车转化&预订单转化   d(className="StaticText", index=3).text
    def salergwcStrtoDou(self,id):
        a = id.text
        c = float(a.decode('utf8')[5:12].encode('utf8'))
        return c

   # & 预订单转化
    def saleryddStrtoDou(self,id):
        a = id.text
        c = float(a.decode('utf8')[4:12].encode('utf8'))
        return c

    def cangku(self):
        print self.d(className="StaticText", index=32)
        print self.d(className="StaticText", index=37)
if __name__ == '__main__':
    d = atx.connect("http://localhost:8100")
    print d(className="StaticText", index=31).text
    print d(className="StaticText", index=36).text
    if "¥" in d(className="StaticText", index=31).text:
        goodprice1 = d(className="StaticText", index=31).text
        if "¥" in d(className="StaticText", index=36).text:
            goodprice2 = d(className="StaticText", index=36).text
        elif "¥" in d(className="StaticText", index=35).text:
            goodprice2 = d(className="StaticText", index=35).text
        elif "¥" in d(className="StaticText", index=34).text:
            goodprice2 = d(className="StaticText", index=34).text
    elif "¥" in d(className="StaticText", index=28).text:
        goodprice1 = d(className="StaticText", index=28).text
        if "¥" in d(className="StaticText", index=33).text:
            goodprice2 = d(className="StaticText", index=33).text
        elif "¥" in d(className="StaticText", index=32).text:
            goodprice2 = d(className="StaticText", index=32).text
        elif "¥" in d(className="StaticText", index=31).text:
            goodprice2 = d(className="StaticText", index=31).text
    elif "¥" in d(className="StaticText", index=29).text:
        goodprice1 = d(className="StaticText", index=29).text
        if "¥" in d(className="StaticText", index=34).text:
            goodprice2 = d(className="StaticText", index=34).text
        elif "¥" in d(className="StaticText", index=33).text:
            goodprice2 = d(className="StaticText", index=33).text
        elif "¥" in d(className="StaticText", index=32).text:
            goodprice2 = d(className="StaticText", index=32).text
    elif "¥" in d(className="StaticText", index=30).text:
        goodprice1 = d(className="StaticText", index=30).text
        if "¥" in d(className="StaticText", index=35).text:
            goodprice2 = d(className="StaticText", index=35).text
        elif "¥" in d(className="StaticText", index=34).text:
            goodprice2 = d(className="StaticText", index=34).text
        elif "¥" in d(className="StaticText", index=33).text:
            goodprice2 = d(className="StaticText", index=33).text

    print goodprice1,goodprice2








































