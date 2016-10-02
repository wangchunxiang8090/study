#!/usr/bin/env python
# _*_ coding: utf-8 _*_
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

# add
# info["stu1104"] = "苍井空"
# print(info)

# change
# info["stu1103"] = "武藤兰"
# print(info)

# del
# info.pop("stu1103")
# print(info)
# del info["stu1102"]
# print(info)
# info.popitem()
# print(info)

# find
# print("stu1103" in info)
# print(info.get("stu1104"))
# print(info["stu1104"])


#多级字典嵌套及操作
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# print(av_catalog["大陆"]["1024"][1])


# other function
# value
# print(info.values())

#key
# print(info.keys())

# setdefault
# info.setdefault("stu1106","Alex")
# print(info)
# info.setdefault("stu1101","change")
# print(info)


# update
# b = {1:2,3:4, "stu1102":"龙泽萝拉"}
# info.update(b)
# print(info)

# items
# print(info.items())

# fromkeys
# print(dict.fromkeys([1,2,3],'testd'))
# print(info)




# for dict
for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)
