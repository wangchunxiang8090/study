#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
import time
import datetime
def nginx_tiem_replace(tm):
    struct_time = time.strptime(tm,'%m/%b/%Y:%H:%M:%S ')
    return time.strftime("%Y-%m-%d %H:%M:%S ",struct_time)

def replace_after_data(filename):
    data = []
    with open(filename,'r') as f:
        for i in f:
            x = re.search('.*\[(.*:[0-9]+ ).*',i.strip())
            try:
                i=i.replace(x.group(1),nginx_tiem_replace(x.group(1))).strip()
                data.append(i)
            except Exception as e:
                pass
    return data
x = replace_after_data(r"C:\Users\wangcx\Desktop\nginx.log")
for i in x:
    print(i)

# for i in x:
#     data = re.search('.*([0-9]{4}-[0-9]{1,2}-[0-9]{2}).*',i)
#     print(data.groups())
    # for i in range(1,31):
    #     date = datetime.date.today() - datetime.timedelta(days=i)
    #     if date == data.groups()[0]:
    #         print(i)