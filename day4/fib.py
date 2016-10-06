#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

#fib(100)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         #print(b)
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# for i in fib(10):
#     print(i)

# f = fib(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(10)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value：',e.value)
        break