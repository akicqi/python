# -- coding:utf-8 --
# �б��ڽ������ݽṹ�����洢һϵ��Ԫ��
# ��ȡ30�����֣�������ƽ����

nums = [] #����һ���յ��б�

for i in range(10): # forѭ��30��
	num = float(raw_input())
	nums.append(num) # ������׷�ӵ�nums��
	
s = 0 #s�洢����num��ֵ
for num in nums:
	s += num
avg = s / len(nums)

print avg1

# print sum(nums) / len(nums),����sum������ƽ��ֵ�������