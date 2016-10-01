#!/usr/bin/env python
# encoding: utf-8

# 变量名 = 变量值(该值是字符串类型)
name = "Arvin"
# name2 指向name的值
name2 = name

# print可以连接多个参数,","逗号打印出来表示空格
print("My name is ",name,name2)

# Python解释器是逐行解释的,
name = "PaoChe Ge"
print(name,name2)

# 同时赋值多个变量,值和变量值的个数和变量名的个数必须一一对应
s = "key,value"
key,value = s.split(',')
print(key,value)

# 复杂变量名，驼峰写法
gf_of_oldboy = "Chen rong hua"
GFOFoldboy = "Chen rong hua"
print(gf_of_oldboy,GFOFoldboy)

# 不推荐
姓名="wcx"
print(姓名)