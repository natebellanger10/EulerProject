'''smallest number divisible by 1 to 20'''

counter = 20
#divisor = 0
listDivisor = list(range(2,20))
running = False

while running == False:
    for i in listDivisor:
        if counter % i == 0:
            running = True
        else:
            counter+=1

