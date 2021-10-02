# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 02:10:55 2021

@author: mjach
"""

'''Boolean Logic True or False'''

'''
- 0(zero) is false rest is true even negative numbers
- empty data structures like list, sets, dict. and tuple are False
- List, sets, tupe and dict. with items within are True
- None is also False
'''
#Example

# print('10 > 5 is it true?:', 10 > 5 )

# '''To find out quickly either it is true or false use bool'''

# print('\nNone is true or false?:', bool(None))
# print(bool(10 > 5))
# print(bool(10 < 5))
# print(bool(-1)) # to check negative number true or false
# print(bool(0))# to check 0 zero true or flase

'''Empty string are also False'''

# print(bool('Salam')) # with string true
# print(bool('')) # empty string false

'''Empty list, sets, tuple and dict false'''
#list

# print('\nEmpty list:',bool(list()))
# print('Empty list:',bool([]))
# print('list with items:',bool([1]))

#sets

# print('\nEmpty sets:',bool(set()))
# print('Sets with items:',bool({1}))

#tuple

print('\nEmpty tuple:',bool(()))
print('Tuple with items:',bool(1,))

#dictionary

print('\nEmpty dict:',bool(dict()))
print('Empty dict:',bool({}))
print('Dict with items:',bool({1:'apple'}))