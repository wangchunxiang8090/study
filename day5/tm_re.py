#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#re
# import re
# origin = 'has hehe'
# r = re.match("h(\w+)", origin)
# print(r.group())
# print(r.groups())
#
# origin = 'has hehe'
# r = re.search("h(\w+)", origin)
# print(r.group())
# print(r.groups())
#
# origin = 'has hehe'
# r = re.findall("h(\w+)", origin)
# print(r)
#
# origin = 'qhas qhehe'
# r1 = re.split("h\w+", origin)
# r2 = re.split("h(\w+)", origin)
# print(r1)
# print(r2)


import re
import json

f = open("re.conf.txt",'rb')
result = f.read()
url = []
for i in result:
    temp = re.search('src="(.*)"',i)
    print(temp)