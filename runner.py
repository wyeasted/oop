#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import os
import sys
import HTMLTestRunner

os.path.abspath()

reload(sys)
sys.setdefaultencoding('utf-8')


def testsuite():
	suite=unittest.defaultTestLoader.discover(
		start_dir=os.path.dirname(__file__),
		pattern='test*.py',
		top_level_dir=None
	)
	return suite

if __name__ == '__main__':
    test=file(os.path.join(os.path.dirname(__file__),'report.html'),'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
		stream=test,
	    title=u'自动化测试报告',
	    description=u'自动化测试报告具体信息'
    )
    runner.run(testsuite())