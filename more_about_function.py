# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 01:48:42 2021

@author: mjach
"""

# example of function with arguments
def greeting(name, greeting):
    print(f'{name}, {greeting}')

greeting('Mohammed', 'Good Morning !!')

#example of default value passing with a argument  
def greeting_with_default_value(name = 'Mohammed', greeting= 'Good Night'):
    print(f'{name}, {greeting}')

#calling function    
greeting_with_default_value()

#exmple of getting error when function not getting required positional argument.
def greeting(name, greeting):
    print(f'{name}')

#calliong function
greeting('Mohammed')
 
# variable scopes in python
def python_version_info():
    python_version = '3.9'
    print(f'Python version info inside the function : {python_version}')

# calling the function
python_version_info()

# example of getting error using function variable
# outside the function

#print(f'Python version info outside the function : {python_version}')