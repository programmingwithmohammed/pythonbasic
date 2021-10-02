# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:39:53 2021

@author: mjach
"""
'''
how to write in a file with write() and writelines() function
'''
# with open('writing_my_file.txt', 'w') as my_writing_file:
#     #writing_file = my_writing_file.writelines('we are learning python basic.')
#     writing_file = my_writing_file.write('we are learning python basic and how to writing to a file.')
#     my_writing_file.close()

'''
how to append in a file with write() and writelines() function
'''
with open('writing_my_file.txt', 'a') as my_writing_file:
    #writing_file = my_writing_file.writelines('\nwe are learning python basic.')
    writing_file = my_writing_file.write('\nwe are learning python basic and how to writing to a file.')
    my_writing_file.close()