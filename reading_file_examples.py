# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:57:00 2021

@author: mjach
"""

'''files character meaning in python'''

'''
'r' - open for reading its is default
'w' - open for writing, but delete the first one
'x' - open for new one creation, but fail it the file already exits
'a' - open for writing and adding more contents at the end if the file exits
'b' - open the file in binary mode
't' - open the file in text mode
'+' - open a file from disk for updating either reading or writing
'''
## always make sure file is closed
## the below examples are base on the current working directory

'''
#1. reading a jason file from same directory
'''
# my_file = open('sample1.json', 'r')
# fruit = my_file.read()
# print(fruit) # read and print entire file contents
# my_file.close()

'''
#2. reading a text file example from same directory
'''

# my_file = open('reading_my_file.txt', 'r')
# print(my_file.read())
# my_file.close()

'''
#3. reading a text file example from same directory
# with this its work like a try...catch ...finally
# it will close the file automatically
'''
# with open('reading_my_file.txt', 'r' ) as my_file:
#     #fruit = my_file.read()
#     print(my_file.read())

'''
#4. reading a text file example from same directory
'''
file = open('reading_my_file.txt')
#print(file.readline())# read only one line
#print(file.readline(2))# read only specific character from a line
#print(file.readlines())# reading all the lines and return as a list
#file.close()

'''
#5. reading a text file example from same directory
#iterting or going through each line of the text file with a while loop
'''
# with open('reading_my_file.txt', 'r') as my_file:
#     line = my_file.readline()
#     while line != '': # '' means empty string
#         print(line, end='')
#         line = my_file.readline()

'''
#6. reading a text file example iterating through for loop
# recommend option
'''
# with open('reading_my_file.txt','r') as my_file:
#     for line in my_file.readlines():
#         print(line, end='')

'''more simplified options'''

with open('reading_my_file.txt','r') as my_file:
    for line in my_file:
        print(line, end='')
    
 