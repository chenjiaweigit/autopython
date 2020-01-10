# coding=utf8

import atx
d = atx.connect()
class appFunction():
    def youobj(self):
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/brand_tab_name", text=u"乳品饮料").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/item_brand_bg").click()
        for i in range(3):
            d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_increase").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/btn_ok").click()
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/coupons_titlt").click()
        # 选第一个优惠券
        d(resourceId="winretailsaler.net.winchannel.wincrm:id/mcoupon_select").click()

    def monry(self):
        mon = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/sum_money_textview").text[1:10])
        return mon
    def monry1(self):
        mon1 = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/favourable_money_textview").text[2:10])
        return mon1
    def monrys(self):
        mons = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/actual_payment_textview").text[1:10])
        return mons
    def monryi(self):
        monsis = float(d(resourceId="winretailsaler.net.winchannel.wincrm:id/tv_price").text[1:7])
        return monsis

