# -- coding = utf-8 --

"""
Created:2015.02.25
@Author:akic

"""

f = open('name.txt') # f�����ļ����

for line in f: # ����ֵ�ڱ���line��
	name = line.strip()
	print name.title() # ����title����ĸת��
	
	# print line.strip().title �������д���������ʡȥname����

f.close() # �رմ��ļ�
