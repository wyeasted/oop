#!/usr/bin/env python
# -*-coding:utf-8-*-

class Test(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print 'Error details :%s' %(e.args[0])

	def findElements(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			print 'Error details :%s' %(e.args[0])

class Baidu(Test):
	from selenium.webdriver.common.by import By
	login=(By.LINK_TEXT,u'登陆')
	username=(By.ID,'TANGRAM__PSP_10__userName')
	password=(By.ID,'TANGRAM__PSP_10__password')
	login_button=(By.ID,'TANGRAM__PSP_10__submit')
	assert1=(By.ID,'TANGRAM__PSP_10__error')

	def login(self):
		self.findElement(*self.login).click()

	def username(self,username):
		self.findElement(*self.username).send_key('username')

	def password(self,password):
		self.findElement(*self.password).send_key('password')

	def loginbutton(self):
		self.findElement(*self.login_button).click()

	def assert1(self):
		self.findElement(*self.assert1).text