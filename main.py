# Sign-Magnitude Floating-Point to Fixed-Point Converter
# Developed by Mehdi0xC, Fall 2019

# Specify total size of your fixed-point and size of fractions part
FP_Size = 22
FR_Size = 17

# Input to be converted
inp = -6.573

import numpy as np

result = np.zeros(shape=(1,32))

if (inp < 0):
	result[0, FP_Size-1] = 1
	inp = inp * -1

for i in range(FP_Size-FR_Size-2,-FR_Size-1,-1):
    if inp>2**i:
        result[0,FR_Size+i] =  1
        inp -= 2**i

temp = 0
for i in range(0,32,1):
    temp += (2**i)*result[0,i]

print("result in uint32:")
print(int(temp))

print("result in binary:")
print(np.flip(result))
