import numpy as np

arr_1d = np.array([1,2,3,4])
print(arr_1d)
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d,"\n")

print(arr_1d.ndim, type(arr_1d), arr_1d.size, arr_1d.shape , arr_1d.dtype)
print(arr_2d.ndim, type(arr_1d), arr_2d.size, arr_2d.shape , arr_2d.dtype)