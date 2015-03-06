# --coding:utf-8 --
"""ÅúÁ¿²âÊÔÍøÕ¾±àÂë"""
import urllib
import chardet

def automatic_detect(url):
	"""ÅúÁ¿²âÊÔÍøÕ¾±àÂë"""
	content = urllib.urlopen(url).read()
	result = chardet.detect(content)
	encoding = result['encoding']
	return encoding

url = [
	"http://www.1688.com/",
	"http://www.jd.com",
	"http://www.163.com",
	"http://open.cd",
	"http://www.z.cn",
	"http://www.dangdang.com"

]

for urls in url:
	print urls,automatic_detect(urls)