num = 1 # to count current student number
Total_num = 3 # total number of all students
count = 0 # to count passed student number

for num in range(1,4):
	grade = input("input No."+str(num)+"student's grade")
	if grade >= 60:
		count +=1
	else:
		pass
print "Passed student number is",count

# 对于确定循环次数的可以使用for循环代替