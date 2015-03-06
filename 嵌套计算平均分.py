# -- coding:utf-8 --
students = [['li',98],['liu',45],['zhang',100],['zao',95]]
"""
s = 0.0
for student in students:
    s += student[1]

print s / len(students)
"""
"""    
# 利用列表推导求

print float(sum([student[1] for student in students])) / len(students)

"""

"""
# 对列表进行排列


def f(lst):
    return lst[1]
    
students.sort(key = f ,reverse = True)

print students 
"""

# 使用匿名函数

students.sort(key = lambda x:x[1] ,reverse = True)
print students 