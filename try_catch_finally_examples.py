# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 00:40:22 2021

@author: mjach
"""
'''
example 1
'''

# with open('reading_myy_file.txt','r') as my_reading_file:
#         read_file = my_reading_file.read()
#         print(read_file)

'''
example 2
'''
# try:
#     with open('reading_my_file.txt','r') as my_reading_file:
#         read_file = my_reading_file.read()
#         print(read_file)
# except:
#     print('File not found error')
    
'''
example 3
'''
# try:
#     with open('reading_myy_file.txt','r') as my_reading_file:
#         read_file = my_reading_file.read()
#         print(read_file)
# except FileNotFoundError as file_error:
#     print(file_error)

'''
example 4
'''
# try:
#     with open('reading_myy_file.txt','r') as my_reading_file:
#         read_file = my_reading_file.read()
#         print(read_file)
# except FileNotFoundError as file_error:
#     print(file_error)
# finally:
#     print('This part will run, no amtter what happen up.')    

'''
we can use as many as except to catch the error also we can use else--
within else block we can use try catch block
'''

#try:
    #some code
#except:
    #some code
#else:
    #try:
        #some code
    #except:
        #some code
#finally:
    #some code