# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:48:43 2022

Module 6 

@author: iburr
"""
import math

def readingFiles():
    
    #This is how we open a file in read mode
    user_file = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'r')
    
    #here, we will read the contents of the file
    file_contents = user_file.read()
    
    #we print the contents of the file
    print(file_contents)
    
    #we use the close() function to ensure the file has been closed
    #This is important or we can get into a memory leak. 
    user_file.close()
    
def writingFiles():
    
    userName1 = input("What is your name? ")
    userName2 = input("What is your mother's name? ")
    
    #Here we will open a file in write mode
    inFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'w')
    
    inFile.write(f'{userName1}\n{userName2}')
    
    inFile.close()
    
             
def readEachLine():
    
    #here we will open a file in read mode
    inFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'r')
    
    #Here we are reading each line of code and storing it into a variable
    firstLine = inFile.readline()
    secondLine = inFile.readline()
    thirdLine = inFile.readline()
    
    inFile.close()
    
    print(f'{firstLine}\n{secondLine}\n{thirdLine}')
    
    

def appendingFiles():
    
    inFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'a')
    
    inFile.write('\nKim')
    
    inFile.close()
    
 

def strippingLines():
    
    inFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'r')
    
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    #strip the new line character, and the white sapce to the right of the text
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line1.strip(' ')
    line4  = line1.strip('D')
    inFile.close()
    
   #print the values with a tabe space in between
    print(f'{line1}\n{line2}\n{line3}\n {line4}')
    
    
def savingNumericData():
    
    outFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'w')
    
    myNumber = int(input("Enter a number: "))
    
    #convert the number to a string, so it can be stored in the text document
    outFile.write(str(myNumber)  + '\n')

    outFile.close()  
    
    
def usingNumbersFromFiles():
    
    inFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'r')
    
    number1 = 501
    
    #store the line in a string variable
    line1 = inFile.readline()
    
    #convert the string variable into a integer
    value = int(line1)
    
    #perform an integer calculation
    result = number1 + value
    
    print('\n', result)
    
    inFile.close()
  

def usingLoops():
    
    outFile = open('/Users/shazaddevani/Desktop/TXT/Test.txt', 'w')
    
    highest_root = int(input("Enter a positive integer to see it's square root" + 
                             "and all square roots below said number: "))
    
    #set up a loop to continue adding a value to the file
    for count in range (highest_root, 0, -1):
        
        #do the math
        value = math.sqrt(count)
        
        #convert the int to a string so it can be stored in the text document
        result = str(value)
        #wtie the result ot the file
        outFile.write(f'{result}\n') 
    
    #close the file
    outFile.close()
    
if __name__=='__main__':
    
    readingFiles()
    #ritingFiles()
    #readEachLine()
   # appendingFiles()
    #strippingLines()
    #savingNumericData()
    #usingNumbersFromFiles()
    #usingLoops()