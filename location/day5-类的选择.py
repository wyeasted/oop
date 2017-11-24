#!/usr/bin/env python
#-*-coding:utf-8-*_

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t

def findCss(driver,css):
    return driver.find_element_by_css_selector(css)

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
action=ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector('#u1 > a.pf')).perform()
findCss(driver,'#wrapper > div.bdpfmenu > a.setpref').click()

#index方式每页显示50条
select=Select(driver.find_element_by_xpath('//*[@id="nr"]'))
select.select_by_index(2)
driver.find_element_by_xpath('//*[@id="nr"]').click()
t.sleep(3)

#文本的方式每页显示20条
select.select_by_visible_text(u'每页显示20条')
driver.find_element_by_xpath('//*[@id="nr"]').click()
t.sleep(3)

#value的方式每页显示10条
select.select_by_value('10')
driver.find_element_by_xpath('//*[@id="nr"]').click()
t.sleep(3)
driver.quit()




