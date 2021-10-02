# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:19:51 2021

@author: mjach
"""

'''how to use break examples'''

fruit_list = ['apple', 'banana', 'orange', 'watermelon']

# for fruit in fruit_list:
#     print(f'The fruit name is :{fruit}')
#     if fruit == 'orange':
#         break

'''How to do break in while loop'''   
# fruit = 'orange'
# while True:
#     if fruit in fruit_list:
#         print(f'The fruit is found: {fruit}')
#         break
    
'''How to do break in while loop'''   
counter = 0
while True:
    counter = counter + 1
    if counter == 20:
        print(f'Count has been done to : {counter}')
        break