import numpy as np

str1 = "I am Rahul Gaur"
str2 = "I am a good boy"

print(np.char.add(str1,str2))
print(np.char.lower(str1))
print(np.char.upper(str2))
print(np.char.center(str1,100,fillchar="*"))
print(np.char.split(str1))
print(np.char.splitlines("Rahul\nGaur"))
print(np.char.join("-","RAHUL"))
print(np.char.replace("Aam","A","R"))
print(np.char.equal(str1,str2))
print(np.char.count(str1,"a"))
print(np.char.find(str1,"Rahul"))