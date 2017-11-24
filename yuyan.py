#!/usr/bin/env python
# -*-coding:utf-8-*-

#  字符串转化为列表
str1='auto selenium test'
list1=str1.split(' ')
print list1,type(list1)

# 列表转化为字符串

list2=['html','java','python']
str1=' '.join(list2)
print str1,type(str1)

#unicode转化为字符串(编码）
unicode=u'王怡'
print type(unicode)
print unicode.encode('utf-8'),type(unicode.encode('utf-8'))

#字符串转化为unicode（解码）
str1='auto selenium test'
print str1.decode('utf-8'),type(str1.decode('utf-8'))
