#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:37:43 2022

@author: shazaddevani
"""

number_guessed =int(input(" pleaase choose a anumber from 1-200:"))
print("\n")
if (number_guessed <= 200):
    if(number_guessed < 200 and number_guessed >= 150):
        print("you have entered a value in the correct range")
        print(" the number you chose is less than 200 but greater than 149")
    elif(number_guessed < 150 and number_guessed >=100): 
        print("you have entered a value in the correct range")
        print(" the number you chose is less 150, but greater than 99")
    elif(number_guessed < 100 and number_guessed >=50):
        print("you have entered a value is the correct range ")
        print(" the number you have entered is less than 100 but greater than 49")
    elif(number_guessed < 50 and number_guessed > 1 ):
        print(" you have entered the a value that is correct")
        print(" the number you have entered is lees than 50 but greater than 0")
    elif(number_guessed <= 0):
        print(" the value you have entered is not in the corrext range ")
        if(number_guessed == 0):
            print("the number you have provided is 0")
        elif(number_guessed < 0):
            print(" the number you have entered is less than zero")
else: 
    print("you did not enter a value in the correct range.")
    print(" the number you entered was greater than 200")