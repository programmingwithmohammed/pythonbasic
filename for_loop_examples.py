# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:40:11 2021

@author: mjach
"""

'''For look examples'''

my_fruits_list = ['apple', 'orange', 'banana', 'watermelon']

#checking is the fruit in my list
print('Is this fruit in my list?:', 'apple' in my_fruits_list)

'''for loop example'''
# for fruit in my_fruits_list:
#     print(f'Fruit name is :{fruit}')
    
'''how to use range() function in for loop - 
here range 0 is inclusive I mean 0 will print it will start from 0
and 4 is exclusive I mean 4 will not print, it will stop to number 3
'''

# for number in range(11):
#     print(f'Number is : {number}')
    
'''How to print specific number within range
we can specify start and end.
here number 1 is inclusiveand
number 10 is exclusive
'''
# for number in range(1, 10):
#     print(f'Here number will print from 1 to 9: {number}')
    
'''range() function another use
specify start, end, increment
'''

# for number in range(2, 20, 2):
#     print(f'Number is :{number}')
    
'''How to print out the index of the items
we can use buit in function enumerate
'''

# for index, fruit in enumerate(my_fruits_list):
#     print(f'Fruit :{fruit} is at index no : {index}')
    
'''how to use for loop in dictionary'''

my_fruit_dict= {1:'apple', 2:'orange', 3:'banana', 4:'watermelon'}

# for fruit in my_fruit_dict:
#     print(f'That will return only keys of the dict.: {fruit}')
    
for keys, values in my_fruit_dict.items():
    print(f'Fruit :{values} is at {keys} ')