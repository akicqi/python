# -- coding:utf-8--

f = open("1.txt")

count = {}

for line in f:
    line = line.strip() # 去掉每一段末尾回车符
    words = line.split() # 对句子按空格进行切割
    for word in words: # 进行遍历
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

word_freq = []

for word,freq in count.items(): # 对count进行遍历获得每一个单词及其对应的频率
# item()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
# 如果纯使用for..in则只能取得每一对元素的key值
    word_freq.append((freq,word))

word_freq.sort(reverse = True)# 进行排序

for freq,word in word_freq[:10]: # 打印前十个
    print word,freq