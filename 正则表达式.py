# -- coding:utf-8 --
# �ж�һ������name�Ƿ�����һ��ģʽ��
# Michael: name == 'Michael'
# ��Mi��ʼ��name[:2] == 'Mi'
# ����cha�Ӵ���'cha' in name

import re

f = open("name.txt")

pattern = 'a.'

for line in f:
	name = line.strip()
	result = re.search(pattern,name) # ʹ��������ʽ��search����
	if result:
		print name

f.close()