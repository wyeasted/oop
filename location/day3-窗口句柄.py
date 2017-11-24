#!/usr/bin/env python
#-*-coding:utf-8-*_

from selenium import webdriver
import time as t
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.baidu.com')
driver.find_element_by_css_selector('#u1 > a.lb').click()
t.sleep(3)
#获取百度当前浏览器的窗口句柄
nowHandle=driver.current_window_handle
t.sleep(3)
driver.find_element_by_link_text(u'立即注册').click()
#获取所有浏览器的窗口句柄
handles=driver.window_handles

for handle in handles:
    if handle!=nowHandle:
        driver.switch_to_window(handle)
        t.sleep(2)
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys(u'fewferrfefwfewt')
        driver.find_element_by_css_selector('#TANGRAM__PSP_3__submit').click()
    # 在输入用户名后直接点击注册，出现所有字段的断言信息
        error_text1=driver.find_element_by_css_selector('#TANGRAM__PSP_3__userNameError').text
        error_text2=driver.find_element_by_css_selector('#TANGRAM__PSP_3__phoneError').text
        error_text3=driver.find_element_by_css_selector('#TANGRAM__PSP_3__verifyCodeError').text
        error_text4=driver.find_element_by_css_selector('#TANGRAM__PSP_3__passwordError > span > span.pwd-strength-detail').text
        error_text5=driver.find_element_by_css_selector('#TANGRAM__PSP_3__isAgreeError').text
     #输入手机号后，关掉窗口
        t.sleep(3)
        driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys(u'1234567')
        t.sleep(3)
        '''用于只关闭当前窗口'''
        driver.close()
#跳转到当前的窗口句柄
driver.switch_to_window(nowHandle)
#断言用户名密码不输入时点击登陆
driver.find_element_by_css_selector('#TANGRAM__PSP_10__submit').click()
error_text=driver.find_element_by_css_selector('#TANGRAM__PSP_10__error').text
t.sleep(3)
driver.quit()
assert error_text in u'请您输入手机/邮箱/用户名'
assert error_text1 in u'用户名不能超过7个汉字或14个字符'
assert error_text2 in u'请您输入手机号'
assert error_text3 in u'请您输入验证码'
assert error_text4 in u'请输入密码'
assert error_text5 in u'请勾选“阅读并接受百度用户协议”'

