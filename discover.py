#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
import os

def testsuite():
	suite=unittest.defaultTestLoader.discover(
		start_dir=os.path.dirname(__file__),
		pattern='test*.py',
		top_level_dir=None
	)
	return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(testsuite())