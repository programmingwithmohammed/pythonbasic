# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 02:30:03 2021

@author: mjach
"""

'''How to create empty set'''

my_set = set()
#print('What type is it?:', type(my_set))

'''how to create set with items'''
my_set = {}
#print('What type is it?:', type(my_set))

my_set = {1,2,3,6}
#print('What type is it?:', type(my_set))
#print('Item within sets:', my_set)

'''Finding the length of the set'''
#print('Length of the set is:', len(my_set))

'''Set will not allowd duplicate items'''
#creating new sets

my_fruit_set = {'apple', 'orange', 'apple'}
#print('What is in my fruit set?:', my_fruit_set)

'''How to convert list to sets'''

my_fruit_list = ['apple', 'orange', 'cherry', 'watermelon', 'apple', 'orange']
#print('Checking list itms:',my_fruit_list)

# converting list to set

fruit_list_to_set=set(my_fruit_list)
#print('Checking my fruit list now:', fruit_list_to_set)

'''set can not keep the items in order
because of that we can not access set items by the index number
'''
#print(fruit_list_to_set[0])

'''set does not support sorted either
but if you want to sort same type item you can first convert set to list
or use the built in function sorted() function
'''
#print('Testing set to sort:', sorted(fruit_list_to_set))

'''Adding item in the sets'''

my_fruit_set.add('plum')
print('Updated sets now:',my_fruit_set)

'''How to delete or remove or discard item from the sets'''

my_fruit_set.discard('apple')
print('Updated sets now:', my_fruit_set)

#to check discard function where items not available
my_fruit_set.discard('watermelon')
print('Updated sets now:',my_fruit_set)

# to check remove function

#my_fruit_set.remove('watermelon')
# my_fruit_set.remove('plum')
# print('Updated sets now:',my_fruit_set)

'''how to update a sets'''

# programming_languages = {'python', 'java', 'c++'}
# rate_languages = {'5*', '4*', '3*'}

#programming_languages.update(rate_languages)

#print('After update the sets :', programming_languages)

#never use string to update a sets.

#programming_languages.update('spyder')
#print('After update the sets :', programming_languages)

'''how to use sets operations'''

#creating to sets

fruit_set = {'apple', 'orange', 'watermelon', 'plum', 'banana'}
favorite_fruits = {'watermelon', 'mango', 'grape', 'dates', 'banana'}

# example of sets operations
# union
print('Union example :', fruit_set | favorite_fruits)

# intersection
print('Intersection example :', fruit_set & favorite_fruits)

# difference
print('Difference example :', fruit_set ^ favorite_fruits)



