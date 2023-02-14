import numpy as np

mat1 = np.arange(1,17).reshape(4,4)
mat2 = np.arange(17,33).reshape(4,4)
print(mat1)
print(mat2)
print(mat1+mat2)

# CONCATENATION
print("\nCONCATENATION\n")
print(np.concatenate((mat1,mat2))) # Concatenate matrix by column
print(np.concatenate((mat1,mat2),axis =1)) # Concatenate matrix by column
# Also we can use some other method to do the same 
print(np.vstack((mat1,mat2))) # Concatenate matrix by column
print(np.hstack((mat1,mat2)))  # Concatenate matrix by column
print(np.hstack((mat1,mat2,mat1))) # So you can concatenate two or more matrix

# SPLITING
print("\nSPLITING\n")
print(np.split(mat1,2)) # Split matrix horizontally
print(np.split(mat1,2,axis=1)) # Split matrix vertically

arr = np.arange(1,10)
print(np.split(arr,[2,5])) # Split array into multiple part 