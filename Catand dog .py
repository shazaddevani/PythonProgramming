#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:51:32 2022

@author: shazaddevani
"""

def dog(n):
    print(" sounds like a dog")
    
    
   

def cat():
    print( "sounds like a cat")
    pass


def main():
    sound= input( "what is the sound")
    number = int(input("how many did you hear"))
    if sound.lower() == "woof":
        number = int(input("how many did you hear"))
        dog(number)
    elif sound.lower() == "meow":
        
        cat()
    
main()