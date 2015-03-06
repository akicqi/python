# -- coding:utf-8--

f = open("1.txt")

count = {}

for line in f:
    line = line.strip() # ȥ��ÿһ��ĩβ�س���
    words = line.split() # �Ծ��Ӱ��ո�����и�
    for word in words: # ���б���
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

word_freq = []

for word,freq in count.items(): # ��count���б������ÿһ�����ʼ����Ӧ��Ƶ��
# item()�������ֵ���ÿ��key��value���һ��Ԫ�飬������ЩԪ������б��з��ء�
# �����ʹ��for..in��ֻ��ȡ��ÿһ��Ԫ�ص�keyֵ
    word_freq.append((freq,word))

word_freq.sort(reverse = True)# ��������

for freq,word in word_freq[:10]: # ��ӡǰʮ��
    print word,freq