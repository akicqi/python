# -- coding = utf-8 --

"""
Created:2015.02.25
@Author:akic

"""

f = open('name.txt') # f叫做文件句柄

for line in f: # 赋予值于变量line中
	name = line.strip()
	print name.title() # 利用title首字母转换
	
	# print line.strip().title 方法进行串联，可以省去name变量

f.close() # 关闭打开文件
