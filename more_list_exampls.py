# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 01:05:50 2021

@author: mjach
"""

'''Sort example'''

my_match_score = [175, 200, 193, 300, 122, 385]

#Original list
print('original my match score list :', my_match_score)

#Sorted list ascending order
print('Sorted my match score list ascending order:', sorted(my_match_score))

#Original list
print('original my match score list :', my_match_score)

# Descending order
print('Sorted my match score list descending order:', sorted(my_match_score, reverse=True))

#Original list
print('original my match score list :', my_match_score)

# reverse the list order
my_match_score.reverse()
print('original my match score list :', my_match_score)

#to find out the more function related to list
#help(list.)

'''Adding an item in he list'''
my_fruit_list = ['apple', 'apple', 'orange', 'cherry']
# print('Original my fruit list:', my_fruit_list)
my_fruit_list.append('watermelon')
# print('Updated My fruit list now :', my_fruit_list)

'''If you want add items in a specific position
then use insert function'''

my_fruit_list.insert(1,'plum')
print('Updated my fruit list now:', my_fruit_list)

'''Adding two list togather'''
fruit_color_list = ['pink', 'yellow', 'red', 'red', 'green', 'red']

my_fruit_list.extend(fruit_color_list)
print('Updated the list :', my_fruit_list)

'''Searhing item in the list'''

print('pink' in my_fruit_list)
print('white' in my_fruit_list)

print('Item searching by index number :', my_fruit_list[1])
#will print list is out of range
#print('Item searching by index number :', my_fruit_list[12])

'''TO find how many same number of the items in the list '''

print('Number of same items in the list:',my_fruit_list.count('apple'))

'''How to remove items from the list
remove() function will remove item from the list 
but we have to specify the item name. it take exectly one argument
if the item is not in the list then it will give error'''

print('Removing an item from the list:', my_fruit_list.remove('apple'))
print('Updated fruit list now:', my_fruit_list)

'''we can also use pop() function
that function will remove from the last item from the list
but if we give index number it can also delete that specific item
if yhe item we want to delete is not in the list then it will give error'''

print('Removing the last item from the list:',my_fruit_list.pop())
print('Removing the specific item from the list:',my_fruit_list.pop(1))
print('Updated fruit list now:', my_fruit_list)
