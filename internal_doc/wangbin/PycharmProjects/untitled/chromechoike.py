# coding: utf-8
from selenium import webdriver
import time


# driverOptions = webdriver.ChromeOptions()
# driverOptions.add_argument(r"user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")
# driver = webdriver.Chrome("chromedriver",0,driverOptions)
driver = webdriver.Chrome()
driver.get("http://tv.winhxd.com")  # 输入url
driver.maximize_window()  # 最大化
driver.find_element_by_name("username").send_keys("15200001111")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("submit").click()
time.sleep(2)
cookie= driver.get_cookies()
print (cookie)
driver.add_cookie(cookie)
