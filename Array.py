''' Python Array Modules '''

import array
int_array = array.array('i',[1,2,3,4,5,6]) #Creating array int array
float_array = array.array('f',[1.0,1.1,1.2,1.3,1.4,1.5]) # Creating float float array
print(int_array) #Print array
print(float_array)

'''We can print array elements using for elements '''

import array

int_arrary = array.array('i',[1,2,3,4,5,6])
for a in int_array:
  print(a)
  

  '''Insert elements ''' 
import array
int_array = array.array('i'[1,2,3,4,5,6])
int_array.insert(0,1)
int_array.insert(1,2)
int_array.insert(2,3)
print(int_array)

  
''' Python array supports negative index ''' 
import array
int_array = array.array('i'[1,2,3,4])
int_array.insert(-1)
int_array.insert(-2)
print(int_array)


'''Remove elements'''

import array
int_array = array.array('i',[12,13,21,22])
try:
  int_array.remove(20)
except ValueError as ve:
  print(ve)
  

  ''' Slicing an Array'''
  import array
  int_array = array.array('i',[12,13,14,15,16,17])
  print(int_array[3:])
  print(int_array[1:])
  
  


