#!/usr/bin/env python
#-*-coding:utf-8-*_
"""id属性的定位"""
from selenium import webdriver
import time as t
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""name属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_name('wd').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""class_name属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_class_name('s_ipt').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""tag name属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
tag=driver.find_elements_by_tag_name('input')
tag[7].send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""xpath属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""css selector属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#kw').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""link_text属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_link_text('地图').click()
t.sleep(5)
driver.quit()

"""partial_link_text属性的定位"""
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_partial_link_text(u'频').click()
t.sleep(5)
driver.quit()

