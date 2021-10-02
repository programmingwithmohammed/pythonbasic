# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 03:31:58 2021

@author: mjach
"""

'''Comparisions example with numbers '''

# > greater than sign
# >= greater than equal to sign
# < less than sign
# <= less than equal to sign

# print('100 < 200 =', 100 < 200)
# print('100 <= 100 =', 100 <= 100)
# print('100 < 50 =', 100 < 50)
# print('100 <= 90 =', 100 <= 90)

# print('\n') # to get a new line

# print('200 > 100 =', 200 > 100)
# print('200 >= 200 =', 200 >= 200)
# print('200 > 500 =', 200 > 500)
# print('200 >= 500 =', 200 >= 500)

# print('-20 is greater than 20 ?:', -20 > 20)

'''
Equality
Comparisions example with equals(==) and not equals(!=)
will return boolen result either True or False
'''

answer_one = 1
answer_two = 1

#print('True or False:',answer_one == answer_two)

answer_one = 5
answer_two = 1
#print('True or False:',answer_one != answer_two)

answer_one = 'apple'
answer_two = 'apple'

# print('True or False:',answer_one == answer_two)
# print('True or False:',answer_one != answer_two)

'''Identity check
is or is not key words. (is) is similiar to == and (is not) is similiar to !=
'''
fruit_list_one = ['apple', 'banana'] 
fruit_list_two = ['apple', 'banana']

#checking for equality

#print(fruit_list_one == fruit_list_two) # will give true or false result

#checking for identity
# both list has different memory address so when checking for identy 
# it will give false result because both list has different memory address.

#print(fruit_list_one is fruit_list_two) # will give true or false result

'''
is and is not checking for built in types like None, True and False
'''

one = True

print('One is True :',one is True)

two = False
print('Two is fasle:',two is False)
print('Two is not true:', two is not False )