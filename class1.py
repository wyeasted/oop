#!/usr/bin/env python
#-*-coding:utf-8-*-

class F1_sys(object):
	def __init__(self,name,displayname,mark):
		self.name=name
		self.displayname=displayname
		self.marked=mark
	def adduser(self):
		print '系统管理员的姓名是：{0},姓名是：{1}，备注是：{2}'.format(self.name,self.displayname,self.marked)
class F2_sec(object):
	def __init__(self,name,displayname,mark):
		self.name=name
		self.displayname=displayname
		self.marked=mark
	def adduser(self):
		print '安全管理员的姓名是：{0},姓名是：{1}，备注是：{2}'.format(self.name,self.displayname,self.marked)
class Cluster(F1_sys,F2_sec):
	def __init__(self,name,displayname,mark):
		super(Cluster,self).__init__(name,displayname,mark)
	def adduser(self):
		print '审计管理员的姓名是：{0},姓名是：{1}，备注是：{2},审核有审计日志功能'.format(self.name,self.displayname,self.marked)

st=Cluster('audit','测试数据','2017-10-16建立')
st.adduser()

