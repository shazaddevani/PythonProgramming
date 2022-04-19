#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:30:06 2022

@author: shazaddevani
"""

print("Hello, please enter your name.")
userName = input()
x = 2022
#age = int(input("enter today's year"))
myNumber = int(input("please enter your birth year "))
newNumber = x - myNumber
myNumber = str(myNumber)
newNumber = str(newNumber)
print('Your name is ' + userName + ". " + 'You were born in ' + myNumber + ".")
print('That makes you approximately ' + newNumber + " years old.")


