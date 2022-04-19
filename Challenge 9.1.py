#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:55:26 2022

@author: shazaddevani
"""


def studentgradebook(student_name,grade_book):
    

    if student_name in grade_book:
        
        print(grade_book[student_name])

       
    if student_name not in grade_book:
        print("The student does not exist in the grade book.")
        pass
    gradebook=[]  
    for number in range(1,4):
        grade= int(input(f"please enter the grade {number}"))
        gradebook.append(grade)
    grade_book[student_name] = gradebook
    



def Menu():
    
    student_name = input("Enter the students name to see their respective grades: ")
    grade_book ={'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82]}
    print(grade_book)
    print(student_name)
    studentgradebook(student_name, grade_book)
    print(grade_book)
    
if __name__=='__main__':
    Menu()
   

