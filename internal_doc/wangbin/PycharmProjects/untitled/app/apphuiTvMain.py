# coding: utf-8
from wangye import wangyeInfomation_Tvnew
from appsaler import appsalerInformation
import time


if __name__ == '__main__':
    #需要验证
    # aa = wangyeInfomation_Tvnew()
    bb = appsalerInformation()
    # aa.wangyeLogin_newTv("http://tv.winhxd.com","15200001111","123456")
    # easyui_textbox_input1, easyui_textbox_input10 = aa.wangyetvNew_add(u"自动化新惠tv12", u"自动化测试惠Tv", r"newTv.mp4",
    #                                                                    r"newTv.png", u"汉西")
    # time.sleep(3)
    # aa.wangyetvNew_offiframe()
    # aa.wangeytvNew_shouloadAwards(u"汉西", "10", "50")  # 视频观看奖励
    # aa.wangyetvNew_offiframe()
    # aa.wangeytvNew_UploadAwards(u"汉西","10","100","1000")#上传视频奖励
    # time.sleep(3)
    # bb.appsaler_stop()
    bb.start_app()
    # bb.salerlogintrue("14778786568","ab248163")
    # tvname, name, edt_title, edit_info, result = bb.salerNewTv(u"自动化上传视频111", u"自动化个人签名111")#上传，个人信息设置
    # print edt_title
    # print edit_info
    # print result
    # aa.wangeytvNew_examine(edt_title,"0",u"汉西")#审核
    # aa.wangyetvNew_offiframe()
    # spname = aa.wangyeNewtv_RecommendingCommodities(u"自动化新惠tv12","1","lebaishi",u"脉动",u"5箱脉动600mlx15+2箱新雨瑞苏打水400mlx24")
    RecommendingCommodities1, RecommendingCommodities2 = bb.salerNewTv_RecommendingCommodities()#惠tv推荐购物车
    print (RecommendingCommodities1,RecommendingCommodities2)
    # if spname == RecommendingCommodities1 and RecommendingCommodities1 == RecommendingCommodities2:
    #     print "T"
    #     log = open('E://banben.txt', 'a+')
    #     log.write(
    #         '\n' + "（true）------版本-新惠tv推荐商品:"   "------" + str(spname) +str(RecommendingCommodities1)+str(RecommendingCommodities2) + "------" + time.strftime(
    #             "%Y-%m-%d %H:%M:%S",
    #             time.localtime()) + '\n')
    #     log.close()
    # else:
    #     print "F"
    #     log = open('E://banben.txt', 'a+')
    #     log.write(
    #         '\n' + "（Flase）------版本-新惠tv推荐商品:"   "------" + str(spname) +str(RecommendingCommodities1)+str(RecommendingCommodities2) + "------" + time.strftime(
    #             "%Y-%m-%d %H:%M:%S",
    #             time.localtime()) + '\n')
    #     log.close()

    # aa.wangyeNewtv_RecommendingCommodities_del()
    bb.salerBack()

    newtvname = bb.salerNewTvshou(u"自动化观看视频发送评论")#视频观看操作
    # aa.wangyeNewtv_Barragereview(u"后台上传", "0")  # 审核评论
    # print newtvname

