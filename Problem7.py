'''Find the 10,001st prime'''
import sympy
counter = 0
i = 0
while counter <= 10001:
    if sympy.isprime(i):
        counter+=1
    if counter == 10001:
        break
    i+=1

print(i)
