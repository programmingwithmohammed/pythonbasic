# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 00:52:42 2021

@author: mjach
"""

'''how to create dict.'''
my_dict = {} # empty dict
another_way_dict = dict() # empty dict

# print('What type is it?', type(my_dict))
# print('\nWhat type is it?', type(another_way_dict))

'''how to create dict with items'''

my_dict_with_items = {1: 'apple', 2: 'banana', 3: 'orange'}

'''how to find out length of the dict'''

#print('\nlength of the dict:', len(my_dict_with_items))

'''how to find out key is exits or not'''

# print('\nTo find out key exits or not:', 5 in my_dict_with_items)
# print('\nTo find out key exits or not:', 1 in my_dict_with_items)

'''how to find out value by the key'''

# print('\nTo find out the value:', my_dict_with_items[2])
# #print('\nTo find out the value:', my_dict_with_items[4]) # will throw key error
# print('\nTo find out the value:', my_dict_with_items.get(4)) # will not throw error but rather it will give none

'''how to get all the keys and values'''
print('\nTo get all the keys and values from dict.:', my_dict_with_items.items())

'''how to get only keys from the dict'''

print('\nTo get all the keys only from dict.:', my_dict_with_items.keys())

'''how to get only values from the dict'''

print('\nTo get all the keys only from dict.:', my_dict_with_items.values())

'''how to add new items in the dict'''

my_dict_with_items[6] = 'watermelon' # key value pairs
print('\nTo add new items in the dict',my_dict_with_items.items())

'''how to add or update two dict togather'''

new_dict = {7: 'cucumber', 8: 'carrot'}

my_dict_with_items.update(new_dict)
print('\nUpdated dict now :', my_dict_with_items)
