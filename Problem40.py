count = 1 
countList = []
while count <= 1000000:
    countList.append(count)
    count +=1

final = countList[1]*countList[10]*countList[100]*countList[1000]*countList[10000]*countList[100000]*countList[1000000]
print(final)