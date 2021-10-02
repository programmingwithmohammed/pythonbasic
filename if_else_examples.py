# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 03:16:37 2021

@author: mjach
"""

'''if - else -  elif examples'''

#if examples
number = 7

# if number > 5:
#     print('We are learning python basic')
    
'''How to use not operator with if'''
# either True or False- if th eexpression if is false then it will run

# if not number > 11:
#     print('We are learning python basic')
    
'''How to use nested if '''

def find_out_about_number(number):
    if number > 7:
        print('Number is greater than 7')
        if number < 10:
            print('Number is less than 10')
            
# calling the function
#find_out_about_number(8)

# else examples

def find_out_about_number(number):
    if number > 7:
        print('Number is greater than 7')
    else:
        print('Check your number again!!')

# calling the function

#find_out_about_number(3)
#find_out_about_number(8)

#elif - else if examples

def find_out_about_number(num):
    if num > 10:
        print('Number is greater than 10')
    elif num < 15:
        print('Number is less than 15')
    else:
        print('Check your number please!!')

# calling the function
find_out_about_number()
