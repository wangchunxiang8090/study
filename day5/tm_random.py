#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import random
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10))
print(random.choice("学习Python"))#学
print(random.choice(["JGood","is","a","handsome","boy"]))  #List
print(random.choice(("Tuple","List","Dict")))   #List
print(random.uniform(1, 10)) #9.887001463194844
items = [1,2,3,4,5,6,7]
print(items) #[1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items) #[1, 4, 7, 2, 5, 3, 6]


import random
def password(length=12):
    code = []
    for i in range(length):
        r = random.randint(1,9)
        if r == i:
            code.append(str(random.randint(0,9)))
        elif r > 5:
            code.append(chr(random.randrange(97,122)))
        else:
            code.append(chr(random.randrange(65,90)) )
    print(''.join(code))

if __name__ == "__main__":
    number=input('please input generator password length default length 12:')
    if len(number) == 0:
        password()
    else:
        if number.isdigit():
            number = int(number)
            password(number)
        else:
            exit('invalid input')