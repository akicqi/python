# -- coding:utf-8 --
def revert_dict(d):
	reverse = {}
	for k,v in d.items():
		if v in reverse:
			reverse[v].append(k) # ���ԭ�е�valueֵ�ظ����������غ�
		else:
			reverse[v] = [k]
	return reverse

d = {'A':28,'B':30,'C':28}

r = revert_dict(d)

print r 