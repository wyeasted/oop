#!/usr/bin/env python
#-*-coding:utf-8-*_
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
import time as t
"""id属性的定位"""

def findID(driver, id):
    return driver.find_element_by_id(id)


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findID(driver, 'kw').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""name属性的定位"""

def findName(driver,name):
    return driver.find_element_by_name(name)

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findName(driver,'wd').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""class_name属性的定位"""
def findClassName(driver,name):
    return driver.find_element_by_class_name(name)

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findClassName(driver,'s_ipt').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""tag name属性的定位"""
def findTagName(driver,name):
    return driver.find_elements_by_tag_name(name)

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
tag=findTagName(driver,'input')
tag[7].send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""xpath属性的定位"""
def findXpath(driver,xpath):
    return driver.find_element_by_xpath(xpath)

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findXpath(driver,'//*[@id="kw"]').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""css selector属性的定位"""
def findCss(driver,css):
    return driver.find_element_by_css_selector(css)

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findCss(driver,'#kw').send_keys(u'王怡')
t.sleep(5)
driver.quit()

"""link_text属性的定位"""

def findlink_text(driver,link_text):
    return driver.find_element_by_link_text(link_text)
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findlink_text(driver,u'地图').click()
t.sleep(5)
driver.quit()

"""partial_link_text属性的定位"""

def findPlink_text(driver,plink_text):
    return driver.find_element_by_partial_link_text(plink_text)
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
findPlink_text(driver,u'频').click()
t.sleep(5)
driver.quit()


