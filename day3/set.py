#!/usr/bin/env python
# _*_ coding: utf-8 _*_

l1 = [1,4,5,7,3,6,7,9]
l1 = set(l1)

l2 = set([2,6,0,66,22,8,4])
print(l1,l2)

# 交集
print(l1.intersection(l2))

# 并集
print(l1.union(l2))

# 差集
print(l1.difference(l2))
print(l2.difference(l1))

# 子集
# print(l1.issubset(l2))
# print(l1.issuperset(l2))
l3 = set([1,3,7])
print(l3.issubset(l1))

# 对称差集
print(l1.symmetric_difference(l2))

print('-----------------------------')
# & | - ^
print(l1 & l2)
print(l1 | l2)
print(l1 - l2)
print(l1 ^ l2)

print(l1.discard('fff'))
#print(l1.remove("fff"))
print(1 in l1)