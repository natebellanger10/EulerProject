#145! = 1! + 4! + 5!
#find the sum of all #'s which are equal to the factorial of their digits
#1! and 2! arent included
import math


final=[]
digits = []
def listview(a):
    digits = [int(a) for a in str(a)]
    return digits
    
    
def Factor(digits,a):
    total=0
    for i in digits:
        total += math.factorial(i)
    if total == a:
        final.append(total)

count = 3
while count < 100000:
    passingList = listview(count)
    Factor(passingList,count)
    count +=1
    
finalsum=0
for item in final:
    finalsum+=item
    
print(finalsum)