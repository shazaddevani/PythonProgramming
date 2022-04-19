#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:00:56 2022

@author: shazaddevani
"""
import re 
while True:
    ins=input(" write your number 122-222-2222")
    valid = re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}",ins)
    if valid:
        print('it is a match')
    else:
        print("damn it bro use the correct value or use the correct structure")

