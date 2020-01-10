#-*- coding: UTF-8 -*-
from decimal import Decimal

import atx
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Commonvariable
package_namedeler = 'com.winchannel.winretaildealer'
class appdealerInformation_IOS:
    def __init__(self,ip):
        self.d = atx.connect(ip)
        pass

# 封装click（）+set_text方法
    def dealerClick_ios(self, iosID):
        self.d(label=iosID).click()
        pass

    def dealerSet_text_ios(self, iosID, iosSet_text):
        self.d(label=iosID).set_text(iosSet_text)
        pass

    # 启动登陆门店app
    def dealer_startapp_ios(self,login_phone,login_pwd):
        self.d.start_app(package_namedeler)
        if self.d(label=u"忘记密码?").exists:
            self.d(type="TextField", index=1).set_text(login_phone)
            self.d(type="SecureTextField", index=1).set_text(login_pwd)
            self.d(label=u"完成").click()
            self.d(label=u"登录").click()
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

        else:
            print("222")
        time.sleep(5)

        if self.d(label=u"您有一条新消息").exists:
            self.d(label=u"取消").click()
        if self.d(label=u"禁止登录提示", name=u"禁止登录提示", type="StaticText").exists:
            self.d(label=u"取消").click()
            self.d.stop_app(package_namedeler)
        time.sleep(3)
        if self.d(label=u"合作协议").exists:
            print("新账号，需要签写合作协议")
        else:
            print("不是新账号，登陆成功")
        pass

#经销商第一次登陆
    def dealerjxsOnelogin_ios(self,regname,farenname,rangcode,busnum,pnum):
        self.d(label=u"下一步").click()
        self.d(label=u"下一步").click()
        time.sleep(5)
        self.d(type="TextField", index=1).set_text(regname)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=2).set_text(farenname)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=6).set_text(rangcode)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=8).set_text(busnum)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=9).set_text(pnum)
        self.d(label=u"完成").click()
        self.d(label=u"开户城市").click()
        self.d(label=u"北京市").click()
        self.d(label=u"开户行").click()
        self.d(label=u"交通银行").click()
        self.d(label=u"开户支行").click()
        self.d(label=u"交通银行北京光华路支行").click()
        self.d(label=u"同法人代表").click()
        self.d(label=u"下一步").click()
        self.d(label=u"开始使用").click()
        assert self.d(label=u"订单管理", name=u"订单管理", type="Button").exists
        pass

#经销商惠聊发优惠券
    def dealerHuiliao_ios(self,startNum):
        self.d(label=u"惠聊").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"tongxunlu.1334x750.png")
        self.d(type="TextField", index=1).set_text("61")
        self.d(label=u"完成").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_huiliaoer.1334x750.png")
        time.sleep(3)
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"yuyin.1334x750.png")
        time.sleep(3)
        self.d(label=u"icon toolview add normal").click()
        self.d(label=u"优惠券").click()
        self.d(type="Cell").click()
        self.d(label=u"发送红包").click()
        import winretailsaler_IOS
        bb = winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
        bb.saler_startapp_ios("15122674750","111")
        time.sleep(3)
        print(".............")
        print(startNum)
        endNum = bb.salerhuiliaoyouhuiquan()
        print(endNum)
        assert endNum-startNum ==1
        pass

#退出登陆
    def dealerOfflogin_ios(self):
        self.d(label=u"我的").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"ixs_shezhi.1334x750.png")
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"jxs_offlogin.1334x750.png")
        self.d(label=u"确定").click()
        assert self.d(label=u"登录").exists
        pass
#jxs角色权限
    def dealerJxsPower_ios(self,role):
        if "jxs" is role:
            self.d(label=u"订单管理", name=u"订单管理", type="Button").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"jxs_order.1334x750.png")
            self.d(label=u"货架管理").click()
            assert u"货架管理" in self.d(className="StaticText",index=1).text
            self.d(label=u"门店管理").click()
            assert u"门店管理" in self.d(className="StaticText", index=1).text
            self.d(label=u"我的").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"jxs_wode.1334x750.png")
            print(role)
        elif "shsj" is role:
            self.d(label=u"订单管理", name=u"订单管理", type="Button").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"shsj_order.1334x750.png")
            self.d(label=u"货架管理").click()
            assert u"货架管理" not in self.d(className="StaticText",index=2).text
            self.d(label=u"门店管理").click()
            assert u"门店管理" not in self.d(className="StaticText", index=2).text
            self.d(label=u"我的").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"shsj_wode.1334x750.png")
            print(role)
        elif "cxsj" is role:
            self.d(label=u"订单管理", name=u"订单管理", type="Button").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"cxsj_order.1334x750.png")
            self.d(label=u"货架管理").click()
            assert u"货架管理" not in self.d(className="StaticText", index=2).text
            self.d(label=u"门店管理").click()
            assert u"门店管理" not in self.d(className="StaticText", index=2).text
            self.d(label=u"我的").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"cxsj_wode.1334x750.png")
            print(role)
        elif "sdy" is role:
            self.d(label=u"订单管理", name=u"订单管理", type="Button").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"sdy_order.1334x750.png")
            self.d(label=u"货架管理").click()
            assert u"货架管理"  in self.d(className="StaticText", index=1).text
            self.d(label=u"门店管理").click()
            assert u"门店管理"  in self.d(className="StaticText", index=1).text
            self.d(label=u"我的").click()
            assert self.d.exists(Commonvariable.All_PHOTO_LIST+"sdy_wode.1334x750.png")
            print(role)
        elif "pss" is role:
            pass
        else:
            pass

#jxs货架管理
    def dealerjxsGoodsshelves_ios(self,jxs_sousuo,jxs_price,login_phone,login_pwd):
        self.d(label=u"货架管理").click()
        time.sleep(4)
        self.d(label=u"搜索", name=u"搜索", type="SearchField", index=1).set_text(jxs_sousuo)
        self.d(label=u"搜索").click()
        self.d(label=u"edit@2x").click()
        self.d(type="TextField", index=2).clear_text()
        self.d(type="TextField", index=2).set_text(jxs_price)
        # self.d(label=u"库存紧张").click()
        self.d(label=u"完成").click()
        self.d(label=u"保存").click()
        time.sleep(2)
        globaltext = "357.99"
        if self.d(label=u"保存").exists:
            print(self.d(label=u"保存").exists)
            self.d(type="TextField", index=2).clear_text()
            self.d(type="TextField", index=2).set_text(globaltext)
            self.d(label=u"完成").click()
            self.d(label=u"保存").click()
        else:
            print(self.d(label=u"保存").exists)
            pass
        time.sleep(5)
        self.d.swipe(300, 300, 300, 600)
        self.dealerOfflogin_ios()
        self.dealer_startapp_ios(login_phone,login_pwd)
        self.d(label=u"货架管理").click()
        time.sleep(3)
        self.d(label=u"搜索", name=u"搜索", type="SearchField", index=1).set_text(jxs_sousuo)
        # print (self.d(className="StaticText", index=5).text).strip(u'  默认渠道')
        c = str(self.d(className="StaticText", index=4).text.strip(' 默认渠道'))

        m = c.strip(u'￥')
        shelves_price = str(m)
        assert shelves_price in jxs_price or shelves_price in globaltext
        pass

#人员管理
    def dealerRoleManage_ios(self,rolename,rolephone,jxsphone,jxspwd):
        self.d(label=u"我的").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"jxs_rolem.1334x750.png")
        time.sleep(5)
        self.d(label=u"添加人员").click()
        self.d(type="TextField", index=1).set_text(rolename)
        self.d(type="TextField", index=2).set_text(rolephone)
        self.d(label=u"完成").click()
        # self.dealertupian("Users/wangbin/Desktop/banbentupian/1212.1334x750.png")
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_addrole.1334x750.png")
        self.dealerbackone_ios()
        self.d(label=u"保存").click()
        #修改角色
        self.d(type="Cell").click()
        time.sleep(4)
        hq_name = self.d(className="StaticText", index=3).text
        hq_phone = self.d(className="StaticText", index=6).text
        self.cannelsesion()
        assert hq_name in rolename
        assert hq_phone in rolephone
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_qhrole.1334x750.png")
        self.d(label=u"送货司机").click()
        self.dealerbackone_ios()
        self.d(label=u"重置密码").click()
        self.d(label=u"确认重置").click()
        self.dealerbackone_ios()
        self.dealerbackone_ios()
        self.dealerOfflogin_ios()
        self.dealer_startapp_ios(rolephone,rolephone)
        self.d(label=u"我的").click()
        assert self.d.exists(Commonvariable.All_PHOTO_LIST+"shsj_wode.1334x750.png")
        self.dealerOfflogin_ios()
        self.dealer_startapp_ios(jxsphone,jxspwd)
        self.d(label=u"我的").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"jxs_rolem.1334x750.png")
        self.d(type="Cell").click()
        time.sleep(4)
        self.d(label=u"删除此用户").click()
        self.d(label=u"删除").click()
        self.dealerbackone_ios()
        self.dealerOfflogin_ios()
        self.dealer_startapp_ios(rolephone,rolephone)
        pass

#门店管理
    def dealerStoreManage(self,jxsstorename):
        self.d(label=u"门店管理").click()
        time.sleep(3)
        self.d(label=u"搜索门店", name=u"搜索门店", type="SearchField", index=1).set_text(jxsstorename)
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_search.1334x750.png")
        time.sleep(5)
        if self.d(label=u"默认", name=u"默认", type="StaticText").exists:
            self.d(label=u"默认", name=u"默认", type="StaticText", index=1).click()
            time.sleep(3)
            assert self.d(className="StaticText", index=5).text is not ""
            assert self.d(className="StaticText", index=7).text is not ""
            assert self.d(className="StaticText", index=9).text is not ""
            assert self.d(className="StaticText", index=11).text is not ""
            assert self.d(className="StaticText", index=13).text is not ""
            assert self.d(className="StaticText", index=15).text is not ""
            self.d(className="StaticText", index=11).click()
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"AB.1334x750.png")
            time.sleep(2)
            aB = self.d(className="StaticText", index=11).text
            print aB
            self.dealerbackone_ios()
            import winretailsaler_IOS
            bb =winretailsaler_IOS.appsalerInformation_IOS(Commonvariable.PORT)
            bb.salerStoreManage_ios(str(aB))
            bb.salerbackone_ios()
            bb.salerbackone_ios()

            print("xxxxxxxx")
            self.dealer_startapp_ios("14778786566","aa248163")
            time.sleep(2)
            self.d(label=u"门店管理").click()
            time.sleep(3)
            self.d(label=u"搜索门店", name=u"搜索门店", type="SearchField", index=1).set_text(jxsstorename)
            self.dealertupian(Commonvariable.All_PHOTO_LIST + "dealer_search.1334x750.png")
            self.d(label=u"默认").click()
            time.sleep(3)
            assert self.d(className="StaticText", index=5).text is not ""
            assert self.d(className="StaticText", index=7).text is not ""
            assert self.d(className="StaticText", index=9).text is not ""
            assert self.d(className="StaticText", index=11).text is not ""
            assert self.d(className="StaticText", index=13).text is not ""
            assert self.d(className="StaticText", index=15).text is not ""
            self.d(className="StaticText", index=11).click()
            self.dealertupian("/Users/wangbin/Desktop/banbentupian/moren.1334x750.png")
            moren = self.d(className="StaticText", index=11).text
            bb.salerStoreManage_ios(str(moren))
        else:
            print "渠道修改"
            pass
#订单筛选，搜索，送货地图
    def dealerjxsOrdersousuo_ios(self,sousuoname):
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_dfh.1334x750.png")
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_dfh_sousuo.1334x750.png")
        self.d(type="TextField", index=1).set_text(sousuoname)
        self.d(label=u"Search").click()
        self.d(label=u"三个月").click()
        self.d(label=u"一个月").click()

        self.dealerbackone_ios()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_dfh_ditu.1334x750.png")
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.dealerbackone_ios()
        self.d(label=u"只看今天").click()
        self.d(label=u"最近三天").click()
        self.d(label=u"一周之内").click()
        self.d(label=u"查看全部").click()



    def cannelsesion(self):
        if self.d(label=u"您有一条新消息", name=u"您有一条新消息", type="StaticText").exists:
            self.d(label=u"取消").click()
        else:
            pass

# dealer获取订单信息比较订单
    def dealerOrderinfo_ios(self, ordertype):
        global code
        self.dealerClick_ios(u"订单管理")
        time.sleep(4)
        self.cannelsesion()
        if str(ordertype) == "待确认":
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_dqr.1334x750.png")
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break

            # print d(type="StaticText", index=2).text  # 价格
            # # print d(type="StaticText", index=3).text  # 价格
            # print d(type="StaticText", index=4).text  # 下单时间
            # print d(type="StaticText", index=5).text  # 状态

            self.cannelsesion()
            assert self.d(label=u"修改订单").exists == True
            assert self.d(label=u"确认订单").exists == True
            assert self.d(type="StaticText", index=5).text == "订单待确认"
            self.cannelsesion()
            self.d(type="Cell").click()
            time.sleep(2)
            assert self.d(label=u"orderChange").exists
            print self.d(type="StaticText", index=3).text
            code = self.d(type="StaticText", index=3).text
            for i in range(3):
                self.d.swipe(500, 1500, 500, 500)
            assert self.d(label=u"取消订单").exists == True
            assert self.d(label=u"确认订单").exists == True
            self.dealerbackone_ios()
            self.d(label=u"确认订单").click()
            time.sleep(3)
            self.d(type="Cell", index=2).click()
            self.d(label=u"确定").click()

        elif str(ordertype) == "待发货":
            self.dealerClick_ios(u"订单管理")
            self.cannelsesioon()
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_dfh.1334x750.png")
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            assert self.d(label=u"64f546fef14a41279c61b867242425").exists == True
            assert self.d(label=u"d218ad907c9a4d57a1fd230d22f888").exists == True
            if self.d(label=u"待支付").exists:
                print(1)
            elif self.d(label=u"送货完成").exists:
                assert self.d(label=u"修改订单").exists == True
            # print d(type="StaticText", index=3).text  # 价格
            # # print d(type="StaticText", index=3).text  # 价格
            # print d(type="StaticText", index=4).text  # 下单时间
            # print d(type="StaticText", index=5).text  # 状态
            print self.d(type="StaticText", index=5).text  # 状态
            assert self.d(type="StaticText", index=5).text == "订单待发货"
            self.d(type="Cell").click()
            time.sleep(2)
            self.cannelsesioon()
            print self.d(type="StaticText", index=3).text
            code = self.d(type="StaticText", index=3).text
            time.sleep(2)
            for i in range(3):
                self.d.swipe(500,1500,500,500)
            if self.d(label=u"待支付").exists:
                assert self.d(label=u"关闭订单").exists==True
            elif self.d(label=u"送货完成").exists:
                assert self.d(label=u"取消订单").exists==True
            self.dealerbackone_ios()
            if self.d(label=u"送货完成").exists:
                self.d(label=u"送货完成").click()
                print("songhuowanchegn")
            elif self.d(label=u"待支付").exists:
                self.d(label=u"待支付").click()
                print("daizhifu")
            # while True:
            #     if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
            #         time.sleep(3)
            #         continue
            #     else:
            #         break
            time.sleep(3)
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_paizhao.1334x750.png")
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
            # self.d(label=u"我知道了").click()
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_qfk.1334x750.png")
            time.sleep(5)
            if self.d(label=u"取消").exists:
                print("确认品牌规定")
                self.d(label=u"确定").click()
            else:
                print("取消品牌规定")
                pass
            self.d(label=u"现金支付").click()
            self.d(label=u"确定").click()
            time.sleep(5)
            self.d.swipe(800,400,800,1500)
        elif str(ordertype) == "已完成":
            self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_ywc.1334x750.png")
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            assert self.d(label=u"359f9104589440dbb0b9ef1ed7b077").exists == True
            assert "已完成" in self.d(type="StaticText", index=5).text
            if self.d(label=u"取消").exists:
                self.d(label=u"取消").click()
            else:
                pass

            assert self.d(type="StaticText", index=5).text == "订单已收货"
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=3).text
            code = self.d(type="StaticText", index=3).text
            time.sleep(2)
            for i in range(3):
                self.d.swipe(500,1500,500,500)
        elif str(ordertype)=="关闭订单":
            self.dealerClick_ios(u"订单管理")
            self.dealertupian(Commonvariable.All_PHOTO_LIST + "dealer_dfh.1334x750.png")
            while True:
                if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                    time.sleep(3)
                    continue
                else:
                    break
            self.d(type="Cell").click()
            time.sleep(2)
            print self.d(type="StaticText", index=3).text
            code = self.d(type="StaticText", index=3).text
            time.sleep(2)
            for i in range(3):
                self.d.swipe(500,1500,500,500)
            self.d(label=u"关闭订单").click()
            self.d(label=u"确定").click()


        return code

    def dealerCancleOrder(self,review):
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"jxs_dqr.1334x750.png")
        time.sleep(2)
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        assert self.d(label=u"修改订单").exists == True
        assert self.d(label=u"确认订单").exists == True
        print self.d(type="StaticText", index=2).text  # 页面标题
        assert "待确认" in self.d(type="StaticText", index=2).text
        print self.d(type="StaticText", index=3).text  # 状态
        assert self.d(type="StaticText", index=3).text == "订单待确认"
        print self.d(type="StaticText", index=4).text  # 下单时间
        print self.d(type="StaticText", index=5).text  # 商品数量和种类
        print self.d(type="StaticText", index=8).text  # 支付方式和金额
        print self.d(type="StaticText", index=10).text  # 经销商名称
        self.d(type="Cell").click()
        time.sleep(2)
        assert self.d(label=u"orderChange").exists
        print self.d(type="StaticText", index=4).text
        jxs_code = self.d(type="StaticText", index=4).text
        for i in range(3):
            self.d.swipe(500, 1500, 500, 500)
        assert self.d(label=u"取消订单").exists == True
        assert self.d(label=u"确认订单").exists == True
        self.d(label=u"取消订单").click()
        self.d(label=u"确定").click()
        self.d(type="Button", index=8).click()
        self.d(type="TextView").set_text(review)
        self.d(label=u"完成").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST + "qxwc_saler.1334x750.png")
        self.d(label=u"确定").click()
        return jxs_code

    def cannelsesioon(self):
        if self.d(label=u"您有一条新消息").exists:
            self.d(label=u"取消").click()

#修改订单
    def dealerAlterOrder(self):
        self.cannelsesioon()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"jxs_dqr.1334x750.png")
        self.cannelsesioon()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealer_xgdd.1334x750.png")
        self.cannelsesioon()
        self.d(type="TextField", index=3).clear_text()
        import random
        s = random.randint(1, 10)
        print  s
        print(type(s))
        self.d(type="TextField", index=3).set_text(str(s))
        self.d(label=u"完成").click()
        spjg = self.d(type="TextField", index=2).text
        print(spjg)
        print(type(spjg))
        spjgtod = float(spjg) + 1.00
        self.d(type="TextField", index=2).clear_text()
        self.d(type="TextField", index=2).set_text(str(spjgtod))
        self.d(label=u"完成").click()
        time.sleep(4)
        # sumprice1 = self.dealerAlterprice()
        self.d(label=u"确认修改").scroll().click()
        time.sleep(3)
        xgddcg = float(self.d(className="StaticText", index=8).text)
        self.d(label=u"确定").click()
        self.d(type="Button", index=4).click()
        self.d(label=u"完成").click()
        self.d(label=u"确定").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        p = self.dealerStrtoDou2(self.d(type="StaticText", index=12).text,u'货到付款｜待收款: ¥')
        print p
        return p


#修改订单获取修改后商品数量价格的方法
    def dealerAlterprice(self):

        sumprice_xgdd = float(self.d(type="TextField", index=1).text) * int(self.d(type="TextField", index=3).text)+\
                        float(self.d(type="TextField", index=2).text) * int(self.d(type="TextField", index=4).text)
        print(sumprice_xgdd)
        return sumprice_xgdd

#经销商我的信息
    def dealerMyinfo(self,jxsname,jxsaddr,jxsgszcname):
        self.d(label=u"我的").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealerMyinfo.1334x750.png")
        self.dealertupian(Commonvariable.All_PHOTO_LIST + "dealer_wodeshengyi.1334x750.png")
        time.sleep(3)
        self.d(type="Image").click()
        self.d(label=u"经销商名称").click()
        self.d(type="TextField", index=1).clear_text()
        self.d(type="TextField", index=1).set_text(jxsname)
        self.d(label=u"完成").click()
        self.d(label=u"保存").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.d(label=u"详细地址").click()
        self.d(type="TextField", index=1).clear_text()
        self.d(type="TextField", index=1).set_text(jxsaddr)
        self.d(label=u"完成").click()
        self.d(label=u"保存").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.d(label=u"工商注册名称").click()
        self.d(type="TextField", index=1).clear_text()
        self.d(type="TextField", index=1).set_text(jxsgszcname)
        self.d(label=u"完成").click()
        self.d(label=u"保存").click()
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        self.d(label=u"营业执照").click()
        time.sleep(2)
        self.d(type="Image").click()
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
        time.sleep(3)
        self.dealerbackone_ios()
        self.d(label=u"头像").click()
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

#经销商意见反馈
    def dealerView(self,viewconnect,viewphone):
        self.d(label=u"我的").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST+"dealerview.1334x750.png")
        self.d(label=u"C）费用核销问题").click()
        self.d(type="TextView").set_text(viewconnect)
        self.d(label=u"完成").click()
        self.d(type="TextView", index=2).set_text(viewphone)
        self.d(label=u"完成").click()
        self.dealertupian(Commonvariable.All_PHOTO_LIST + "qxwc_saler.1334x750.png")
        self.d(label=u"确定").click()







#back one
    def dealerbackone_ios(self):
        self.d.click_image(Commonvariable.All_PHOTO_LIST+"fanhui.1334x750.png")
        pass

#图片点击
    def dealertupian(self,a):
        #/Users/wangbin/Desktop/7.1334x750.png
        self.d.click_image(a)
        pass

# 随机数整数
    def dealerNumrandom(self, m, n):
        import random
        s = random.randint(m, n)
        print  s
        print(type(s))
        return s

#str to double
    def dealerStrtoDou(self,id,):
        c = str(id).strip(u'¥')
        print c
        print(type(c))
        b = float(c)
        return b
    def dealerStrtoDou2(self,id,name):
        c = str(id).strip(name)
        print c
        print(type(c))
        b = float(c)
        return b



if __name__ == '__main__':
    d =atx.connect("http://localhost:8100")
    # print d(type="StaticText", index=2).text  #价格
    # # print d(type="StaticText", index=3).text  # 价格
    # print d(type="StaticText", index=4).text  # 下单时间
    # print d(type="StaticText", index=5).text  # 状态
    # print
    d(className="StaticText", index=9).click()















