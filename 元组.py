# --coding:utf-8--
# Ԫ��DSUģʽ:װ�Ρ����򡢷�װ��

words = ['abcd','ab','defghi']

lst = []

for word in words:
	lst.append((len(word),word))
	
lst.sort(reverse = True)

# ��Ԫ�����װ��
sort_words = []

for e in lst:
	length,word = e
	sort_words.append(word)
	
print sort_words

# ʹ�������������м�
# words.sort(key = lambda x : len(x),reverse = True)