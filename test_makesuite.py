#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import time as t


class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('http://www.baidu.com')
        cls.driver.implicitly_wait(30)

    def test_003(self):
        '''验证输入框输入内容是否正确'''
        t.sleep(5)
        self.driver.find_element_by_id('kw').send_keys('webdriver')
        self.assertEqual('webdriver', self.driver.find_element_by_id('kw').get_attribute('value'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def suite():
	    suite=unittest.makeSuite(BaiduTest)
	    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite)