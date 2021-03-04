#Euler problem 52, It can be seen that the number, 125874,
#and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


i = 995806754
print(list(str(i)))

from collections import Counter as C

def checker (a, b, C):
    if C(str(a)) == C(str(b)):
        return True
    else:
        return False


counter = 1

while True:
    if checker(counter, counter*2, C) and checker(counter, counter*3, C) and checker(counter, counter*4, C) and checker(counter, counter*5, C) and checker(counter, counter*6, C):
        print(counter)
        break
    else:
        counter +=1



            
