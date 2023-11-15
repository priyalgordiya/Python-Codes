# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:11:48 2023

@author: priya
"""

a = 'amity'
for i in range(len(a)):
    for j in range(i+1):
        print(a[j], end='')
    print()