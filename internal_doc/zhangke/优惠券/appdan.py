# coding=utf8
from appaddr import *
import time

class appPhone():
    lists = []
    listz = []
    listf = []
    listb = []
    listv = []
    user = appFunction()
    def orders(self):
        # 选择乳品饮料-脉动
        self.user.youobj()
        man = d(resourceId="winretailsaler.net.winchannel.wincrm:id/mtv_month_label").text
        self.lists.append(man)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        time.sleep(2)
        for i in range(2):
            d.swipe(300, 700, 300, 300)
        ops = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_price").text[1:6])
        self.listv.append(ops)
    def nameobj(self):
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        d.keyevent("BACK")
        d.keyevent("BACK")
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_send_goods").click()
        obje = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/payreceive_money").text[1:6])
        self.listb.append(obje)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(text=u"确定").click()
        d(text=u"试试怎么用").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/applybtn").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        d.keyevent("BACK")
        d(text=u"优惠券").click()
        if d(description=u"满减嘿嘿").wait.exists():
            ma = d(description=u"满减嘿嘿").description
            self.listz.append(ma)
        else:
            self.ccc("取消订单优惠券没有返回")
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").click()

    def correct(self):
        self.user.youobj()
        man1 = d(resourceId="winretailsaler.net.winchannel.wincrm:id/mtv_month_label").text
        self.listf.append(man1)
        time.sleep(2)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        d.keyevent("BACK")
        d.keyevent("BACK")
        d.keyevent("HOME")
        d(text=u"惠下单经销商").click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
          instance=1).click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/modify_order_button").click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_decrease_one").click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/btn_decrease_one").click()
        d.swipe(300, 1000, 300, 200)
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/win_dialog_one_btn").click()
        d(text=u"修改价格").click()
        d(resourceId="winretaildealer.net.winchannel.wincrm:id/applybtn").click()
        d(text=u"确定").click()
        time.sleep(2)
        d.keyevent("BACK")
        d.keyevent("HOME")
        d(text=u"惠下单").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        d(text=u"优惠券").click()
        if d(description=u"满减嘿嘿").wait.exists():
            ma1 = d(description=u"满减嘿嘿").description
            self.listf.append(ma1)
        else:
            self.ccc("经销商修改订单优惠券没有返回")
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/back").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/component_maintab_tab_textview").click()

    #满赠优惠券
    def maze(self, z, y, n):
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"乳品饮料").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_brand_bg").click()
        for i in range(3):
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/coupons_titlt").click()
        # 选第一个优惠券
        if d(text=z).wait.exists():
            d(text=z).click()
        else:
            self.ccc(y)
        time.sleep(2)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        self.ccc(n)
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        d.keyevent("BACK")
        d.keyevent("BACK")
    def much_Reduction(self):
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"乳品饮料").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_brand_bg").click()
        for i in range(3):
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/coupons_titlt").click()
        if d(text=u"品牌满减") == u"品牌满减" and d(resourceId="winretailsaler.net.winchannel.wincrm:id/mcoupon_select") ==u"可选择":
            d(text=u"品牌满减").click()
        else:
            pass
        if d(text=u"供应满减").wait.exists():
            d(text=u"供应满减").click()
        else:
            self.ccc("多优惠券使用供应满减失败")
        if d(text=u"满减嘿嘿").wait.exists():
            d(text=u"满减嘿嘿").click()
        else:
            self.ccc("多优惠券使用满减嘿嘿失败")
        if d(text=u"供应满减").wait.exists() and d(text=u"满减嘿嘿").wait.exists() and d(text=u"品牌满减").wait.exists():
            self.ccc("true---多优惠卷使用成功一共使用了三张品牌满减,供应满减,惠下单满减")
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/ok_button").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/rightbtn").click()
        d.keyevent("BACK")
        d.keyevent("BACK")

    def ccc(self, e):
        fileHandler = file(r'E:\nice.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()





