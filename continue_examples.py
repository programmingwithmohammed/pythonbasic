# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:31:51 2021

@author: mjach
"""

'''Continue examples'''

fruit_list = ['apple', 'banana', 'orange', 'watermelon']

# for fruit in fruit_list:
#     if fruit == 'orange':
#         continue
#     print(f'The fruit name is :{fruit}')

    
'''continue and break togather examples'''
# for fruit in fruit_list:
#     if len(fruit) !=6:
#         continue
#     print(f'The fruit name is : {fruit}')
    
#     # if fruit == 'orange':
#     #     break

'''How to use return statement inside the loop'''

def find_fruit(fruit_name):
    for fruit in fruit_list:
        print(fruit)
        if fruit == 'orange':
            return f'we found out the fruit :{fruit}'

#calling the function
print(find_fruit(fruit_list))
    