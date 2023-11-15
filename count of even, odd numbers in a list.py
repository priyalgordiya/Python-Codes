# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:41:31 2023

@author: priya
"""

a= [1,2,3,4,5,6,7,8,9,10]
even_count = 0
odd_count = 0
for i in range(len(a)):
    if a[i]%2 == 0:
        even_count= even_count+1
    else:
        odd_count= odd_count+1
print(even_count)
print(odd_count)