#!/usr/bin/env python
# _*_ coding: utf-8 _*_

Name = input("Name:")
Age = int(input("Age:"))    # integer
print(type(Age))
Job = input("Job:")
Salary = input("Salary:")

# 字符串拼接
info = '''
--------- info of  %s---------
Name: %s
Age: %d
Job: %s
Salary: %s

''' %(Name,Name,Age,Job,Salary)


# 字符串format类似字典
info2 = '''
--------- info of  {_Name}---------
Name: {_Name}
Age: {_Age}
Job: {_Job}
Salary: {_Salary}

'''.format(_Name=Name,
           _Age=Age,
           _Job=Job,
           _Salary=Salary)

# 字符串format方法 {number}
info3 = '''
--------- info of  {0}---------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}

'''.format(Name,Age,Job,Salary)

print(info)
print(info2)
print(info3)