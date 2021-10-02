# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:38:51 2021

@author: mjach
"""
#simple function example
def my_function():
    print('Hi it is a function.')
    
#function example with arguments        
def function_with_arguments(greeting, name):
    print('Hi, %s, I wish you all the best %s'%(greeting, name))
    
# return function example   
def adding_two_numbers(a, b):
    return a + b
    
# calling the functions

my_function() # calling first function

function_with_arguments('Good morning', 'Mohammed')# calling function with the arguments

result_two_numbers = adding_two_numbers(5, 4)# calling function that return 

print(result_two_numbers) # print the result of the function 