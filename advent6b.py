from collections import defaultdict
from itertools import count

ddict = defaultdict(lambda: 0)

def generateKey(myList):
    s = ''
    for c in myList:
        s += str(c)
    return s

def findMaxIndex(myList):
    return myList.index(max(myList))

def divideEvenly(myList, index):
    bank, myList[index] = myList[index], 0
    i = count(index+1)
    while bank > 0:
        currInd = i.__next__() % (len(myList))
        myList[currInd] += 1
        bank -= 1
    return myList

indata = """14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"""
myList = [int(i) for i in indata.split('\t')]

myList = [14, 13, 12, 11, 9, 8, 8, 6, 6, 4, 4, 3, 1, 1, 0, 12]

steps = 0

key = generateKey(myList)

while ddict[key] == 0:
    ddict[key] += 1
    steps += 1
    maxIndex = findMaxIndex(myList)
    myList = divideEvenly(myList, maxIndex)
    key = generateKey(myList)

print(myList, steps)

