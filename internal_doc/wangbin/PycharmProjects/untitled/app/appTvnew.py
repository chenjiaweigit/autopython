# coding: utf-8
import time
from wangye import wangyeInfomation_Tvnew
from appsaler import appsalerInformation
from pymssqlManage import excelManager
saler,dealer,sr,express,htv,pc = excelManager.banbeninfo("retail",r"E:\banben\banben.xlsx")

#新的惠tv
if __name__ == '__main__':
    #1660313
    bb = appsalerInformation("192.168.253.3:7912")
    aa = wangyeInfomation_Tvnew()
    aa.wangyeLogin_newTv(htv[1],htv[2],htv[3])#登录后台
    spname = aa.wangyeNewtv_RecommendingCommodities(htv[4],htv[5],htv[6],htv[7],htv[8])
    bb.salerNewTv_RecommendingCommodities(htv[4])#惠tv推荐购物车
    aa.wangyeNewtv_RecommendingCommodities_del()
    bb.salerLog_banben(dealer[6],dealer[25])

    # easyui_textbox_input1,easyui_textbox_input10 = aa.wangyetvNew_add(u"自动化新惠tv3",u"自动化测试王斌",r"newTv.mp4",r"newTv.png",u"汉西")
    # # time.sleep(6)
    # # aa.wangyetvNew_iframe("mainFrame")
    # aa.wangyetvNew_topstick(u"自动化新惠tv3")#easyui_textbox_input1
    # aa.wangeytvNew_UploadAwards(u"汉西","10","100","1000")#上传视频奖励

    # aa.wangeytvNew_shouloadAwards(u"汉西","10"," 50")#视频观看奖励
    # newtvname = bb.salerNewTvshou(u"自动化观看视频发送评论")#视频观看操作
    # aa.wangyeNewtv_Barragereview(u"后台上传", "0")  # 审核评论
    # print newtvname
    bb.backCommonMethod()
    tvname, name, edt_title, edit_info, result = bb.salerNewTv(u"自动化上传视频2222", u"自动化个人签名2222")#上传，个人信息设置
    # aa.wangeytvNew_examine(edt_title,"0",u"c")#审核

