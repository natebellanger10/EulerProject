"""Find the largest palindrome made from product of two 3 digit #'s"""

n=100
m=100
prod = 0 
largest = 0

while m < 999:
    while n < 999:
        prod = m * n
        if str(prod) == str(prod)[::-1] and prod > largest:
            largest = prod
        n+=1
    n=100
    m+=1

print(largest)