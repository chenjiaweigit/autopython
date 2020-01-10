# coding: utf-8
import time
import uiautomator2 as ut2
package_nameexpress = 'winretailexpress.net.winchannel.wincrm'

class appexpressInformation:
    def __init__(self):
        self.d = ut2.connect('172.18.200.192:7912')
        pass

    '''start app'''
    def expressStart(self):
        self.d.app_start(package_nameexpress)
        pass

    ''' app返回 '''
    def expressBack(self):
        self.d.press("back")
        time.sleep(1)
        pass

    def asserttext(self,x,):
         assert x in self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/title").info[u"text"]

    '''登录
        账号，密码
        返回手机的品牌
    '''
    def expressLogin(self,et_username,et_pwd):
        if self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/btn_login").exists:
            self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_username").clear_text()
            self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_username").send_keys(et_username)
            self.expressBack()
            self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_pwd").clear_text()
            self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_pwd").send_keys(et_pwd)
            self.expressBack()
            self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/btn_login").click()
            device = self.d.device_info[u"brand"]
            print(device)
        else:
            device = self.d.device_info[u"brand"]
            print(device)
        return device

    '''司机管理'''
    def expressDriverManage(self,et_id_my_name,et_id_phone,et_id_number,phone_brand):
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/driver_mg").click()
        self.asserttext("司机管理")
        start = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        print(start)
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/add_person").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_id_my_name").send_keys(et_id_my_name)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_id_phone").send_keys(et_id_phone)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_id_number").send_keys(et_id_number)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/take_photo_tip").click()
        if "OPPO" in phone_brand:
            self.d(resourceId="com.oppo.camera:id/shutter_button").click()
            self.d(resourceId="com.oppo.camera:id/btn_done").click()
            self.d(resourceId="com.coloros.gallery3d:id/action_apply").click()

        elif "xiaomi" in phone_brand:
            print(2)
        else:
            print(3)
        time.sleep(2)
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/rightbtn").click()
        end1 = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        assert end1-start==1
        assert et_id_phone in self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/driver_phone").info[u"text"] and et_id_my_name in self.d(resourceId="win"
               "retailexpress.net.winchannel.wincrm:id/driver_name").info[u"text"]
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/reset_pwd").click()#重置密码
        hph_picture = self.appscreenshot()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/delete_driver").click()#删除司机
        end2 = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        print(end2)
        assert end1-end2 ==1 and end2==start
        self.express_banben("（true）------hph版本-司机管理:------",time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime()) )
        pass

    '''我的账号'''
    def expressMyinfo(self):
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/my_count").click()
        time.sleep(2)
        self.asserttext("我的账户")
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/imageview").click() #营业执照
        time.sleep(2)
        self.asserttext("营业执照")
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView", instance=1).click()
        self.asserttext("服务承诺")
        time.sleep(5)
        self.appscreenshot()
        self.express_banben("（true）------hph版本-我的账号:------",time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime()) )
        pass

    '''车辆管理:名称，车牌，长，宽，高，可载标箱，车辆类型，特殊属性'''
    def expressCarsmanage(self,et_car_name,et_car_no,et_car_len,et_car_width,et_car_height,et_car_box_count):
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/imageview").click()
        self.asserttext("车辆管理")
        start = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/add_car").click()
        self.asserttext("添加车辆")
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_name").send_keys(et_car_name)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_no").send_keys(et_car_no)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_len").send_keys(et_car_len)
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_width").send_keys(et_car_width)
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_height").send_keys(et_car_height)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/et_car_box_count").send_keys(et_car_box_count)
        self.expressBack()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/img").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/tv_ok").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/checkbox").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/rightbtn").click()
        end1 = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        assert end1-start ==1
        assert et_car_name in self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/car_name").info[u"text"]
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img").click()
        self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/delete_car").click()
        end2 = len(self.d(resourceId="winretailexpress.net.winchannel.wincrm:id/head_img"))
        assert end1-end2==1 and end2==start
        self.express_banben("（true）------hph版本-车辆管理:------",time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime()) )
        pass




    def express_banben(self,a,b):
        log = open('E://banben//hph_banben.txt', 'a+', encoding='utf-8')
        log.write(
            '\n' + a +b + '\n')

    def appscreenshot(self):#截图
        timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file = r'E:/banben/hph'
        self.d.screenshot('%s/%s.jpg'%(file,timestamp))
        pictruename = '%s\%s.jpg'%(file,timestamp)
        print(pictruename)
        return pictruename









