#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:33:37 2022

@author: shazaddevani
"""

count = 10
while count >=1:
    print(count)
    count -= 1
    if count == 4:
       # break
   # count = count - 1 
       print("there will be an error")
       continue
    print("\n", count)