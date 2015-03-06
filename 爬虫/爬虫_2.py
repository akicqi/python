# --coding:utf-8--
import urllib

def callback(a,b,c):
	"""
	写函数以及类最好在里面写上注释
	@a:是什么
	"""
	down_progress = 100.0*a*b/c
	if down_progress > 100:
		down_progress = 100
	print "%.2f%%"% down_progress,
	
	
url = "http://www.baidu.com/"
local = "C:\\Users\\DELL\\Desktop\\baidu.html"

urllib.urlretrieve(url,local,callback)