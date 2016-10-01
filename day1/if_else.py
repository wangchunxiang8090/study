#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# getpass 模块在pycharm中不能使用,别的地方可以使用
import getpass

_username = 'alex'
_password = 'abc123'

username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")

# 流程了控制
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("invalid username or password")
print("over")