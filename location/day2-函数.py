#!/usr/bin/env python
#-*-coding:utf-8-*_

def login(username='admin',password='admin'):
    if username=='admin' and password=='admin':
        print u'登陆成功'
    else:
        print 'sorry'

login()

def add(a=2,b):
    return a+b
print(add(5,5))