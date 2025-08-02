# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 12:20:08 2025

@author: ArtemT
"""

config = dict()
with open('connections.config') as file:
    for line in file:
        info = line[:-1].split('=')
        config[info[0]] = info[1]
print(config)