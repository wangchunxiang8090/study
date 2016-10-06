#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# def bar():
#     print('in the bar')
#
# def test1(func):
#     print(func)
#     func()
#
# test1(bar)
# func = bar
# func()


def bar():
    print('in the bar')

def test2(func):
    print(func)
    return func

# print(test2(bar))

# t = test2(bar)
# t()

bar = test2(bar)
bar()