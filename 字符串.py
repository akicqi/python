# -- coding:utf-8 --
"""
Created : 2015.02.25
@author:


"""

def vowels_count(string):
	count = 0
	for c in string: # 使用in判断一个字符串是不是另一个字符串的子串
		if c in 'aeiouAEIOU':
			count += 1
	return count
	
s = "abcdfoi"

print vowels_count(s)
			