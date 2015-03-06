# -- coding:utf-8 --
"""
created:2025.02.25
author:akic
"""
# 使用循环的方法判断
def is_palindrome(string):
	low = 0
	up = len(string) - 1
	while(low < up):
		if string[low] != string[up]:
			return False
		else:
			low += 1
			up -= 1
	return True

# 递归实现

def is_palidrome_2(string):
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False
	else:
		return is_palidrome_2(string[1:-1])


f = open('name.txt')

for line in f:
	name = line.strip()
	if is_palindrome(name):
		print name

f.close()
	