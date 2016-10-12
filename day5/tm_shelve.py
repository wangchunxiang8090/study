#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import shelve
d = shelve.open("shelve_test")
meme = [1,2,2,3,3,4,5]
d["test"] = meme
print(d.get())