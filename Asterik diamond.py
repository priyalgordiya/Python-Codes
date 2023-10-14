# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:07:24 2023

@author: priya
"""

for i in range(5-1):
    for j in range(i,5):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    for j in range(i):
        print('*', end='')
    print()
for i in range(5):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,5):
        print('*', end='')
    for j in range(i, 4):
        print('*', end='')
    print()