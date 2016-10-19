
# print( all([1,-5,3]) )
# print( any([]) )
# a= ascii([1,2,"开外挂开外挂"])
# print(type(a),[a])
# a = bytes("abcde",encoding="utf-8")
# b = bytearray("abcde",encoding="utf-8")
# print( b[1] )
# b[1]= 50
# print(b)


#print(a.capitalize(),a)
# def sayhi():pass
# print( callable(sayhi) )

code = '''
def fib(max): #10
    n, a, b = 0, 0, 1
    while n < max: #n<10
        #print(b)
        yield b
        a, b = b, a + b
        #a = b     a =1, b=2, a=b , a=2,
        # b = a +b b = 2+2 = 4
        n = n + 1
    return '---done---'

#f= fib(10)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''

#py_obj = compile(code,"err.log","exec")
#exec(py_obj)

#exec(code)


# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)
#
# #(lambda n:print(n))(5)
# calc = lambda n:3 if n<4 else n
# print(calc(2))

#res = filter(lambda n:n>5,range(10))
# res = map(lambda n:n*2,range(10))
# res = [ lambda i:i*2 for i in range(10)]
# import functools
# res = functools.reduce( lambda x,y:x*y,range(1,10 ))
# print(res )

# a = frozenset([1,4,333,212,33,33,12,4])
# #print(globals())
#
# def test():
#     local_var =333
#     print(locals())
#     print(globals())
# test()
# print(globals())
# print(globals().get('local_var'))
#
#
# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
#
# #print(  sorted(a.items()) )
# print(  sorted(a.items(),key=lambda x:x[1]) )
# print(a )
#
# a = [1,2,3,4,5,6]
# b = ['a','b','c','d']
#
# for i in zip(a,b):
#     print(i)

#import 'decorator'
# __import__('decorator')

# a = frozenset(set(range(10)))
# print(hash('s'))



# print(abs(-9))

# def fun():
#     print('func')

# apply(fun)
# print(bin(255))
# print(bool(01))
# print(callable(fun))
# print(chr(100))
# s = "for i in range(10):print i"
# exec(s)
# print(cmp(3,4))
# print(cmp(3,3))
# print(cmp(5,3))
# print(dict(f='2'))
# s = 'str'
# print(dir(s))
# print(divmod(3,3))
# li = [u'手表',u'汽车',u'房']
# for i in enumerate(li):
#     print(i)
# result = eval('1*3')
# print(result)
# s = '''
# for i in enumerate(range(1,10,3)):
#     print(i)
# '''
# exec(s)
# li = [11,22,33]
# def foo(arg):
#     if arg >22:
#         return False
#     else:
#         return True
# temp = filter(foo,li)
# print(temp)
# print(float(10))
# s = 'i am {0},{1}'
# print(s.format('alex','xxx'))
# a = frozenset(set(range(10)))
# print(a)
# print('__name__' in globals())\
# print(hash('s'))
# import os
# print(hasattr(os,path))
# import re
# print(help(re.sub))
# print(hex(23))
# s = 1
# f = s
# print(id(s),id(f))
# inp = input("input >>> ")
# print(inp)
# class f(object):
#     pass
# x = f()
# print(isinstance(x,f))
# s = 'fafafa'
# for i in iter(s):
#     print(i)
# import hashlib
# s = "os"
# __import__(s)
# s = "str"
# print(len(s))
# print('gaga' in locals())
# print(max(range(22)))
# print(min(range(22)))
# print(sum(range(22)))
# next()
# print(oct(223))
# print(open('xxx'))
# print(ord('A'))
# print(pow(2,10))
# print('f')
# print(range(10))
# x = range(10)
# print(type(x))
# print(xrange(10))
# s = {'k1':'v1'}
# f = repr(s)
# print(f,type(f))
# x = range(10)
# print(reversed(x))
# print(round(1.8))
# print(reduce(lambda x,y:x+y,[1,2,3]))
# import os
# reload(os)
# x = [1122222,222222,33]
# print(sorted(x))
# print(set('x'))'
# print(type(list()))
# print(tuple([1,2,3]))
# s = "str"
# print(vars(s))
# x = [1,2,3]
# y = [4,5,6]
# z = [4,5,6]
# print(zip(x,y,z))