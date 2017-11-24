#!/usr/bin/env python
#-*-coding:utf-8-*_
from selenium import webdriver
import time

values=['selenium','webdriver','haha']

for serch in values:
	driver=webdriver.Firefox()
	driver.maximize_window()
	driver.get('http://www.baidu.com')
	driver.find_element_by_id('kw').send_keys(serch)
	time.sleep(3)