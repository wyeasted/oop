#!/usr/bin/env python
#-*-coding:utf-8-*_

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')

action=WebDriverWait(driver,1).until(expected_conditions.element_to_be_clickable((By.ID,'kw')))
action.send_keys(u'搜索')
driver.quit()