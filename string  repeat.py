# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:39:40 2023

@author: priya
"""

a = 'amity'
for i in range(len(a)):
    for j in range(i+1):
        print(a[i], end='')
    print()