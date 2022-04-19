#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:26:00 2022

@author: shazaddevani
"""
'''

num = 40 
for i in range(0,10):
    num+=1
    print(num ,"\n")
    print(i)
    
for number in range (2,10,2):
    print(number)
    
print("\n")

for num in [1,2,3,4]:
    print(num, "\n")
    
print("-------------------------------")

for num in range(5):
    print(num, "\n")

for num in range(4,25,3):
    print(num, "\n")
    
    if num==16:
        print("error will robinson")
        continue
for numbers in range (6,0,-1):
    print(numbers)
    
end = int(input(" enter a number, and i will display its squared value:")
print("Number\tSquare")
print("'------------------")
for number in range(1, end ):
    square= number ** 2
    print(f"{number}\t\t{square}")
    '''
funny_word = "Badmamjama"
for letter in funny_word:
    print(letter)
    print(funny_word)
    
for num in[1,5,8,12,15]:
    print(num)
for name in[ "carl","sally","mike"]:
    print(name)
    
mylist =[1,5,8,14]
for mylist, i in enumerate(mylist):
    print( mylist, i)