import numpy as np

matrix1 = np.ones(5)
print(matrix1)

matrix2 = np.ones((4,5)) # It will give matrix with float no.
print(matrix2)

matrix_int_with_ones = np.ones((2,3),dtype=int)
print(matrix_int_with_ones)

matrix_int_with_zeros = np.zeros((2,3),dtype=int)
print(matrix_int_with_zeros)

matrix_bool_with_zeros = np.zeros((2,3),dtype=bool)
print(matrix_bool_with_zeros)

matrix_str_with_zeros = np.zeros((2,3),dtype=str)
print(matrix_str_with_zeros)

matrix_empty = np.empty((3,3))
print(matrix_empty)