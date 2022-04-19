#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:21:57 2022

@author: shazaddevani
"""
user_name=input(" would you like to play a game")
if user_name =="no":
    print(" goodbye")
elif user_name == "yes" :
    print(",")
number_guessed = int(input(" please choose a number from 1-50"))
if(number_guessed == 45):
        print(" you have won a grand prize of a car")
elif(number_guessed >= 35 and number_guessed <=40 and number_guessed!=45):
        print(" you where so close you win a small price of a brick")
else:
    print(" try again")

   
       