#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import time as t
import os
from object import *

class BaiduTest(unittest.TestCase,Baidu):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get(BaiduTest.readLog()[0])


    def test_001(self):
        '''验证title是否正确'''
        self.assertTrue(self.driver.title,BaiduTest.readLog()[1])

    def test_002(self):
        '''验证URL是否正确'''
        self.assertEqual(self.driver.current_url,BaiduTest.readLog()[2])

    def test_003(self):
        '''登录：密码为空点击登陆后的错误提示信息'''
        self.login()
        self.username(BaiduTest.readLog()[3])
        self.loginbutton()
        assert=self.assert1()
        self.assertEqual(assert.encode('utf-8'), BaiduTest.readLog()[5])

    def test_004(self):

        '''登录：密码为空点击登陆后的错误提示信息'''
        self.login()
        self.username(BaiduTest.readLog()[3])
        self.loginbutton()
        assert=self.assert1()
        self.assertEqual(
        assert.encode('utf-8'), BaiduTest.readLog()[5])


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def suite(self):
        lists1=[]
        suite = unittest.TestSuite()
        with open(os.path.join(os.path.dirname(__file__),'sequence.txt'),'r') as t:
            for item in (''.join(t.readlines())).split('\n'):
                list1.append(item)
        return lists1

    @staticmethod
    def readLog(self):
        lists2=[]
        with open(os.path.join(os.path.dirname(__file__),'log.txt'),'r') as f:
            for item in (''.join(f.readlines())).split('\n'):
                lists2.append(item)
        return lists2
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite)