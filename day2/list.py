#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#names = "ZhangYnag GuYun Xiangpeng XuLiangChen"
#names = ["ZhangYnag", "GuYun","Xiangpeng", "XuLiangChen"]

#切片
# print(names)
# print(names[0])
# print(names[1:3])
# print(names[0:3])
# print(names[:3])
# print(names[-1])
# print(names[-2:])
# print(names[:])

# delete
# names.remove("ChenRongHua")
# del names[0]
# names.pop()
# names.pop(0) # del names[0]
# print(names)

# append
# names.append("LeiHaiDong")
# names.insert(1,"ChenRongHua")

# change
# names[2] = "XieDi"

# find index
# print(names.index("GuYun"))
# print(names[names.index("GuYun")])

# pos = 0
# a = [ '!','@','#','eric',2,2,'jack','jack','a','b',2,'c','d','e',1,2,3,4,5,6,7,1,2,3,4,5,6]
# for i in range(a.count(2)):
#     if pos == 0:
#         pos = a.index(2)
#     else:
#         pos = a.index(2,pos+1)
#     print(pos)



# count
# names.append("GuYun")
# print(names.count("GuYun"))

#clear
# print(names.clear())

# reverse
# names.reverse()
# print(names)

# sort
# names.sort()
# print(names)

#extemd
# names2 = [1,2,3,4]
# names.extend(names2)
# print(names,names2)

# copy
# names = ["ZhangYnag", "GuYun","Xiangpeng", ["Alex","Eric"],"XuLiangChen"]
# names2 = names.copy()
# print(names)
# print(names2)
# names[1] = "顾云"
# print(names)
# print(names2)
# import copy
# names2 = copy.copy(names)
# print(names2)
# name3 = copy.deepcopy(names)
# print(name3)


# for
names = ["ZhangYnag", "GuYun","Xiangpeng", ["Alex","Eric"],"XuLiangChen"]
print(names[::2])
# for i in names:
#     print(i)

