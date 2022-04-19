#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:34:56 2022

@author: shazaddevani
"""

class Student:
    def __init__(self,GPA,year):
        self.__GPA= GPA
        self.__year= year
    def set_GPA(self,GPA):
        self.__GPA = GPA
    def set_year(self,year):
        self.__year =year
    def get_GPA(self):
        return self.__GPA
    def get_year(self):
        return self.__year
class Teachers:
    def __init__(self,tenure, major):
        self.__tenure= tenure
        self.__major= major
    def set_tenure(self,tenure):
        self.__tenure = tenure
    def set_major(self,major):
        self.__major
    def get_tenure(self):
        return self.__tenure
    def get_major(self):
        return self.__major
        
        
    
    

    