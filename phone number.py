#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:02:30 2022

@author: shazaddevani
"""
import Cellphone
def main():
    man = input("enter the name brand ")
    mod = input(" enter the model number")
    retail = float(input("enter the retail price"))
    phone = Cellphone.CellPhones(man, mod, retail)
    print("here is the data you have entered ")
    print(f'manufacture {phone.get_manufact()}')
    print(f'model number { phone.get_model()}')
    print(f'Retail Price  ${phone.get_retail_price():,.2f}')
if __name__=='__main__':
    main()
                                   
