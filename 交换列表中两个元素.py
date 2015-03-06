# -- coding:utf-8 --
"""
def swap(a,b):
	tmp = a
	a = b
	b = tmp

x = 10 
y = 20

swap(x,y)
print x,y
# 仅仅交换形参并没有交换实参
"""

def swap(lst,a,b):
	tmp = lst[a]
	lst[a] = lst[b]
	lst[b] = tmp

x = [10,20,30]
swap(x,0,1)
print x