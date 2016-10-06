#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time

def deco(func):
    def inner(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time %s" %(stop_time-start_time))
    return inner

@deco   #test1 = deco(test1)
def test1():
    time.sleep(1)
    print('in the test1')

@deco
def test2(name):
    print('test2',name)

# test1 = deco(test1)
test1()
test2('args')
