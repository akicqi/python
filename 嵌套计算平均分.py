# -- coding:utf-8 --
students = [['li',98],['liu',45],['zhang',100],['zao',95]]
"""
s = 0.0
for student in students:
    s += student[1]

print s / len(students)
"""
"""    
# �����б��Ƶ���

print float(sum([student[1] for student in students])) / len(students)

"""

"""
# ���б��������


def f(lst):
    return lst[1]
    
students.sort(key = f ,reverse = True)

print students 
"""

# ʹ����������

students.sort(key = lambda x:x[1] ,reverse = True)
print students 