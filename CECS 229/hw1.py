#!/usr/bin/env python
# coding: utf-8

# # CECS 229: Coded HW #1
# 
# ### Submission Instructions:
# 
# Attach your coded solution to the programming tasks below. When you are finished...
# 
# 1. Rename this file so that your actual name replaces "YOUR NAME" in the current notebook name, and submit it to the dropbox by **Tuesday 2/18 @ 11 AM**. For example, I would submit to the dropbox a file called  `CECS 229 Coded HW#1 - KATHERINE VARELA.ipynb`
# 2. Submit your code only to CodePost as `hw1.py` by **Tuesday 2/18 @ 11 AM**
# 
# 

# Submit the following Python functions in one Jupyter Notebook after demoing your work.
# 
# 

def modExp(b, n, m):
    sum=(b**n)%m
    return sum


def bezoutCoeffs(a, b):
    
    x = 0
    x1 = 1
    y = 1
    y1 = 0
    
    
    while (b != 0): 
        flr = (a // b)
        
        b1 = a % b
        a = b
        b = b1
        
        x, x1 =x1-(flr*x),x
        y, y1 =y1-(flr*y),y
        
    return (x1,y1)

def gcd(a,b):
    while b: 
       a, b = b, a % b 
    sum = a
    return sum



""" TESTER CELL """
print("Testing modExp(23, 1002, 41) = ", modExp(23, 1002, 41))
print("Testing bezoutCoeffs(26, 7) = ", bezoutCoeffs(26, 7))
print("Testing gcd(101, 4620) = ", gcd(101, 4620))
print("Testing gcd(2349, 36) = ", gcd(2349, 36))

