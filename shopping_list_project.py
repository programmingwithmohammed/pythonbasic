# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:52:38 2021

@author: mjach
"""

'''
Shopping List Project
1. Create a shopping list - items add
2. Iteam view from the shopping list
3. Delete shopping items from the list.
4. Writing to the file all the shopping items.
5. Exit from the program
'''
import sys
def mainMenu():
    print('\t\t----Shopping List----')
    print('\t\t---------------------')
    print('Please select an options:\n')
    print('(a)dd an item.')
    print('(v)iew the list.')
    print('(d)elete an item.')
    print('(e)xit the program.')
    
    user_choice = input('Please select an option: ')
    
    if len(user_choice) > 0:
        if user_choice.lower()[0] == 'a':
            print('add later')
        elif user_choice.lower()[0] == 'v':
            print('add later')
        elif user_choice.lower()[0] == 'd':
            print('add later')
        elif user_choice.lower()[0] == 'e':
            sys.exit()
        else:
            mainMenu()
    else:
        mainMenu()
 
mainMenu()