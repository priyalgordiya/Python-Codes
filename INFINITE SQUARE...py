# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:18:45 2023

@author: priya
"""

import turtle 
t=turtle.Turtle()
for i in range(10):
    
    #20 multiplied with i because it was forwarded by 10cm from one side.
    #so from other side it will also be forwarded by 10cm
    #so 10+10 = 20cm
    t.forward(200-i*20)
    t.right(90)
    t.forward(200-i*20)
    t.right(90)
    t.forward(200-i*20)
    t.right(90)
    t.forward(200-i*20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.penup()
    t.forward(10)
    t.left(90)
    t.pendown()   
    
    
    
    
    
    