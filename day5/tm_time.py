#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time
time_stamp=time.time()      #获取时间戳
time_tuple =time.localtime(time_stamp)   #件时间戳转换为元组形式
time_str = time.strftime("%Y-%m-%d",time.localtime(time_stamp)) #将元组形式转换为字符串形式
print(time_stamp)
print(time_tuple)
print(time_str)

time_fromat ="2016-10-09"
tm_tuple = time.strptime(time_fromat,'%Y-%m-%d')    #将字符串转换成对应的元组
tm_stamp = time.mktime(tm_tuple)    #将元组装换为时间戳形式
print(tm_tuple)
print(tm_stamp)

print(time.asctime(time.localtime()))
print(time.ctime(time.time()))