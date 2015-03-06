# 求解一元二次方程
# 输入：a,b,c三个系数
# 输出：方程的根
# 算法：求根公式
import math # 导入函数模块
while True:
	# 循环体开始
	a,b,c = eval(raw_input("请输入三个参数"))
	if a == 0:
		print "方程为一元一次方程"
	else:
		delta = b * b - 4 * a * c
		print 'delta = ',delta
		if delta < 0:
			print "Without real roots"
		elif delat == 0:
			print "Only one root is",(-b/2,0/a)
		else:
			discRoot = math.sqrt(delta)
			r1 = (-b + discRoot) / (2 * a)
			r2 = (-b - discRoot) / (2 * a)
			print "Two discinct roots are:",r1,r2
	# 循环体结束
	ch = raw_input("Please input \'c\' to end or any keys to continue\n")
	if ch!='c' and ch!='C':
		pass
	else:
		break
print "=== end ==="
	