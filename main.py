# -*- coding: UTF-8 -*-
 
import codecs
import duty
import time
import datetime 

emails_file = 'emails.conf'
inform_file = 'list.conf'
type_file = 'timetype.conf'
init_file = 'init.conf'

def get_file_content(fname):
	buf = ""
	with codecs.open(fname,'r','utf-8')as fin:
		for line in fin.readlines():
			buf+=line
	return buf

def str2int(str):
	try:
		n = int(str)
		return n
	except ValueError:
		return str

def zo2bool(zo):
	if zo == 0:
		return False
	else:
		return True
	
	
receivers = []  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

with codecs.open(emails_file,'r','utf-8')as fin:
	for line in fin.readlines():
		line = line.strip('\r\n')
		receivers.append(line)
#print receivers
#任务槽
duties = []
init_id = []
#开始日期（从这一天的第二天开始运行）初始化为-1，即首次满足时间条件的均立刻发送：
start_day = -1

with codecs.open(init_file,'r','utf-8')as fin:
	for line in fin.readlines():
		line = line.strip('\r\n')
		init_id.append(str2int(line))
		
		
with codecs.open(inform_file,'r','utf-8')as fin:
	ct = 0
	for line in fin.readlines():
		line = line.strip('\r\n')
		s = line.split('\t')
		tp = s[0]
		ems = []
		
		content = get_file_content(s[-1])
		
		for id in s[1:-1]:#for each partners
			ems.append(receivers[str2int(id)])
		
		temp = duty.Cduty(tp,content,ems,start_day,init_id[ct])
		duties.append(temp)
		ct = ct + 1
		

		
#每个时间类型的发送时间(周次、天次)
day_time = {}	
week_time = {}

with codecs.open(type_file,'r','utf-8')as fin:
	for line in fin.readlines():
		line = line.strip('\r\n')
		s = line.split('\t')
		tp = s[0]
		
		s = map(str2int,s)
		day_time[tp] = s[1:3]#X小时X分
		
		s = map(zo2bool,s)
		week_time[tp] = s[3:]#星期X
		
		
while True:
	d = datetime.datetime.now()
	for it in duties:
		if it.judge(d.day,week_time,day_time):#一旦判断成功 st变量修改
			n = it.cur_id
			it.send()
			print u'发送了一封去往%d号的邮件'%n
	print d	
	time.sleep(40)#挂起40s
	

	
	
	
	
	
				