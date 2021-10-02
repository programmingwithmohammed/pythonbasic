# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:08:16 2021

@author: mjach
"""

'''How to create one item and empty tuple'''

my_tuple = ()
print('To see what type it is :', type(my_tuple))

'''please make sure if you create one item tuple
must be added one comma at the end other wise it will not work'''

my_tuple_with_one_item = (1,)
print('To find out what type is it:',type(my_tuple_with_one_item))

'''creating tuple with multiple items'''

student_result_details = ('Hasan','Math', 80, 'geography', 90, 'science', 95, 'total', 265 )
print('Student result details :', student_result_details)

'''How to access tuple items. if index is too big compare to tuple index size
then it will give error message. tuple index out of range
'''
print('Item access by the index number :', student_result_details[0])

'''Assinging tuple items- unpacking'''

studentName,subjectMath, mathMarks, subjectGegraphy, geographyMarks, subjectScience, scienceMarks , total, totalMarks = student_result_details

print('Studnet subject result grade :', studentName, totalMarks)

'''But we can not assign new item as we can not change them  '''
#we will get a type error 'tuple' object does not support item assignment

student_result_details[0] = 'English'