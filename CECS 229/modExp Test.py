# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1