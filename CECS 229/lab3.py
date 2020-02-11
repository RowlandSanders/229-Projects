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
    
    sum = ''
    
    c = 0
    carry = 1
    carry2 = 0
    
    print("a = ",a)
    print("b = ",b)
    
    i = len(a) - 1
    while (i>=0):
        x = int(a[i])+int(b[i]) #iterating and testing the possible additions per line
        if x==2:
            if c==0:
                c = carry
                sum = "%s%s" % (sum, '0') #checks for carry then adds
            else: 
                sum = "%s%s" % (sum, '1')
                
        elif x == 1: 
            if c == 1:
                sum = "%s%s" % (sum, '0')
            else:
                sum = "%s%s" % (sum, '1')
        else: 
            if c == 1:
                sum = "%s%s" % (sum, '1')
                c = carry2   
            else:
                sum = "%s%s" % (sum, '0') 

        i = i - 1;

    if c>0:             #THIS WAS AVAILIABLE IN LEARNING PYTHON BY MARK LUTZ (Last 3 lines) in "understanding binary addition"
       sum = "%s%s" % (sum, '1')
    return sum[::-1] 
    
    #FIXME: IF STRING b IS SHORTER THAN STRING a, APPEND 0's TO THE BEGINNING OF STRING b TO MAKE LENGTHS EQUAL
     

    #sum = bin(int(a,2)+int(b,2))[2:]
    
    #return str(sum)
    

    
    #FIXME: FINISH THE FUNCTION SO THAT IT RETURNS THE DESIRED OUTPUT 
        