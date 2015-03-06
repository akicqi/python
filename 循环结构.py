# --coding:utf-8--

num = 1 # to count current student number
Total_num = 3 # total number of all students
count = 0 # to count passed student number

while num <= Total_num: # Loop condition
	grade = input("input No."+str(num)+"student's grade")
	if grade >= 60:
		count +=1
	else:
		pass
	num +=1 # to update iteration variable
print "Passed student number is",count

# 注意循环变量的更新

# 书写while语句的三个步骤：
循环体外设定循环可执行的初始条件

设定重复执行的条件即循环条件

书写需重复执行的代码即循环体并在循环体内更新循环条件