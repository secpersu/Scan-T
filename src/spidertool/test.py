#!/usr/bin/python
import Queue
def aa():
	print 'already in port'
class bb:
	def __init__(self):
		self.yy=0
		self.qq=Queue.Queue()
		self.qq.put((self.aa,1))
		self.yy=1
		print 'alread user port'
	def aa(self):
		return self.yy
	def cc(self):
		u,k=self.qq.get()
		print u()
		print k
def asd():
	return 1,2
for l in range(0,6):
	print l