#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 函数
def func1():
    """
    testing1
    :return: x
    """
    print('in the func1')
    return 0

# 过程(没有返回值的函数)
def func2():
    """testing2"""
    print('in the func2')

x=func1()
y=func2()

print('from func1 return is %s' %x)
print('from func2 return is %s' %y)