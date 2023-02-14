import numpy as np

mat = np.arange(1,101).reshape(10,10)
print(mat[0,0]) # To get the value from particular index in matrix
print(mat[0,0].ndim) # To check the dimension of the value
print(mat[0]) # To get the row
print(mat[:,0]) # To get the column
print(mat[:,0:1]) # To get the column in two dimension format
print(mat[1:4,1:4])
print(mat[:,2:4])
print(mat.itemsize) # To get the size of any value
print(mat.dtype)  # To get the datatype of matrix