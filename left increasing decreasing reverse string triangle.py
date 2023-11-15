# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:40:53 2023

@author: priya
"""

a ='amity'
for i in range(len(a)):
    for j in range(i+1):
        print(a[::-1][j], end='')
    print()
for i in range(len(a)):
    for j in range(len(a)-i-1):
        print(a[::-1][j], end='')
    print()