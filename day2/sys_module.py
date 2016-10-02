#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys

# python2.X 会出错，当前路径下存在sys模块,而不是使用python自带的sys
# 打印python环境变量
print(sys.path)

for i in sys.path:
    print(i,)

# 打印相对路径, 打印参数
print(sys.argv)
print(sys.argv[2])