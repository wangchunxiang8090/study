#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))

r1 = Role('Alex','police','AK47') #实例化(初始化一个类，造了一个对象)
r2 = Role('Jack','terrorist','B22')  #生成一个角色

r1.buy_gun("AK47")
# 把一个类编程一个具体对象的过程叫做实例化
Role('one','terrorist','B33').got_shot()    #调用完成就销毁了，赋值变量，在内存中长期保存
Role('one','terrorist','B33').got_shot()    #再次使用的时候调用也不是同一个对象（内存地址使不一样的）

