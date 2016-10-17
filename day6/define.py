#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s wang wang wang " %self.name)

d1 = Dog("陈荣华")
d2 = Dog("陈三炮")
d3 = Dog("成老跑")

d1.bulk()
d2.bulk()
d3.bulk()

