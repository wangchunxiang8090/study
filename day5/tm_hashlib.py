#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import hashlib
m = hashlib.md5()
m.update("wcx")
print(m.hexdigest())

import hmac
h = hmac.new('wueiqi')
h.update('hellowo')
print h.hexdigest()
