# check whether a color is present in list and student from tuple

list=['red','black','green','orande']
tuple=('ramu','priya','bhanu','rocky')

color=input('enter color:')
if(color in list):
    print('color is present..')
else:
    print('failed..')

student=input('enter student name:')
if(student in tuple):
    print('student is present..')
else:
    print('failed..')