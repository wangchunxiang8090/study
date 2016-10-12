#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time
import datetime
print(datetime.date.today())    #返回当前日期
print(datetime.datetime.now())  #打印当前时刻
print(datetime.datetime.now().timetuple())  #返回当前时刻的元组形式
print(datetime.date.today().replace(2014,9,12))  #替换时间
print(datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"))  #将字符串转换成日期格式
print(datetime.date.fromtimestamp(time.time())) #时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
