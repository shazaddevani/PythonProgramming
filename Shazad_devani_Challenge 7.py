#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:38:54 2022

@author: shazaddevani
"""

    
def InOperator():
    
    passwordDatabase = ('password', '123456', 'admin', 'root', '000000', 'AAAAAAAAAAAAA')
    
    addname = input(" Enter username ")
    checkPass = input("Enter a password: ")

    
   # if checkPass in passwordDatabase:
        
     #   print("Your password is in the known database")
     #   print(passwordDatabase.index(checkPass))
    #else:
    #    print("good password")
     #   print (addname)
        
    has_valid = ["%","@","!","^","*"]
    has_invalid = ['#', '$','_','+']
    is_valid = False
    while not is_valid:
        if checkPass in passwordDatabase: 
            print("Your password is in the known database")
            print(passwordDatabase.index(checkPass))
            checkPass = input("Enter a password: ")
        else:
            correct_length = False 
            has_uppercase = False
            has_lowercase = False
            has_digit = False 
            has_valid = False
            has_invalid = True
            if len(checkPass) >=8:
                correct_length = True
                for c in checkPass:
                    if c.isupper():
                        
                        has_uppercase =True
                    if c.islower():
                        
                        has_lowercase=True
                    if c.isdigit():
                        
                        has_digit=True
                    if '@' or '%'or '!' or '*' == c:
                        
                        has_valid = True
                    if '#' == c:
                        
                        has_invalid = False
                #for checkPass in passwordDatabase:
                    #if checkPass.isupper():
                     #   print("Test upper")
                      #  has_uppercase =True
                    #if checkPass.islower():
                     #   has_lowercase=True
                    #if checkPass.isdigit():
                    #    has_digit=True
                    #if '@' in checkPass:
                     #   has_valid = True
                    #if '#' in checkPass:
                     #   has_invalid = True
                    
                    
                if correct_length and has_uppercase and has_lowercase and has_digit and has_valid and has_invalid:
                    print("valid")
                    is_valid =True
                else:
                    print(" password not valid ")
                    #has_invalid = False
                    is_valid= False 
                    checkPass = input("Enter a password: ")  
            else:
                print(" password not valid ")
                is_valid = False
                checkPass = input("Enter a password: ")  
    passwordDatabase = passwordDatabase + (checkPass, )
    print(passwordDatabase)
    print(addname + " your password is added to the database" )
                    
    
 
if __name__=='__main__':
    InOperator()
   
     