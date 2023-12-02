# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:59:27 2023

@author: priya
"""

a = [[2,8], [3,3], [5,5]]
b=[]

for i in range(len(a)):
    
    for j in range(len(a[i])):
        c = []
        c.append(a[i][j])
        b.append(c)

print(b)    