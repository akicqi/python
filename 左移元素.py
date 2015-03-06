# -- coding:utf-8 --

def shif_left(lst):
	tmp = lst[0]
	for i in range(len(lst) - 1):
		lst[i] = lst[i + 1]
	lst[-1] = tmp
	
x = [10,20,30]
shif_left(x)
print x