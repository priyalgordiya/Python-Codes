# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:04:14 2023

@author: priya
"""

a = 'amity'
for i in range(len(a)):
    for j in range(len(a)-i):
        print(a[i], end='')
    print()