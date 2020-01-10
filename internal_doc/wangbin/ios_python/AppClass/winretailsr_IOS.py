#-*- coding: UTF-8 -*-
from decimal import Decimal
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Commonvariable

import atx
import time

package_namesr = 'com.winchannel.winretailsr'
class appsrrInformation_IOS:
    def __init__(self,ip):
        self.d = atx.connect(ip)

    def assert_sr(self,m):
        assert m.exists
        pass

    def srbackone_ios(self):
        self.d.click_image("/Users/wangbin/Desktop/fanhui.1334x750.png")
        pass

#登陆
    def srStartapp_ios(self,loginphone,loginpwd):
        self.d.start_app(package_namesr)
        if self.d(label=u"登录").exists:
            self.d(type="TextField", index=1).set_text(loginphone)
            self.d(label=u"完成").click()
            self.d(type="SecureTextField", index=1).set_text(loginpwd)
            self.d(label=u"完成").click()
            self.d(label=u"登录").click()
            time.sleep(3)

            if self.d(label=u"联系客服").exists:
                print("登陆限制")
                self.d(label=u"取消").click()
            else:
                pass

        if self.d(label=u"允许").exists:
            self.d(label=u"允许").click()
        else:
            pass

#业代激活
    #门店名称，姓名，年龄，性别，所在地区，详细地址，标准建筑，门牌号，经营形式，共同经营人数，经营范围，
    # 单体？连锁，营业时间，店铺渠道，主营品类，店铺面积，商圈，移动支付，收银台数量，拍照4
    def  srActive_ios(self,active_phone,storename,name,storeaddr,storejianzhu,storenum):
        self.d(label=u"我的门店", name=u"我的门店", type="Button").click()
        self.srtupian(Commonvariable.All_PHOTO_LIST+"sralive.1334x750.png")
        self.d(type="TextField", index=1).set_text(active_phone)
        self.d(label=u"完成").click()
        self.d(label=u"创建").click()
        time.sleep(3)
        self.d(type="TextField", index=1).set_text(storename)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=2).set_text(name)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=3).set_text("22")
        self.d(label=u"完成").click()
        self.d(label=u"性别").click()
        time.sleep(2)
        self.d(label=u"确定").click()
        self.d(label=u"所在地区").click()
        time.sleep(5)
        while True:
            if self.d(label=u"进行中", name=u"进行中", type="ActivityIndicator").exists:
                time.sleep(3)
                continue
            else:
                break
        if self.d(label=u"北京市").exists:
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
            self.d(className="StaticText", index=2).click()
        else:
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
            self.d(className="StaticText", index=2).click()
            time.sleep(2)
        self.d(label=u"街道，楼牌号等").set_text(storeaddr)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=5).set_text(storejianzhu)
        self.d(label=u"完成").click()
        self.d(type="TextField", index=6).set_text(storenum)
        self.d(label=u"完成").click()
        self.d(label=u"经营形式").click()
        self.d(label=u"确定").click()
        self.d(label=u"共同经营人数").click()
        self.d(label=u"确定").click()
        self.d(label=u"经营范围").click()
        self.d(label=u"确定").click()
        self.d(label=u"单体/连锁").click()
        self.d(label=u"确定").click()
        self.d(label=u"营业时间").click()
        self.d(label=u"确定").click()
        self.d(label=u"店铺渠道").scroll().click()
        self.d(label=u"确定").click()
        self.d(label=u"主营品类").scroll().click()
        self.d(label=u"母婴玩具").click()
        time.sleep(4)
        self.d(label=u"确定").click()
        self.d(label=u"店铺面积").scroll().click()
        self.d(label=u"确定").click()
        self.d(label=u"商圈").scroll().click()
        self.d(label=u"确定").click()
        self.d(label=u"移动支付").scroll().click()
        self.d(label=u"确定").click()
        self.d(label=u"收银台数量").scroll().click()
        self.d(label=u"确定").click()
        for i in range(2):
            self.d.swipe(500, 1000, 500, 500)
        #拍照
        self.d(label=u"addpicture@2x").click()
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


        time.sleep(2)
        self.srtupian(Commonvariable.All_PHOTO_LIST+"srsave.1334x750.png")
        self.d(label=u"确定").click()
        self.d(type="Cell", index=2).click()
        self.d(label=u"临时保存").click()


# 图片点击
    def srtupian(self, a):
        # /Users/wangbin/Desktop/banbentupian/add.1334x750.png
        self.d.click_image(a)
        pass

if __name__ == '__main__':
    d = atx.connect("http://localhost:8100")
    # c = atx.connect("http://localhost:8200")
    #
    # # d.start_app(package_namesr)
    # c.start_app('com.winchannel.winretailsaler')








