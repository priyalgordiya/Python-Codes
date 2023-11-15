# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:35:35 2023

@author: priya
"""

a = 'priyal'
b = ['a', 'e', 'i', 'o', 'u']
v=0
c=0
for i in range(len(a)):
    
   if a[i] in b:
    v= v+1
    
   else:
      c=c+1
      
print(v,c)    