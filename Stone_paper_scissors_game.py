# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:50:37 2023

@author: priya
"""
import random
options = ["Rock", "Paper", "Scissors"]
my_choice = input("Rock, Paper, Scissors? ")
computer_choice = options[random.randint(0,len(options)-1)]
if my_choice==computer_choice:
    print('Its a tie')
elif my_choice=="Scissors":
    if computer_choice=="paper":
        print('Scissors cut paper. You win')
    else:
        print('rock smashed scissors. Computer wins')
elif my_choice=="Paper":
    if computer_choice=="Rock":
        print('paper covered rock. You win')
    else:
        print('scirssors cut paper.computer wins')
elif my_choice=="rock":
    if computer_choice=="scissors":
        print('rock smashed scissors. you win')
else:
    print('paper covers rock.computer wins')