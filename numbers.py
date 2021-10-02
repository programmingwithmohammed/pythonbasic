# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 00:17:22 2021

@author: mjach
"""
'''
python has three types of number int, Float, and complex
In python integer and other data types are objects. By saying that means 
we can create new one by calling methods.
'''

'''Integer number '''

#these are all integer number
a = 12
b = - 1000
c = 0

'''Float numbers'''
#these are all float numbers

a = 7.0
b = -17.3
c = 0.

''' Complex number '''
#these are all complex number

a = 22j

#Integer and float number can be added togather and 
# result will be float
#Example

a = 5.0 #float number
b = 2 # integer number

c = a + b
print('C=',c) # result will be float

'''
Boolean types
'''
# in python boolean are also a number. boolean types are True or Flase
# True is 1
# Flase is 0

''' % modulas not a percent sign? How does it work? '''

# Example A divided by B with C remaing
# suppose if you divided 

A = 17
B = 3

C = 17 % 3

print ('C', C) # will show remaing value


'''Python calculation order of operation - PEMDAS '''
# P = Parentheses
# E = Exponents
# M = Multiplication
# D = Division
# A = Adition
# S = Substract

''' / (divide) round down'''
#it is not really rounding down, rather it is just dropping fractional 
#part after decemial point

# Example 

x = 11.0
y = 4.0
z = 11.0/4.0
print('Z =',z) # will drop the fractional part

z = 11/4
print('Z=',z) # will drop the fractional part