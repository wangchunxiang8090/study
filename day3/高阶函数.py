#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def add(a,b,f):
    return f(a)+f(b)

res =add(3,-6,abs)
print(res)