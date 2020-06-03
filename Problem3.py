''' What is the largest prim factor of 600851475143'''

import sympy
from math import sqrt

counter = 1
largest = 0
bigNum = 600851475143


while counter < sqrt(bigNum):
    if bigNum % counter == 0:
        if sympy.isprime(counter) == True:
            largest = counter    
    counter+=1

print(largest)