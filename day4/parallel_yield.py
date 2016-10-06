#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("chenzhonghuan")
# c.__next__()
# b1="大葱"
# c.send(b1)  #send被yield接收到了,并且把改值赋值给了baozi。唤醒同时传递一个值

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
            time.sleep(1)
            print("做了2个包子!")
            c.send(i)
            c2.send(i)

producer("alex")