#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:47:54 2022

@author: shazaddevani
"""

print("welcome")
count = 0 
baskets = 0
guess = 3 
while baskets!=10: 
    count+= 1
    guess=int(input("please guess a anumber from 1-5"))
    
    if(guess == 3):
        baskets +=1
print(count)

        
    