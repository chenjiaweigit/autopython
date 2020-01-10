from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://baidu.com')
print("go to http://baidu.com")
yuansu = driver.find_element_by_id('kw')
yuansu.send_keys('selenuim')
driver.find_element_by_id('su').click()
driver.set_window_size(700,1000)
driver.find_element_by_link_text(" - 标签 - 上海-悠悠 - 博客园")
driver.find_element_by_link_text(" - 标签 - 上海-悠悠 - 博客园").click()
driver.find_element_by_xpath("")