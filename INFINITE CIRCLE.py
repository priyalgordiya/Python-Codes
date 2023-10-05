# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 10:35:46 2023

@author: priya
"""

import turtle 
t=turtle.Turtle()
for i in range(10):
    print(i)
    radius=100-i*10
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()
    
    