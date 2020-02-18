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
# #### Problem 1:
# 
# Program a function `modExp(b, n, m)` that computes $$b^n \mod m$$ using the algorithm discussed in lecture.  The function should satisfy the following:
# 
# 1. INPUT: 
#     * `b` - positive integer representing the base
#     * `n` - positive integer representing the exponent
#     * `m` - positive integer representing the modulo
# 
#     
# 2. OUTPUT:
#     * the computation of $b^n \mod m$
# 
#  
# EXAMPLE: 
# 
# `>> modExp( 3 , 644, 645 )`
# 
# `36`
# 
# 

# In[1]:


def modExp(b, n, m):
    sum=(b**n)%m
    return sum


# #### Problem 2:
# 
# Create a function `bezoutCoeffs(a, b)` that computes the Bezout coefficients `s` and `t` of `a` and `b`.
# 
# 1. INPUT: 
#     * `a`,`b` - integers
# 
# 2. OUTPUT: `(s, t)` - tuple of coefficients
# 
# EXAMPLE:  
#  
# `>> bezoutCoeffs(414, 662)` 
# 
# `(8, -5)`
# 
# 

# In[2]:


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


# #### Problem 3:
# 
# Create a function `gcd(a, b)` that computes the greatest common divisor of `a` and `b`
# 
# 1. INPUT: 
#     * `a`,`b` - integers
# 
# 2. OUTPUT: `d` - the gcd
# 
# EXAMPLE:  
#  
# `>> gcd(414, 662)` 
# 
# `2`

# In[3]:


def gcd(a,b):
    while b: 
       a, b = b, a % b 
    sum = a
    return sum


# In[5]:


""" TESTER CELL """
print("Testing modExp(23, 1002, 41) = ", modExp(23, 1002, 41))
print("Testing bezoutCoeffs(26, 7) = ", bezoutCoeffs(26, 7))
print("Testing gcd(101, 4620) = ", gcd(101, 4620))
print("Testing gcd(2349, 36) = ", gcd(2349, 36))


# In[ ]:





# In[ ]:




