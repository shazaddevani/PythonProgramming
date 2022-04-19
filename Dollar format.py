#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:40:56 2022

@author: shazaddevani
"""

def DollarFormat(value):
    return f'${value}'
def main():
    usernumber=float(input("how you spent today"))
    dollar= DollarFormat(usernumber)
    print(dollar)
    
if __name__ == '__main__':
    main()