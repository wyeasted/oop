#!/usr/bin/env python
#-*-coding:utf-8-*_

from selenium import webdriver
import time as t
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#F5
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
#driver.get('http://www.baidu.com')
#driver.find_element_by_id('kw').send_keys(u'wangyi')
# driver.find_element_by_id('kw').send_keys(Keys.F5)
# t.sleep(3)
# driver.quit()

#F11
# driver.find_element_by_id('kw').send_keys(Keys.F11)
# t.sleep(3)
# driver.quit()

#F11
# driver.find_element_by_id('kw').send_keys(Keys.F12)
# t.sleep(3)
# driver.quit()

#ctrl a ctrl c ctrl v
# driver.find_element_by_id('kw').send_keys(u'公有云')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
# t.sleep(4)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
# t.sleep(3)
# driver.quit()

#id和索引 定位iframe
# driver.get('https://mail.qq.com/cgi-bin/loginpage')
# driver.switch_to_frame(0)
# driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# driver.find_element_by_xpath('//*[@id="u"]').send_keys('996327321')
# t.sleep(3)
# driver.quit()

#嵌套定位
#进入到第一个iframe
driver.switch_to_frame(0)
#进入到第二个iframe
driver.switch_to_frame('son')
driver.find_element_by_class_name('b_searchbox').send_keys(u'搜索')
t.sleep(2)
# 跳出iframe的框架
driver.switch_to_default_content()
t.sleep(3)
driver.find_element_by_id('userid').send_keys(u'搜索')
t.sleep(3)
driver.quit()






