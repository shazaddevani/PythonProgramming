#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:55:22 2022

@author: shazaddevani
"""
user_name=input(" would you like to play a game")
if user_name == "yes" :
    print("lets play a a game")
    number_guessed = int(input(" please choose a number from 1-55"))
    print("\n")
    if(number_guessed == 50):
        print(" you have won a grand prize of a car")
    elif(number_guessed == 45 or number_guessed == 55):
        print(" you have won a small price of a bike")
    else:
        print(" you didnt choose the correct value ")
else: user_name == "no"
print("goodbye")

