'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

'''


a = '0.'
count = 1


while len(a) < 1000020:
    a += str(count)
    count +=1
    

print(int(a[2]) * int(a[11]) * int(a[101]) * int(a[1001]) * int(a[10001]) * int(a[100001]) * int(a[1000001]))



