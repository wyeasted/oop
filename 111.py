#!/usr/bin/env python
# -*-coding:utf-8-*-

import os

with open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'r') as f:
	print (''.join(f.readlines())).split('\n')[0],type(''.join(f.readlines()))

	#1.我们获取的文件里面的内容首先全是列表
	#2.我们把列表转化为字符串
	#3.从字符串中分离出换行,用回车来分隔字符串
	#4.从换行中取到第一个或者第二个内容

with open(os.path.join(os.path.dirname(__file__), 'sequence.txt'), 'r') as f:
	print (''.join(f.readlines())).split('\n')[0],type(''.join(f.readlines()))