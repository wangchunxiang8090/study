#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from collections import Iterable,Iterator
print(isinstance((x for x in range(5)),Iterator))


a=[1,2,3]
b = iter(a)
print(b,type(b))