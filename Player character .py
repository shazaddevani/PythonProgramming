#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:31:41 2022

@author: shazaddevani
"""
import playercharacter
def main():
    wellbeing = int(input("Enter the health from 1-100: "))
    if wellbeing <= 0 or wellbeing > 100:
       
else:
        print("not in range ")
   
    protectionrating  = int(input(" Enter the armor rating from 1-20: "))
    strength = int(input(" Enter the Attacking power from 1-20: "))
    character = playercharacter.Wizard(wellbeing, protectionrating, strength)
    print("here is the data you have entered ")
    print(f'The health of the character {character.get_health()}')
    print(f' the armor rating of the weapon { character.get_armor_rating()}')
    print(f' The attacking power of the character {character.get_attack_power()}  ')
if __name__=='__main__':
    main()
     