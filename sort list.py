# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:39:29 2023

@author: priya
"""

a = [[4,1,3], [6,1,8]]
b=[]
c=[]
for i in range(len(a)):
    
    for j in range(len(a[i])):
        
        c.append(a[i][j])
        #print(c)
        #b.append(c)

print(c) 