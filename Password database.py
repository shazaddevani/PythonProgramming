#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:38:54 2022

@author: shazaddevani
"""

def InOperator():
    
    passwordDatabase = ('password', '123456', 'admin', 'root', '000000')
    
    checkPass = input("Enter a password: ")
    addname = input(" Enter username ")
    
    if checkPass in passwordDatabase:
        
        print("Your password is in the known database")
        print(passwordDatabase.index(checkPass))
    else:
        print("good password")
        print (addname)
 
if __name__=='__main__':
    InOperator()
     