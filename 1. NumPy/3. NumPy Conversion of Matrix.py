import numpy as np

arr_arange = np.arange(1,13) # np.arange(start, stop, step)
print(arr_arange)

arr_linespace = np.linspace(1, 10,5)
print(arr_linespace)

arr_reshape2d = arr_arange.reshape((3,4))
print(arr_reshape2d)

arr_reshape3d = arr_arange.reshape((2,3,2))
print(arr_reshape3d)

# ravel() use to convert 2d Array into 1d
arr_ravel = arr_reshape2d.ravel()
print(arr_ravel)

# flatten() use to convert multi dimension array into 1d
arr_flatten = arr_reshape3d.flatten()
print(arr_flatten)

# transpose() use to convert raw to coulmn and coulmn to raw
arr_transpose = arr_reshape2d.transpose()
print(arr_transpose)
# You can also use .T to perform the same opration as transpose()
arr_transpose = arr_reshape2d.T
print(arr_transpose)