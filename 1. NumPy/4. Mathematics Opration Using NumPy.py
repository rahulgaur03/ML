import numpy as np

arr1 = np.arange(1,10).reshape((3,3))
arr2 = np.arange(1,10).reshape((3,3))
print(arr1,arr2,sep="\n")
print(arr1+arr2)  # np.add(arr1,arr2)
print(arr1-arr2)  # np.subtract(arr1,arr2)
print(arr1*arr2)  # np.multiply(arr1,arr2)
print(arr1/arr2)  # np.divide(arr1,arr2)
print(arr1@arr2)  # arr1.dot(arr2)
print(arr1.max()) # To get the maximum value in array
print(arr1.argmax()) # Top get the index of max value
print(arr1.max(axis = 0)) # To get the maximum value in all column
print(arr1.max(axis = 1)) # To get the maximum value in all raws
# As same as we have min function for the performing the min vlaue oprations
print(np.sum(arr1)) # To get sum of all number present in array
print(np.sum(arr1, axis = 0)) # To get sum of column
print(np.sum(arr1, axis = 1)) # To get sum of raw
print(np.mean(arr1)) # To get the mean value of matrix
print(np.sqrt(arr1)) # To get sqrt of every element of matrix
print(np.std(arr1)) # To get standard division or matrix
print(np.exp(arr1))
print(np.log(arr1))
print(np.log10(arr1))
