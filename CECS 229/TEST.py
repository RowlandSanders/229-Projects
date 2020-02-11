# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:19:13 2020

@author: Rowla
"""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    #a = int('10110', 2) #(0*2** 0)+(1*2**1)+(1*2**2)+(0*2**3)+(1*2**4) = 22
    #b = int('1011', 2) #(1*2** 0)+(1*2**1)+(0*2**2)+(1*2**3) = 11

    sum = int(a, 2) + int(b, 2)

    if sum == 0: return "0"

    out = []

    while sum > 0:
        res = int(sum) % 2
        out.insert(0, str(res))
        sum = sum/2


    return sum