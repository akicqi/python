# -- coding:utf-8 --

def bubble_sort(lst):
	top = len(lst) - 1
	exchange = True # ��������Ϊ��
	while exchange:
		exchange = False
		for i in range(top):
			if lst[i] > lst[i] + 1: # ʵ�ֶ������������������
				swap(lst,i,i + 1)
				exchange = True
		top -= 1

x = [23,14,15,62,50,97]
y = sorted(x)
print y
		