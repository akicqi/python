#--coding:utf-8--
import urllib2
import random

url = "http://blog.csdn.net/happydeer"

my_headers = [
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
]

def get_content(url,headers):
	"""
	@获取403禁止访问的页面
	"""
	random_header = random.choice(headers)
	
	
	req = urllib2.Request(url)
	req.add_header("User-Agent",random_header)
	req.add_header("Host","blog.csdn.net")
	req.add_header("Referer","http://blog.csdn.net")
	req.add_header("GET",url)
	
	content = urllib2.urlopen(req).read()
	return content

print get_content(url,my_headers)
	