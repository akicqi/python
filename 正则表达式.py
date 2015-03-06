# -- coding:utf-8 --
# 判断一个人名name是否满足一下模式：
# Michael: name == 'Michael'
# 以Mi开始：name[:2] == 'Mi'
# 包含cha子串：'cha' in name

import re

f = open("name.txt")

pattern = 'a.'

for line in f:
	name = line.strip()
	result = re.search(pattern,name) # 使用正则表达式的search方法
	if result:
		print name

f.close()