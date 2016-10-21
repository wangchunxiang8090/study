#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof! Woof!')

c = Cat("mao")
d = Dog("gou")
Animal.talk(c)
Animal.talk(d)
