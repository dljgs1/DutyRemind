# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.header import Header
from email import encoders
import mimetypes

class Cemail_sender(object):
	def __init__(self,usrname,password,server = 'localhost'):
		self.usrname = usrname
		self.password = password
		self.sever = server
		self.content = ''
		self.msg = MIMEMultipart()
		self.file_list = []
		
		
	def add_text(self,str):
		self.content = self.content + str
		
	def add_file(self,fname):
	
		mimetype,mimeencoding = mimetypes.guess_type(fname)
		if mimeencoding or (mimetype is None):
			mimetype = "application/octet-stream"
		maintype,subtype = mimetype.split("/")
		
		with open(fname,'rb') as fin:
			mime = None
			if mimetype == 'text':
				mime = MIMEText(fin.read(),_subtype = subtype)
			else:
				mime = MIMEBase(maintype,subtype)
				mime.set_payload(fin.read())
				encoders.encode_base64(mime)
			mime.add_header('Content-Disposition','attachment',filename=fname)
			scount = str(len(self.file_list))
			mime.add_header('Content-ID', '<'+scount+'>')
			mime.add_header('X-Attachment-Id', scount)
			
			self.file_list.append(mime)
			
	def sendto(self,subject,dst_addr):
		self.msg['Subject'] = Header(subject, 'utf-8')
		print Header(subject, 'utf-8')
		self.msg['From'] = 'dljgs<%s>'%self.usrname
		print 'dljgs<%s>'%self.usrname
		self.msg['To'] = dst_addr
		print dst_addr
		
		self.msg.attach(MIMEText(self.content,'plain','utf-8'))
		for item in self.file_list:
			self.msg.attach(item)
			
		
		
		smtp = smtplib.SMTP()
		smtp.connect(self.sever)
		smtp.login(self.usrname, self.password)
		smtp.sendmail(self.usrname, dst_addr, self.msg.as_string())
		smtp.quit()
		


