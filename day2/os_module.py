#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os

# os模块和操作系统交互
# 执行命令，不保存结果
cmd_result = os.system("dir")
print("--->",cmd_result)

if not cmd_result:
   print("False")

# 保存结果到临时空间，通过read方法读取结果
cmd_result = os.popen("ipconfig").read()
print(cmd_result)

# 在当前目录下创建一个文件夹
#os.mkdir("new_dir")