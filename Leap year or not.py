# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:41:47 2023

@author: priya
"""

year = 2000
if year%4 == 0 and year%400 == 0 or year%100 == 0:
    print('this year is a leap year')
else: 
    print('this is not a leap year')