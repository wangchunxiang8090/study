#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()
foo()