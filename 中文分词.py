"""
算法：正向最大匹配
从左到右取尽可能大的词

def fmm_word_seg(sentence,word_dic,max_length):
	begin = 0 
	words = []
	sentence = unicode(sentence,'utf-8')
	
	while begin < len(sentence):
		for end in range(min(beg + max_len,len(sent)),beg,-1):
			words.append(word)
			break
		begin = end
	return words
	
max_len,word_dic = load_dic('lexicon.dic')
words = fmm_word_seg(raw_input(),word_dic,max_len)
for word in words:
	print word
"""