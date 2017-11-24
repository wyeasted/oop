#!/usr/bin/env python
#-*-coding:utf-8-*-

class F1(object):
	def __init__(self,tenant,user,host,storage):
		self.tenant=tenant
		self.user=user
		self.host=host
		self.storage=storage
	def getTenant(self):
		return self.tenant
	def SetTenant(self,tenant):
		self.tenant=tenant
	def getUser(self):
		return self.user
	def SetUser(self,user):
		self.user = user
	def getHost(self):
		return self.host
	def SetHost(self,host):
		self.host=host
	def getStorage(self):
		return self.storage
	def SetStorage(self,storage):
		self.storage=storage
	def info(self):
		print '项目 is {0},用户 is {1},主机 is {2}, 存储 is {3}'.\
			format(self.getTenant(),self.getUser(),self.getHost(),self.getStorage())
f=F1('group1','王怡','host1','lvm')
f.info()
f.SetTenant('group2')
f.SetUser('张三')
f.SetHost('host2')
f.SetStorage('evs')
f.info()

class Vdisk(F1):
	def __init__(self,tenant,user,host,storage,name,size):
		F1.__init__(self,tenant,user,host,storage)
		self.name1=name
		self.size=size
	def info(self):
		print '云硬盘的项目 is {0},用户 is {1},主机 is {2}, 存储 is {3},名称是：{4}，大小是：{5}'.\
			format(self.getTenant(),self.getUser(),self.getHost(),self.getStorage(),self.name1,self.size)
f1=Vdisk('group1','王怡','host1','lvm','vdisk1','20GB')
f1.info()

class VM(F1):
	def __init__(self,tenant,user,host,storage,name,image,image_size,CPU,memory,network):
		F1.__init__(self,tenant,user,host,storage)
		self.name2=name
		self.image=image
		self.image_size=image_size
		self.CPU=CPU
		self.memory=memory
		self.network=network

	def info(self):
		print '云主机的项目 is {0},用户 is {1},主机 is {2}, 存储 is {3},名称是：{4}，镜像是：{5},镜像大小是：{6},' \
		      'CPU是：{7},内存是：{8}，网路是：{9}'.format(self.getTenant(),self.getUser(),self.getHost(),self.getStorage(),
		                                        self.name2,self.image,self.image_size,self.CPU,self.memory,self.network)
f2=VM('group1','王怡','host1','lvm','VM1','centos7.1',11,'1核','2GB','network1')
f2.info()

