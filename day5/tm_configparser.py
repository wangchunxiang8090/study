#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import configparser

# create config file
config = configparser.ConfigParser()
config['DATABASE'] = {'ip':'127.0.0.1',
                      'port':'3306',
                      'user':'alex',
                      'password':'123',
                      }
with open('example.conf','w') as conf:
    config.write(conf)

# read
print(config.sections())
print(id in config)