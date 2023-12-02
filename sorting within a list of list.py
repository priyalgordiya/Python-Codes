# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:23:03 2023

@author: priya
"""

a = [[2,2], [3,3], [5,5]]
b=[]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] in b:
            b=b
        else: 
            b.append(a[i][j])
            
print(b)    

        