# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:35:22 2023

@author: priya
"""


a = 'amity'
for i in range(len(a)):
    for j in range(len(a)-i):
        print(a[::-1][i], end='')
    print()