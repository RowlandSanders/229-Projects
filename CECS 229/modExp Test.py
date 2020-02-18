# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def modExp(b, n, m) :      
    
    b=b%m  
    sum=0
    t = 1
    while (n > 0) : 
        if ((n & 1)==1) : 
            t=(t*b)%m
        b = (b**2)%m 
        n = n >> 1 #bitwise shift to right
    sum = t
    
    return sum
