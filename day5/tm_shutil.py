#!/usr/bin/env python 
# -*- coding:utf-8 -*-

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
