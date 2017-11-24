#!/usr/bin/env python
#-*-coding:utf-8-*_

from selenium import webdriver
import time as t
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
#获取text内容
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
#driver.get('file:///E:/Git/html/html/index.html')
#driver.find_element_by_name('Submit').click()
#print driver.switch_to_alert().text
#driver.switch_to_alert().accept()
#driver.quit()

#确认和取消对话框
# driver.find_element_by_name('Submit2').click()
# print driver.switch_to_alert().text
# t.sleep(3)
# driver.switch_to_alert().dismiss()
# print driver.switch_to_alert().text
# t.sleep(3)
# driver.switch_to_alert().accept()
# t.sleep(3)
# driver.find_element_by_name('Submit2').click()
# t.sleep(3)
# driver.switch_to_alert().accept()
# t.sleep(4)
# driver.quit()

# 输入文本信息

# driver.find_element_by_name('Submit3').click()
# driver.switch_to_alert().send_keys(u'王怡')
# t.sleep(3)
# driver.switch_to_alert().accept()
# t.sleep(3)
# print driver.switch_to_alert().text
# driver.switch_to_alert().accept()
# driver.quit()

#鼠标事件
driver.get('file:///E:/Git/html/html/disabledOnContextMenu/index.html')
action=ActionChains(driver)
element=driver.find_element_by_css_selector('body > div:nth-child(1)')
action.context_click(element).perform()
t.sleep(3)
driver.find_element_by_link_text(u'源码之家').click()
t.sleep(3)
driver.quit()






























