# ���һԪ���η���
# ���룺a,b,c����ϵ��
# ��������̵ĸ�
# �㷨�������ʽ
import math # ���뺯��ģ��
while True:
	# ѭ���忪ʼ
	a,b,c = eval(raw_input("��������������"))
	if a == 0:
		print "����ΪһԪһ�η���"
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
	# ѭ�������
	ch = raw_input("Please input \'c\' to end or any keys to continue\n")
	if ch!='c' and ch!='C':
		pass
	else:
		break
print "=== end ==="
	