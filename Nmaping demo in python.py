#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:11:05 2022

@author: shazaddevani
"""

import socket
import time
if __name__ =="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target = input('What you want to scan?: ')
    IPUSED = socket.gethostbyname(target)
    print('Starting scan on host:', IPUSED)
   
    start = time.time()
    for port in range(5):
        try:
            s.connect((IPUSED, port))
            print(f'port {port} is open')
        except:
            print(f'port {port} is closed')
    end = time.time()
    print(f'Time taken {end-start:.2f} seconds')
        
        
        
	
  
	
    



