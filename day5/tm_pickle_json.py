#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pickle
data = {'k1':'v1','k2':'hello'}
p_str = pickle.dumps(data)
print(p_str)

with open('temp.pickle','w') as pi:
    pickle.dump(p_str,pi)

import json
j_str = json.dumps(data)
print(j_str)

with open('temp.json','w') as fp:
    json.dump(j_str,fp)