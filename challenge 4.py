#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:21:57 2022

@author: shazaddevani
"""
count = 0
user_name=input(" would you like to play a game")
if user_name =="no":
    print(" goodbye")
elif user_name == "yes" :
    print(",")
    while(user_name == "yes"):
        number_guessed = int(input(" please choose a number from 1-50"))
        count+= 1
    if (number_guessed < 1 or number_guessed > 50 ):
        
        print("error message")
    if (number_guessed == 45):
        
        print(" you have won a major price ")
           
    elif(number_guessed >= 35 and number_guessed <=40 and number_guessed!=45):
        print(" you have won a small price")
            
        
else:
    print("try again")
print(f"you have guessed {count} times")
        



   
   
       