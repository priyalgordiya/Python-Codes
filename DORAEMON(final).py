# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:03:45 2023

@author: priya
"""

import turtle
t=turtle.Turtle()
t.speed(100)
#scarf 1
t.pensize(4)
t.pencolor("dark green")
t.forward(200)


t.penup()
t.goto(177, 0)
t.pendown()

#first circle-face
t.left(40)
t.circle(120, 279)

t.penup()
t.goto(158.5, 0)
t.pendown()

#second circle-face
t.left(81)
t.circle(90, 279)

#nose
t.penup()
t.goto(200, 0)
t.pendown()
t.penup()
t.goto(95, 95)
t.pendown()
t.circle(12)
t.penup()
t.goto(102, 90)
t.pendown()
t.right(49.5)
t.forward(77)


#beard
t.penup()
t.goto(130, 70)
t.pendown()
t.left(90)
t.forward(40)
t.penup()
t.goto(130, 63)
t.pendown()
t.right(14)
t.forward(40)
t.penup()
t.goto(130, 80)
t.pendown()
t.left(24)
t.forward(40)
t.left(90)
t.penup()
t.goto(70, 70)
t.pendown()
t.left(80)
t.forward(40)
t.penup()
t.goto(70, 63)
t.pendown()
t.left(14)
t.forward(40)
t.penup()
t.goto(70, 80)
t.pendown()
t.right(24)
t.forward(40)
t.penup()

#right hand
t.penup()
t.goto(186, 10)
t.pendown()
t.right(135)
t.forward(55)
t.right(180)
t.circle(15)
t.penup()
t.goto(240,14)
t.pendown()
t.left(30)
t.forward(70)
t.penup()
t.goto(225, -5)
t.pendown()

#scarf 2
t.penup()
t.goto(200, 0)
t.pendown()
t.left(90)
t.circle(-10, 94.5)
t.right(60)
t.forward(207)
t.right(60)
t.circle(-10, 94.5)

#left hand
t.penup()
t.goto(2, -15)
t.pendown()
t.right(160)
t.forward(60)
t.circle(15)
t.penup()
t.goto(5, -55)
t.pendown()
t.forward(30)
#left side straight line below scarf
t.penup()
t.goto(4, -40)
t.pendown()
t.left(48)
t.forward(150)

# left foot
t.right(88)
t.forward(15)
t.circle(8, 180)
t.right(5)
t.forward(70)
t.circle(8, 180)
t.forward(11)

#pocket
t.penup()
t.goto(45, -15)
t.pendown()
t.left(60)
t.circle(70, 240)
t.penup()
t.goto(48, -60)
t.pendown()
t.right(121.2)
t.forward(118)

#inside pocket
t.penup()
t.goto(48, -60)
t.pendown()
t.right(80)
t.circle(59, 160)

#right straight line below scarf
t.penup()
t.goto(210, -30)
t.pendown()

#right foot
t.right(169)
t.forward(160.2)
t.left(88)
t.forward(15)
t.right(40)
t.circle(-10, 90)
t.right(47.5)
t.forward(80)
t.right(50)
t.circle(-10, 90)
t.right(33)
t.forward(12)
t.left(90)
t.circle(50,166)

#eye1
t.penup()
t.goto(88, 110)
t.pendown()
t.right(62)
t.circle(-28, 90)
t.left(5)
t.circle(-30, 70)
t.right(10)
t.circle(-30, 70)
t.right(5)
t.circle(-30, 70)
t.right(-15)
t.circle(-20, 70)


#eye2
t.penup()
t.goto(134, 107)
t.left(50)
t.pendown()
t.right(62)
t.circle(-28, 90)
t.left(5)
t.circle(-30, 70)
t.right(10)
t.circle(-30, 70)
t.right(5)
t.circle(-30, 70)
t.right(-15)
t.circle(-20, 70)
t.penup()
t.goto(135, 126)
t.right(88)
t.pendown()
t.pensize(4)
t.circle(10,180)
t.penup()
t.goto(85, 120)
t.pendown()
t.right(88)
t.circle(-10)
t.penup()
t.goto(85, 125)
t.pendown()
t.circle(-2)

#mouth
t.penup()
t.goto(50,41)
t.pendown()
t.left(115)
t.circle(60,120)

#bell
t.penup()
t.goto(116, -35)
t.pendown()
t.circle(15)
t.penup()
t.circle(20,25)
t.pendown()
t.pensize(4)
t.left(50)
t.circle(20,90)
t.pensize(4)
t.left(180)
t.circle(-20,90)
t.penup()
t.goto(101,-27)
t.pendown()
t.right(85)
t.circle(4)
t.circle(3,135)
t.right(90)
t.forward(10)
t.hideturtle()












