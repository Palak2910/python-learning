#create a array 
arr = [10,20,30,40,50]
print(arr)

#2D array
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)

#3D array
b = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(b)

#array attributes
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.ndim) #number of dimensions

print(a.shape) #shape of the array

print(a.size) #number of elements in the array

print(a.dtype) #data type of the array elements