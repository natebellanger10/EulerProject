"""Sum of all integers that are multiples of 5 and 3 under 100"""

n=1
multiples = []
while n<=999:
    if n%3==0 or n%5==0:
        multiples.append(n)
    n+=1

sum = 0
for i in multiples:
    sum += i
#print(multiples)
print(sum)
