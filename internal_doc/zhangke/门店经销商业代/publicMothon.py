# coding=utf8
import time
import pymssql
import atx

package_namesaler = 'winretailsaler.net.winchannel.wincrm'
package_namesr = 'winretailsr.net.winchannel.wincrm'
d = atx.connect()


class public_month():
    def yyy(self, e):
        fileHandler = file(r'E:\duanshipin.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()

    def sss(self, e):
        fileHandler = file(r'E:\xkgood.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()

    def uuu(self, e):
        fileHandler = file(r'E:\zke.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()



    def ccc(self, e):
        fileHandler = file(r'E:\hellokiyy.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()
    def zzz(self, e):
        fileHandler = file(r'E:\liuhuang.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(e + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()

    def ttt(self, f):
        fileHandler = file(r'E:\helloman.txt', 'a+')
        fileHandler.write("\r\n")
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        fileHandler.write(f + "______________" + t)
        fileHandler.write("\r\n")
        fileHandler.seek(0)
        fileHandler.close()
    def database(self,x):
        conn = pymssql.connect("118.186.244.9:1433", "wangbin", "wb@HYTX.2017", "CRM_RETAIL")
        cursor = conn.cursor()
        # sqlname = "select CUSTOMER_ID FROM CRM_WS_CUSTOMER where MOBILE = " + x + ""
        sqlname = "update CRM_WS_CUSTOMER set IMEI = '5215200'where MOBILE = '" + x + "' "
        cursor.execute(sqlname)
        conn.commit()
        # data = cursor.fetchone()
        # print data
        conn.close()
    def databaseselect(self, x):
        conn = pymssql.connect("118.186.244.9", "wangbin", "wb@HYTX.2017", "CRM_RETAIL")
        cursor = conn.cursor()
        sqlname = "select content FROM SMSSEND where telephone = '" + x + "' "
        cursor.execute(sqlname)
        # conn.commit()
        data = cursor.fetchone()
        cc = eval("u" + "\'" + data[0] + "\'")[9:15]
        conn.close()
        return cc
    def databaseSrJiHuo(self, n):
        conn = pymssql.connect("118.186.244.9", "wangbin", "wb@HYTX.2017", "CRM_RETAIL")
        cursor = conn.cursor()
        sqlnames = "select SMS_CODE FROM CRM_WS_CUSTOMER where MOBILE = '" + n + "' "
        cursor.execute(sqlnames)
        # conn.commit()
        data = cursor.fetchone()
        vv = eval("u" + "\'" + data[0] + "\'")
        conn.close()
        return vv
    def yeDaizhuce(self,bbp,sn):
        d(text=u"ATX助手").click()
        time.sleep(2)
        d(text=u"输入法设置").click()
        time.sleep(2)
        d(resourceId="android:id/summary").click()
        d(resourceId="vivo:id/radio", className="android.widget.RadioButton", instance=2).click()
        d.keyevent("BACK")
        d.keyevent("BACK")
        d.start_app(package_namesr)
        d(resourceId="winretailsr.net.winchannel.wincrm:id/component_maintab_tab_textview", text=u"我的门店").click()
        d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=1).click()
        time.sleep(3)
        d.keyevent("BACK")
        time.sleep(2)
        d.keyevent("BACK")
        d(resourceId="winretailsr.net.winchannel.wincrm:id/imageview", className="android.widget.ImageView",
               instance=1).click()
        time.sleep(10)
        for i in range(3):
            d.swipe(400, 600, 600, 1900)
        time.sleep(10)
        d(resourceId="winretailsr.net.winchannel.wincrm:id/search_editview").set_text(bbp)
        time.sleep(1)
        d(resourceId="winretailsr.net.winchannel.wincrm:id/search_editview").click()
        time.sleep(2)
        d.click(0.92, 0.768)
        time.sleep(3)
        ttp = d(resourceId="winretailsr.net.winchannel.wincrm:id/tv_store_name").text
        ooo = ttp.encode("utf-8")
        if ooo == sn:
            self.zzz("(true)业代我的门店看填写也带邀请码的门店成功")
        else:
            self.zzz("(false)业代我的门店看填写也带邀请码的门店失败")
            pass
        d.keyevent("BACK")
        d.keyevent("BACK")




