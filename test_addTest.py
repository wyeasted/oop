#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import time as t
import os

'''数据与代码分离'''
class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('http://www.baidu.com')
        cls.driver.implicitly_wait(30)

    def test_001(self):
        '''验证title是否正确'''
        self.assertTrue(self.driver.title,self.readLog()[0])

    def test_002(self):
        '''验证URL是否正确'''
        self.assertEqual(self.driver.current_url,self.readLog()[1])

    def test_003(self):
        '''登录：用户名为空点击登陆后的错误提示信息'''

        self.driver.find_element_by_link_text(u'登录').click()
    # 什么都没输入
        self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
        div = self.driver.find_element_by_id('TANGRAM__PSP_10__error').text
        self.assertEqual(div.encode('utf-8'), self.readLog()[2])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    #def suite():
    #   suite = unittest.TestSuite()
    #   suite.addTest(BaiduTest('test_001'))
    #   suite.addTest(BaiduTest('test_002'))
    #    return suite
    def suite():
        lists=['test001','test002','test003']
        suite=unittest.TestSuite()
        for item in lists:
            suite.addTest(BaiduTest(item))

    #def readLog0(self):
        #f = open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'r')
        #return ''.join(f.readlines()).split('\n')[0]
    #def readLog1(self):
        #f = open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'r')
        #return ''.join(f.readlines()).split('\n')[1]
    #def readLog3(self):
        #f = open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'r')
        #return ''.join(f.readlines()).split('\n')[2]
    def readLog(self):
        lists=[]
        with open(os.path.join(os.path.dirname(__file__),'log.txt'),'r') as f:
            for item in (''.join(f.readlines())).split('\n'):
                lists.append(item)
        return lists
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite)