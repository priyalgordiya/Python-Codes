# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:49:10 2023

@author: priya
"""

#Balcony
#determing whether apartment A / B - which one has bigger balcony.
ALength = 5
Blength = 12
Awidth = 5
Bwidth = 3
areaa = ALength*Awidth
areab = Blength*Bwidth
if areaa>areab: 
    print('AREA OF APARTMENT A is ' + str(areaa) + ' &' + ' AREA OF APARTMENT B is  ' + str(areab))
    print('Apartment A has bigger balcony than Apartment B')
else:
    print('AREA OF APARTMENT B is ' + str(areab) +  ' &' + ' AREA OF APARTMENT A is  ' + str(areaa))
    print('Apartment B has bigger balcony than Apartment A')