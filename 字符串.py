# -- coding:utf-8 --
"""
Created : 2015.02.25
@author:


"""

def vowels_count(string):
	count = 0
	for c in string: # ʹ��in�ж�һ���ַ����ǲ�����һ���ַ������Ӵ�
		if c in 'aeiouAEIOU':
			count += 1
	return count
	
s = "abcdfoi"

print vowels_count(s)
			