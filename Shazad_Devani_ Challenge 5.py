#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:02:56 2022

@author: shazaddevani
"""

GRAVITY = 9.8

def fallingDistance(time_of_fall):
    for distance_traveled_per_second in range(1,time_of_fall+1):    
        result = (0.5 * GRAVITY) * (distance_traveled_per_second**2)
        print(result)
    

def main():
    time = int(input(" how long is the object falling "))
    fallingDistance(time)
    
    
    
main()