#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import sys
import time
for i in range(100):
    sys.stdout.write("#")
    sys.stdout.flush()  #直接刷新，不等缓冲
    time.sleep(0.1)