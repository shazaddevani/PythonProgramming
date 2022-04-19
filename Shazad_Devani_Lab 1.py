#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:12:15 2022

@author: shazaddevani
"""
x=1
user_name=input("What is your name")
print("Hello " + user_name +" welcome to the python pizza chooser")

choice = input(" what pizza would you like to have, pepperoni, cheese or supreme ")
print(" your "+choice+" pizza is here")

AP = input(" would like another pizza, yes or no? ")

if AP == "yes":
    x=1
    while AP == "yes":
        choice = input(" what pizza would you like to have, pepperoni, cheese or supreme ")
        x=x+1
        
        if choice == "supreme" or  choice == "cheese" or choice == "pepperoni":
            print("Another " + choice + " pizza is being prepared!")
            AP = input("Should I continue?")
   
    if AP == "no".lower:
        print(f" Thank you  {user_name} . The  {x}  pizzas you ordered will be ready in 30 minutes.")
else: AP == "no"
print(f" Thank you  {user_name} . The  {x}  pizzas you ordered will be ready in 30 minutes.")
    
                
    
    

