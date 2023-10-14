# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:54:36 2023

@author: priya
"""

for i in range(5):
    for j in range(i,5):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    for j in range(i):
        print('*', end= '')
    print()