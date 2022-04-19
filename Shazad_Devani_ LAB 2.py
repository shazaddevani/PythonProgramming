#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:11:17 2022

@author: shazaddevani
"""

def Database(studentname, changegrade, newgrade):    
    
    saved_database = []    #WE ARE CREATING AN EMPTY LIST HERE
    
    inFile = open('/Users/shazaddevani/Desktop/StudentGradeBook.txt', 'r')     #HERE WE ARE OPENING A FILE IN READ MODE
    
    for lines in inFile:    #WE ARE GOING TO LOOP THROUGH EVERY LINE IN THE FILE
        
        saved_database.extend(lines.split('\t'))    #WE ARE SAVING EACH ITEM SEPARATED WITH A TAB TO A LOCATION IN THE LIST
        
    print(saved_database)
    

        
    
    print('\n------------------------------')
    inFile.close()
    if studentname in saved_database:
        
        studentname1 = saved_database.index(studentname)
        
        saved_database[studentname1 + changegrade] = newgrade
        
        print(saved_database)
    else:
        print(" the name  is not there ")
        
    with open('/Users/shazaddevani/Desktop/StudentGradeBook.txt', 'w') as f:       #OPEN THE FILE IN WRITE MODE
        
        for elements in saved_database:   #ITERATE THROUGH EVERY ELEMENT IN THE DATABASE
            
            f.write('%s\t' % elements)   #WRITE EACH VALUE TO THE DATABASE BACK INTO DELIMITED FORM.  
            
            
    f.close()    
    
def ChangingGrades():
    studentname = input(" what is the students name ")
    changegrade = int(input(" what grade you would like to change "))
    newgrade = int(input(" what is his/hers new grade"))
    print(studentname,changegrade,newgrade)
    Database(studentname, changegrade, newgrade)
if __name__=='__main__':
    ChangingGrades()
   