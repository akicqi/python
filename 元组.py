# --coding:utf-8--
# 元组DSU模式:装饰、排序、反装饰

words = ['abcd','ab','defghi']

lst = []

for word in words:
	lst.append((len(word),word))
	
lst.sort(reverse = True)

# 对元组进行装饰
sort_words = []

for e in lst:
	length,word = e
	sort_words.append(word)
	
print sort_words

# 使用匿名函数进行简化
# words.sort(key = lambda x : len(x),reverse = True)