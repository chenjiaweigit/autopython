# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
def test_click():
    driver = webdriver.Firefox()
    driver.get("http://retail.wincrm.net:8203")
    WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("userAccount").send_keys("wangbinsaler"))


if __name__ == '__main__':
    test_click()


    # driver.find_element_by_id(id).send_keys(userAccount)
#
# driver = webdriver.Firefox()
# driver.get("http://retail.wincrm.net:8203")
# test_click("userAccount","wagnbinsaler")


