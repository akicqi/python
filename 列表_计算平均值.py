# -- coding:utf-8 --
# 列表：内建的数据结构用来存储一系列元素
# 读取30个数字，并计算平均数

nums = [] #创建一个空的列表

for i in range(10): # for循环30次
	num = float(raw_input())
	nums.append(num) # 将输入追加到nums上
	
s = 0 #s存储所有num的值
for num in nums:
	s += num
avg = s / len(nums)

print avg1

# print sum(nums) / len(nums),利用sum函数求平均值精简代码