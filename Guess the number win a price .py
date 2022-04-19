#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 13:18:13 2022

@author: shazaddevani
"""
number_guessed = int(input(" please choose a number from 1-50"))
print("\n")
if(number_guessed == 50):
    print(" you have won a grand prize of a car")
elif(number_guessed == 45):
    print(" you have won a small price of a bike")
else:
    print(" you didnt choose the correct value ")
