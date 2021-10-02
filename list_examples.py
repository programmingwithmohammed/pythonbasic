# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:57:01 2021

@author: mjach
"""

'''Creating empty list examples'''

# my_list = []
# print('Example one :',type(my_list)) # type is built in function to check the type

# #or
# my_list_example = list()
# print('Example two :',type(list()))

'''creating list with items
if you forget to put comma between the list items you will get syntax error'''

my_list_with_int_items = [1, 2, 3, 4] # int value
my_list_with_string_items = ['a', 'b', 'c', 'd'] # string items

# '''printing the list items'''
# print('List int items: ',my_list_with_int_items)
# print('List string items:', my_list_with_string_items)

'''Finding the length of the list'''

print('List length :', len(my_list_with_int_items))

'''How to access list items
to access a list items we use index. python list index start at 0'''

my_fruit_list = ['apple', 'banana', 'orange', 'cherry']

'''finding the items from the list with the index no'''

print('Finding the specific items in the list:', my_fruit_list[3])
#will give error message list is out of index
print('Finding the specific items in the list:', my_fruit_list[5])

'''How to update a list item'''

my_fruit_list[3] = 'watermelon'
print('Uptodate my frit list now:', my_fruit_list)

'''we can create a valid list without a coma, but more readable option is 
to put comma. see the difference. if you forget the bracket of the list 
you will get the syntax error.'''

my_new_list = ['a' 'b' 'c' 'd']
print('My new list :', my_new_list)

my_list_without_closing_bracket = [1,2] #will get the syntax error