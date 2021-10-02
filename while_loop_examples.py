# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:08:55 2021

@author: mjach
"""

'''while loop examples'''

number = 0

max_number = 5

while number <= max_number:
    print(f'the number is {number}')
    # if you do not update the number then it will run forever.
    number += 1
    #number = number + 1