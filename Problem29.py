sequence = []
a=2
b=2

while a < 101:
    while b < 101:
        n = a**b 
        if n not in sequence:
            sequence.append(n)
        b+=1
    b=2
    a+=1
    
    
print(len(sequence))