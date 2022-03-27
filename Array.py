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
  
