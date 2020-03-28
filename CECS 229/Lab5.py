#!/usr/bin/env python
# coding: utf-8

# # CECS 229: Lab Assignment #5
# 
# ### Submission Instructions:
# 
# Complete the task below. When you are finished, you must complete the following to receive a grade:
# 
# 1. Submit this notebook to the Dropbox by **Friday 3/27 @ 11:59 PM**.  Rename this file so that your actual name replaces "YOUR NAME". For example, I would submit to the dropbox a file called `CECS 229 Lab Assignment #5 - KATHERINE VARELA.ipynb`.
# 
# 2. Save your code ONLY to a .py file called `lab5.py`, and submit it on CodePost by the due date.

# #### Problem 1:
# 
# Create a function `translate(S, z0)` that translates the points in the input set $S$ by $z_0 = a_0 + b_0 i$.  The function should satisfy the following:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `z0` - complex number
# 2. OUT:
#     * `T` - set T consisting of points in S translated by $z_0$

# In[1]:


def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * T - set consisting of points in S translated by z0
    """
    T = []
    for z in S:
        T.append(z0 + z)
    return set(T)
pass


# In[2]:


from plotting import plot

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

T = translate(S, -1+2j)
plot(S)
plot(T)


# #### Problem 2:
# 
# Create a function `scale(S, k)` that scales the points in the input set $S$ by a factor of $k$:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `k` - positive float, if negative or zero factor is given then the function raises a ValueError with message, "ERROR: Scaling factor must be a positive float".
# 2. OUT:
#     * `T` - set T consisting of points in S scaled by $k$ and rotated by $\theta$

# In[3]:


def scale(S, k):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    #FIXME: IMPLEMENT FUNCTION
    for i in S:
        yield (i * k)
    pass


# In[4]:


U = scale(S, 3)
plot(U,11) #second parameter affects window size


# #### Problem 3:
# 
# Create a function `rotate(S, theta)` that rotates the points in the input set $S$ by $\theta$ radians:
# 
# 1. INPUT: 
#     * `S` - set S
#     * `theta` - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
# 2. OUT:
#     * `T` - set T consisting of points in S rotated by $\theta$

# In[8]:


def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * T - set consisting of points in S rotated by theta radians
        
    """
    output=set()
    
    if(theta==0):
        return S
    
    else:
        angle=complex(math.cos(theta),math.sin(theta))
        for i in S:
            n=i*angle
            output.add(n)
            
        return output
    pass


# In[10]:


import math
V = rotate(S, math.pi/12)
W = rotate(S, -math.pi/4)
plot(V)
plot(W)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




