#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:30:25 2022

@author: shazaddevani
"""

def menu():
    addname = input( " would you like to a sttudent in the grade book")
    if addname ==  'yes':
        addstudent()
    else:
        print("Au reviour")
        
def addstudent():
    name= input(" please add the name ")
    lists = [ ]
    for number in range(1,4):
        
        grade= int(input("add the grade of the student"))
        lists.append(grade)
    studentgradebook(name, lists)
def studentgradebook(key,value):
    grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82]}
    grade_book[key]= value
    print(grade_book)
    
if __name__=='__main__':
    menu()