# --coding:utf-8--
import urllib

def callback(a,b,c):
	"""
	д�����Լ������������д��ע��
	@a:��ʲô
	"""
	down_progress = 100.0*a*b/c
	if down_progress > 100:
		down_progress = 100
	print "%.2f%%"% down_progress,
	
	
url = "http://www.baidu.com/"
local = "C:\\Users\\DELL\\Desktop\\baidu.html"

urllib.urlretrieve(url,local,callback)