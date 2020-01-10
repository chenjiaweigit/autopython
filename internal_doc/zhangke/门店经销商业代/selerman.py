from appLoin import *
from appOneloginjxs import *
from biglibao import *
from register import *
from salerjihuo import *
from xinyiqi.benefitTV import *
from yedaiyaoqingsaler import *


class adress():
    testsuite = unittest.TestSuite()
    testsuite.addTest(aler_loginTest("test_salerlogin1"))
    testsuite.addTest(aler_loginTest("test_salerlogin2"))
    testsuite.addTest(aler_loginTest("test_salerlogin3"))
    testsuite.addTest(aler_loginTest("test_salerlogin4"))
    testsuite.addTest(dealer_loginTest("test_dealerlogin1"))
    testsuite.addTest(dealer_loginTest("test_dealerlogin2"))
    testsuite.addTest(dealer_loginTest("test_dealerlogin3"))
    testsuite.addTest(dealer_loginTest("test_dealerlogin4"))
    testsuite.addTest(sr_loginTest("test_srlogin1"))
    testsuite.addTest(sr_loginTest("test_srlogin2"))
    testsuite.addTest(sr_loginTest("test_srlogin3"))
    testsuite.addTest(sr_loginTest("test_srlogin4"))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)
    #经销商初次登录
    call = dealer_appOneloginjxsTest()
    call.oneLogin_dealer("http://uat.wincrm.net:8218", "winretaildealer", "win!@#",
                         u"自动化测试", u"王斌", "14758742088", "aa248163", "0", "1", "15122674750",
                         u"打劣势交付落地时间发了多少积分收到了","100.0","40",u"普通经销商", u"汉西省", u"柏社村")
    #注册+注册送
    putdemo = charge()
    putdemo.enroll(u"我恩恩送送", "14013380931", "王晴天", "呵呵单元成功", "北京市中关村清河小营乔南100", "京-55465", "五彩大厦大厦", "14055368526")
    #邀请注册
    words = srYaoqing()
    words.invitation("支持原创哈哈哈", "14033990212", "任天行", "无可奈何花落去","北上广北三十米往上五十米", "北上广-009","无敌大转盘","14017911296")
    #门店激活
    generation = activated()
    generation.salerSr("14010285983","李自然","天时地利人和店","雪山之上无极之巅","悟道大厦北100","京冀蓝光-009","14017911296")
    #大礼包
    demo1 = big_GigLiBao()
    demo1.gift_Packs(u"此卷勿动",u"天时地利",u"春节快乐",u"李白的包",u"南京市及下属区县","14085234587","234587")
    #门店惠TV，经销商惠TV
    sdTV = saler_tv()
    sdTV.beneficial_TV(u"春眠不觉晓",u"不止往来",u"0",u"汉东",u"美的电视",u"好啦好啦",u"看看吧挺好的",u"1",u"艾欧尼亚","我的")







