#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:30:37 2022

@author: shazaddevani
"""
while True:
    ins=input(" write your number 122-222-2222")
    
    
    phone = []
    
    isValid = True
    
    for i in ins :
        
        if i not in "0123456789-":
            isValid = False
    
    if len(ins) != 12 or ins[3] != '-' or ins[7] != '-':
        isValid = False
            
        
    if isValid:
        print(' its a match')
        break
    else:
        print("Damn it bro use the correct value ")

