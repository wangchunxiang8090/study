#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# 默认打开是以操作系统的编码打开，windows默认是gbk
# python3.X 默认是utf-8，不是同一个编码所以不能识别，要指定以哪种编码打开文件
# data = open("yesterday",encoding="UTF-8").read()
# print(data)
'''
# 文件句柄(文件的内存对象)
f = open("yesterday",'r',encoding="utf-8")
data = f.read()
print(data)
'''

# 变成一个迭代器,可以处理大文件，高效的方法
'''
f = open("yesterday",'r',encoding="utf-8")
for line in f:
    print(line.strip())
f.close()
'''
'''
f = open("yesterday",'r',encoding="utf-8")
for i in f.readlines():
    print(i.strip())
'''

'''
f = open('yesterday2','w',encoding="utf-8")
f.write("line1\n")
f.write("line2\n")
'''
'''
f = open('yesterday2','a',encoding="utf-8")
f.write("append")
f.close()
'''
'''
f = open('yesterday','r',encoding="utf-8")
print(f.tell()) #查看光标,指针
print(f.readline())
#print(f.read(50))
print(f.tell())
f.seek(0)
print(f.readline())
print(f.encoding)
print(f.fileno())   #文件描述符
print(f.name)
print(f.isatty())
print(f.flush())
'''
'''
f = open('yesterday2','w',encoding="utf-8")
f.write("hello 1\n")
f.write("hello 2\n")
f.write("hello 3\n")
f.flush()
'''
'''
f = open('yesterday2','a',encoding="utf-8")
f.truncate(10)

'''
'''
#f = open("yesterday2",'r+',encoding="utf-8") #文件句柄 读写
#f = open("yesterday2",'w+',encoding="utf-8") #文件句柄 写读
#f = open("yesterday2",'a+',encoding="utf-8") #文件句柄 追加读写
f = open("yesterday2",'wb') #文件句柄  二进制文件
f.write("hello binary\n".encode())
f.close()
'''


'''
# file change
f = open("yesterday","r",encoding="utf-8")
f_new = open("yesterday2","w",encoding="utf-8")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等alex享受")
    f_new.write(line)
f.close()
f_new.close()
'''
'''
with open("yesterday","r",encoding="utf-8") as f:
    for i in f:
        print(i.strip())
'''
with open("yesterday","r",encoding="utf-8") as f,\
     open("yesterday2","r",encoding="utf-8") as f2:
    pass

