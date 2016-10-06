#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time
user,passwd="alex",'abc123'
def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username: ".strip())
        password = input("Password: ".strip())
        if user == username and passwd == password:
            print("登录成功")
            res = func(*args,**kwargs)
            return res
        else:
            exit("验证失败")
    return wrapper

#@auth
def index():
    print('welcome to index page')
@auth
def home():
    print('welcome to home page')
    return "from home"
@auth
def bbs():
    print('welcome to bbs page')

print(home())