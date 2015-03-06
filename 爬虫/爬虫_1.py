# --coding:utf-8 --

import urllib

url = "http://www.jmpt.cn/"

#html = urllib.urlopen(url)

#print html.read().decode("gbk").encode("utf-8")
# 先转换成gbk再转换成utf-8，解决网易编码问题

#print html.info()
#获取网站头部信息

#print html.getcode()
#获取网站状态码

#print dir(html)
#查看dir对象下面的功能

#html.close()
#注意关闭，防止内存泄漏

###########################################################

#网页抓取，下载网页

urllib.urlretrieve(url,"c:\\Users\\DELL\\Desktop\\jmpt.html")