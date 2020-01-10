#coding=utf-8
from appdan import *
from appaddr import *
from youhuijuan import *
import time

def iii(a, b, x):
    fileHandler = file(r'E:\nice.txt', 'a+')  # 或者调用open()函数
    fileHandler.write("\r\n")
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    if (a == b):
        fileHandler.write("true---" + x + "________" + t)
        fileHandler.write("\r\n")
    else:
        fileHandler.write('false---' + x + "________" + t)
    # fileHandler.write("————————————————————————————————————————")
    fileHandler.seek(0)
    # contents = fileHandler.read()
    # print contents
    fileHandler.close()

if __name__ == '__main__':
    boyd = coupon()
    boyd.voucher() #嘿嘿满减
    numb1 = boyd.title
    names = appPhone()
    numb = appFunction()
    names.orders()
    value1 = numb.monry()
    value2 = numb.monry1()
    value3 = numb.monrys()
    value4 = numb.monryi()
    valus = value1 - value2
    iii(valus, value4, "预订单页面金额计算")
    names.nameobj()
    names.correct()
    zz = names.listv
    nn = names.listz
    cc = names.lists
    ll = names.listb
    iii(zz, ll, "预订单和待发货金额效验")
    iibs = names.listf
    iii(iibs[0], iibs[1], "经销商修改订单优惠券返回成功")
    iii(cc, nn, "经销商取消订单优惠券返回成功")
    iii(numb1, cc, "web和app优惠卷是不是同一张")
    boyd.gifts() #哈哈满赠
    names.maze(u"满赠呵呵", "false---惠下单满赠品牌优惠卷使用失败", "true---惠下单满赠品牌优惠卷使用成功")
    boyd.threshold_Order() #惠下单满减订单无门槛优惠卷
    names.maze(u"惠满减槛", "false---惠下单满减订单无门槛优惠卷使用失败", "true---惠下单满减订单无门槛优惠卷使用成功")
    boyd.mold_Order()  # 惠下单满减优惠券类型排他
    names.maze(u"惠减优排", "false---惠下单满减优惠券类型排他使用失败", "true---惠下单满减优惠券类型排他使用成功")
    boyd.unliMited_Order()  # 惠下单满减订单无限制
    names.maze(u"惠满减无", "false---惠下单满减订单无限制优惠券使用失败", "true---惠下单满减订单无限制优惠券使用成功")
    boyd.brand_Order()  # 品牌商满减订单
    boyd.reduction()# 惠下单按件减商品
    boyd.piece()#惠下单按件赠系列
    boyd.voucher_Scopen()#惠下单满减指定商品范围
    boyd.supplier_Order()#供应商满减订单出资方排他
    boyd.exclusion_Order()#惠下单满减订单全排它
    names.much_Reduction()

