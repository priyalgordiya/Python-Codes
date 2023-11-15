# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:25:27 2023

@author: priya
"""

a= [-5, 8, -9]
min_e = 0
for i in range(len(a)):
    if a[i] < min_e:
        min_e = a[i]
    else:
        min_e= min_e
print(min_e)