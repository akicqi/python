# --coding:utf-8--
def search(lst,v):
	for i in range(len(lst)): # i�����洢�б���±�
		if lst[i] == v:
			return i
	return -1
	
x = [10,20,30]
i = search(x,20)
print x[i]
	