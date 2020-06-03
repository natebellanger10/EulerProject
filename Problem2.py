"""Add all even Fib numbers below 4,000,000"""

def fib(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
       return fib(n-1)+fib(n-2)

n=1
countList = []



while fib(n) < 4000000:
    j=fib(n)
    if j%2==0:
        countList.append(j)
    n+=1

counter=0
for i in countList:
    counter+=i

print(counter)