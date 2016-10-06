#!/usr/bin/env python
# _*_ coding: utf-8 _*_


# l = [i * 2 for i in range(10)]
# print(l)

# a = []
# for i in range(10):
#     a.append(i*2)
# print(a)


# g = (i*2 for i in range(10))
# print(type(g))
# for i in g:
#     print(i)

g = (i*2 for i in range(10))
print(g.__next__())
print(g.__next__())
print(g.__next__())