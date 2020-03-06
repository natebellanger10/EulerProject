Fib = [1,1]
i = 2
while i < 10000:
    new = Fib[i-1]+ Fib[i-2]
    i+=1
    if len(str(new)) == 1000:
        break
    else:
        Fib.append(new)
       
print(i)