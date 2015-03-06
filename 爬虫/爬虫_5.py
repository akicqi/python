# -- coding:utf-8 --
"""
下载贴吧 图片
"""
import re 
import urllib

def getContent(url):
	"""doc"""
	html = urllib.urlopen(url)
	content = html.read()
	html.close()

	return content

def getImages(info):
	"""doc
	 <img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=7dd2cae62adda3cc0be4b82831e83905/3384918ba61ea8d3cbfb277d930a304e241f586f.jpg" pic_ext="jpeg"  changedsize="true" width="560" height="371">
	"""
	regex = r'class="BDE_Image" src="(.+?\.jpg)"'

	pat = re.compile(regex)

	imagesCode = re.findall(pat,info)

	# 设置计数器
	i = 0

	for imageUrl in imagesCode:
		print imageUrl

		urllib.urlretrieve(imageUrl,'%s.jpg'%i)
		i += 1

info = getContent('http://tieba.baidu.com/p/3516265218')

print getImages(info)

"""
使用beautifulsoup:

import urllib
from bs4 import BeautifulSoup

def getContent(url):
	"""doc"""
	html = urllib.urlopen(url)
	content = html.read()
	html.close()

	return content

def getImages(info):
	"""doc"""
	soup = BeautifulSoup(info)

	allImg = soup.findAll('img',class_='BDE_Image')

	x = 1

	for img in allImg:
		imageName = '%s.jpg'%x
		urllib.urlretrieve(img['src'],imageName)

		x += 1

info = getContent('http://tieba.baidu.com/p/2772656630')
print getImages(info)
"""