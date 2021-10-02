# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:43:05 2021

@author: mjach
"""

'''AND, OR, NOT examples'''

# and examples
#if both are true then and expression will be true 

answer_one = True
answer_two = True
#print('True or False :', answer_one and answer_two)

#if one the variable is false answer will be false
answer_one = False
answer_two = True
#print('\nTrue or False :', answer_one and answer_two)

#or operator example
#if one of the varaible is True answer will be true
answer_one = True
answer_two = True
#print('\nTrue or False :', answer_one or answer_two)

answer_one = False
answer_two = True
#print('\nTrue or False :', answer_one or answer_two)

#if both false the result will be false
answer_one = False
answer_two = False
#print('\nTrue or False :', answer_one or answer_two)

#not operator examples
# not represent reverse in boolen
# if its true will return false, and if it is false will return false
answer_one = True
print('\nTrue or False :', not answer_one)

answer_one = False
print('\nTrue or False :', not answer_one)
