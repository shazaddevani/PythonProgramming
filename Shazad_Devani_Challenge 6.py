#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:57:44 2022

@author: shazaddevani
"""
def filecontrol():
    user_file = open('/Users/shazaddevani/Desktop/TXT/FunWithFiles.txt', 'r')
    file_contents = user_file.read()
    print(file_contents)
    user_file.close()
    userName1 = input("What is your favorite movie ")
    
    inFile = open('/Users/shazaddevani/Desktop/TXT/FunWithFiles.txt', 'a')
    
    inFile.write('\n' + userName1)
    
    inFile.close()
    
if __name__=='__main__':
    filecontrol()
  