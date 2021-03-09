'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''


f = open('p042_words.txt', 'r')

wordList = f.read().split(',')



triangleNums = []
n = 1
while n < 1000:
    triangleNums.append(0.5*n*(n+1))
    n+=1




final = 0
for word in wordList:
    word = word.replace('"', '') #list has extra quotes on each string
    counter = 0
    for letter in word:
        counter += (ord(letter)-64)  #moving from A = 65 is ASCII to A = 1
    if counter in triangleNums:  #check if number is triangle
        final +=1


print(final)
    



