#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
print(sys.argv)
print(sys.version)
print(sys.platform)
print(sys.stdout.write("ffff"))

import urllib2
import json

x = urllib2.urlopen('http://api.zfwx.com/v3/auth/login.json?j_password=11111111&appid=e30d6495ef264cac94fd5b29911ed83f&j_username=ceshi001&choose_domain=0&deviceinfo=Phone_OSX&version=4.19&channelId=4523442464381775171%20HTTP/1.1%22%20200%20480%20%22-%22%20%22-%22%20%22-%22', timeout=3)
res = json.loads(x.read())
for i in res:
    print(i,res[i])


import os
import shutil
src = open('tm.py','r',encoding="utf-8")
dst = open('tm_copy.py','w',)
dst = open('tm_file.py','w',)
dst = open('tm_file.py','w',)
shutil.copyfileobj(src,dst)
shutil.copyfileobj(src,dst)
shutil.copy(src,dst)
shutil.copy2(src,dst)
shutil.copytree(os.curdir,'copytree.bak')
shutil.rmtree('copytree.bak')
shutil.move()
shutil.make_archive('www','gztar',root_dir=r"C:\Users\djn1\Desktop\MG_HTML")
