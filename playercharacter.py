#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:16:10 2022

@author: shazaddevani
"""

class Wizard:
    def __init__(self,health,armor_rating,attack_power):
        self.__health= health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power
    def set_health(self, health):
        self.__health = health
    def set_armor_rating(self,armor_rating):
        self.__armor_rating = armor_rating 
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    def get_health(self):
        return self.__health
    def get_armor_rating(self):
        return self.__armor_rating
    def get_attack_power(self):
        return self.__attack_power
    
import playercharacter
def main():
   
   try: 
       wellbeing = int(input("Enter the health from 1-100: "))
       if wellbeing <= 0 or wellbeing > 100:
           raise NameError
              
           
          
       protectionrating  = int(input(" Enter the armor rating from 1-20: "))
       if protectionrating <=0 or protectionrating >20:
           raise NameError
       strength = int(input(" Enter the Attacking power from 1-20: "))
       if strength <=0 or strength >20:
           print('strength entered')
           raise NameError
       

       character = playercharacter.Wizard(wellbeing, protectionrating, strength)
       print("here is the data you have entered ")
       print(f'The health of the character {character.get_health()}')
       print(f' the armor rating of the weapon { character.get_armor_rating()}')
       print(f' The attacking power of the character {character.get_attack_power()}  ')
   except NameError :
       print("it was out of range")    
if __name__=='__main__':
    main()
     
        
        
    