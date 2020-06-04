'''smallest number divisible by 1 to 20'''

def does_it_divide(n):
    for i in [11,13,14,15,16,17,18,19,20]:
      if n % i != 0:
            return False
    return True


counter = 2522

while True:
    if does_it_divide(counter):
        break
    counter+=1

print(counter)