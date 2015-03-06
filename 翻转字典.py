# -- coding:utf-8 --
def revert_dict(d):
	reverse = {}
	for k,v in d.items():
		if v in reverse:
			reverse[v].append(k) # 解决原有的value值重复导致数据重合
		else:
			reverse[v] = [k]
	return reverse

d = {'A':28,'B':30,'C':28}

r = revert_dict(d)

print r 