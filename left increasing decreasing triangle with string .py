# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:37:37 2023

@author: priya
"""

a = 'amity'
for i in range(len(a)):
    for j in range(i+1):
        print(a[j], end='')
    print()
for i in range(len(a)):
    for j in range(len(a)-i-1):
        print(a[j],end='')
    print()