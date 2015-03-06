# -- coding:utf-8--
# ÀûÓÃ×Öµä¼ÆËã
count = {}

for i in 'abcdab':
	if i in count:
		count[i] += 1
	else:
		count[i] = 1

print count
	