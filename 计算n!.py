# 计算n！
def p(n):
	x = 1
	for i in range(1,n + 1):
		x = x * i
	return x

def main():
	n = input("请输入一个整数")
	print n,"!的值为：",p(n)

main()

# 函数：是完成特定功能的一个语句组，通过函数名执行
输入：参数
输出：返回值
