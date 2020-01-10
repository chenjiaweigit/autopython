# coding: utf-8
#!/usr/bin/env python
import time
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


if __name__ == '__main__':

    # 登陆（ok）
    from Main_Hxd import appLogin_IOS
    appLogin_IOS.appLogin()

    # # 门店地址管理（需要修改）
    # from Main_Hxd import appAddrmanage_IOS
    # appAddrmanage_IOS.appAddrmanage_IOS()
    # print("地址管理运行完成")
    # # 预定单（ok）
    # from Main_Hxd import appAgoorder_IOS
    # appAgoorder_IOS.appAgoorder_IOS()
    # print("预订单ok")
    # # 修改订单（ok）
    # from Main_Hxd import appChangeOrder_IOS
    # appChangeOrder_IOS.appChangeOrder_IOS()
    # print("修改订单运行完成ok")
    #关闭订单（ok）
    from Main_Hxd import appClosedOrder
    appClosedOrder.appClosedOrder()
    print("关闭订单ok")

    #首页(ok)
    from Main_Hxd import appHomemanage_IOS
    appHomemanage_IOS.appHomemanage_IOS()
    print("首页ok")

    #惠聊(ok)
    from Main_Hxd import appHuiliao_ios
    appHuiliao_ios.appHuiliao_IOS()
    print("惠聊ok")

    #经销商人员管理（ok）
    from Main_Hxd import appjxs_RoleManage_IOS
    appjxs_RoleManage_IOS.appjxs_RoleManage_IOS()

    #经销商货架管理(ok)
    from Main_Hxd import appjxsGoodsshelves_ios
    appjxsGoodsshelves_ios.appjxsGoodsshelves_IOS()


    #经销商我的信息（ok）
    from Main_Hxd import appJXSMyinfo_IOS
    appJXSMyinfo_IOS.appJXSMyinfo()
    print "jxs 我的信息完成"

    #经销商订单搜索(ok)
    from Main_Hxd import appjxsOrdersousuo_IOS
    appjxsOrdersousuo_IOS.appjxsOrdersousuo_IOS()
    print("经销商订单搜索校验完成。。。。。。。。。。。。。")

    #经销商权限管理(ok)
    from Main_Hxd import appJxsPower_ios
    appJxsPower_ios.appJxsPower()
    print("经销商权限管理校验完成。。。。。。。。。。。。。")

    #修改密码(ok)
    from Main_Hxd import appModifypwd_IOS
    appModifypwd_IOS.appModifypwd_IOS()
    print("修改密码校验完成。。。。。。。。。。。。。")


    # #意见反馈(ok)
    from Main_Hxd import appView_IOS
    appView_IOS.appView_IOS()
    print("意见反馈完成。。。。。。。。。。。。。")

    #仓库(ok)
    from Main_Hxd import appWarehouse_IOS
    appWarehouse_IOS.appWareHouse_IOS()
    print("仓库完成。。。。。。。。。。。。。")

    #购物车(ok)
    from Main_Hxd import appShoppingCart_IOS
    appShoppingCart_IOS.appShoppingCart_IOS()
    print("购物车完成。。。。。。。。。。。。。")



    # # #取消订单()
    # from Main_Hxd import appOrdersCannel_IOS
    # appOrdersCannel_IOS.appOrdersCannel_IOS()
    # print("取消订单。。。。。。。。。。。。。")



   #
   #
   #
    # # #注册
    # from Main_Hxd import appRegister_IOS
    # appRegister_IOS.appRegister_IOS()
   #
   #  # #激活
   #  # from Main_Hxd import appsrActive_IOS
   #  # appsrActive_IOS.appsrActive_IOS()
   #
   #
   #  # #退出登陆
   #  # from Main_Hxd import appOfflogin_ios
   #  # appOfflogin_ios.appOfflogin_IOS()
   #
   # # # 经销商第一次登陆
   # #  from Main_Hxd import appJxsOneLogin_IOS
   # #  appJxsOneLogin_IOS.appJxsOneLogin_IOS()
   #
   #  # #促销管理
   #  # from Main_Hxd import appPromotion_IOS
   #  # appPromotion_IOS.appPromotion_IOS()
   #  # print("促销管理。。。。。。。。。。。。。")
   #  #
   #  #门店管理
   #  from Main_Hxd import appStoreManage_IOS
   #  appStoreManage_IOS.appStoreManage_IOS()
   #  print("货架管理。。。。。。。。。。。。。")
#
#  # #我的优惠券(no ok)
#  # from Main_Hxd import appMyCoupon
#  # appMyCoupon.appMyCoupon_IOS()
#  # print("我的优惠券校验完成。。。。。。。。。。。。。")
    # #门店我的信息（需要修改）
    # from Main_Hxd import appMyinfo_IOS
    # appMyinfo_IOS.appMyinfo()
    # print("门店我的信息校验完成。。。。。。。。。。。。。")





