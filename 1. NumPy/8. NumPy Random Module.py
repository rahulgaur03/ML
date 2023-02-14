import numpy as np
import random

print(np.random.random(5))
print(np.random.random((3,3)))
print(np.random.randint(1,11)) # To get the random value between range
print(np.random.randint(1,11,(4,4))) # To get the 2D Array with random value
# So you can genrate Nd Array using rand function

np.random.seed(10)
print(np.random.randint(1,11,(4,4,4)))
# np.random.seed(10)
# print(np.random.randint(1,11,(4,4,4)))
# So if you always want the same random value so you can use seed function

print(np.random.rand(3,3))
print(np.random.randn(3,3))

x = [1,2,3,4]
print(np.random.choice(x)) # It will choose random number from you given list
print(np.random.permutation(x))