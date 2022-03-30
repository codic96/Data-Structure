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
  
  '''Searching an element in the Array '''
  
  import array 
  int_array = array.array('i',[0,1,2,3,4,5,6])
  print(f' 1 is found at index {int_array.index(1)}')
  try:
    print(int_array.index(20))
 except valueError as ev:
    print(ev)
   
 
''' Updating value  at specific index ''' 
import array
int_array = array.array('i',[0,1,2,3,4,5])
print(int_array)
int_array[0] = -1
int_array[1] = -2
int_array[2] = -3
print(int_array)

try:
  int_array[10]=-10
except IndexError as ve:
  print(ve)

''' Reversing an Array '''

import array 
int_array = array.array('i',[0,1,2,3,4,5])
print(int_array)
print(int_array.reverse())

''' Count of the occurence of an element '''

import array 
int_array = array.array('i',[0,1,2,3,4,5])
print(int_array.count(1))
print(int_array.count(0))


''' Extending an array by Appending an Iterate '''

import array
int_array1 = array.array('i',[0,1,2,3,4,5])
int_array2 = array.array('i',[0,2,23,133,13])
int_array1.extend(int_array2)

''' Converting Array to List '''

import array 
int_array = array.array('i',[0,1,2,3,4,5,6,7])
print(int_array.toList())


  

  
  
  


