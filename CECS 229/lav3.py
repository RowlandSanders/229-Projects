# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:39:33 2020

@author: Rowla
"""

def binaryAdd(a, b): #this is the beginning of a python function
    """This is the functions doc string
    returns the sum of two binary numbers a and b
    INPUT: a,b - string representation of the binary numbers
    OUPUT: string representation of their sum
    """
    a = a.replace(" ", "") #removing all whitespaces in string a
    #FIXME: REMOVE ALL WHITESPACES IN STRING b
    b = b.replace(" ", "")  #removing all whitespaces in string b
    
    m = len(a) #number of digits in string a
    n = len(b) #number of digits in string b
    
    if m < n: #if string a is shorter than string b
        num_missing_zeros = n - m
        a = num_missing_zeros*"0" + a #appending 0's to the beginning of string a, to make it the same length as b
        b = num_missing_zeros*"0" + b
    #FIXME: IF STRING b IS SHORTER THAN STRING a, APPEND 0's TO THE BEGINNING OF STRING b TO MAKE LENGTHS EQUAL
     
        print("a = ",a)
        print("b = ",b)
    
    #FIXME: FINISH THE FUNCTION SO THAT IT RETURNS THE DESIRED OUTPUT 
        