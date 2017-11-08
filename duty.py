# -*- coding: UTF-8 -*-

import codecs
import emsender
import datetime
#任务:包含提醒内容以及负责人邮件地址

info_file = 'usr_info.txt'

class Cduty:
	def __init__(self,type,content,resp_email,start_day,start_id = 0):
		self.tp = type	
		self.st_day = start_day
		self.content = content
		self.addr = resp_email
		self.cur_id = start_id
		
		with codecs.open(info_file,'r','utf-8')as fin:
			self.usr = fin.readline().strip('\r\n')
			self.pswd = fin.readline().strip('\r\n')
		
	
#'admin@opencas.org','63CVlIkWhwU9'	
	def send(self):
		sender = emsender.Cemail_sender(self.usr,self.pswd,'smtp.163.com')
		#如果服务器安装了sendmail（邮件传输代理程序）就可以去除第三个参数 不然只能使用163邮箱
		sender.add_text(self.content)
		sender.sendto('自习室通知',self.addr[self.cur_id])
		self.cur_id = self.cur_id + 1
		if self.cur_id >= len(self.addr):
			self.cur_id = 0;
		
	#根据时间判断当前是否应该发送
	def judge(self,ct_day,week_time,day_time):
		#判断天数是否变化（以天数变化作为驱动,即每个任务每日最多发一封,如果要频繁发的话可以改成小时、分钟）
		
		#print day_time
		
		d = datetime.datetime.now()
		if ct_day == self.st_day:
			return False
		
		if week_time[self.tp][d.weekday()] == True and day_time[self.tp] == [d.hour,d.minute]:
			self.st_day = ct_day#本日不再发送
			return True
		else:
			return False
		
		
		
		
		
		
		