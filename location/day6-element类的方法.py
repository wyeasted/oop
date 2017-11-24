#!/usr/bin/env python
#-*-coding:utf-8-*_
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time as t

def findID(driver,id):
    return driver.find_element_by_id(id)

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findID(driver,'kw').send_keys(u'测试测试测试')
t.sleep(2)
print driver.find_element_by_name('wd').get_attribute('name')
driver.quit()

