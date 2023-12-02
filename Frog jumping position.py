# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:50:41 2023

@author: priya
"""

fa = 2
fb = 3
fa_position = 10
fb_position = 3
a = int(fa_position+ fa )
b = int(fb_position +fb)
meeting_flag = 0

for i in range (10):
        a = fa_position+ i*fa 
        b = fb_position + i*fb
        if a==b:
         
         meeting_flag = 1
         
         
if meeting_flag == 1:
    print('frog 1 & 2 will overlap ')
else:
    print('frog 1 & 2 will not overlap ')
    
