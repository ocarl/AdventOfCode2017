myList = [i for i in range(256)]

# myList = [0,1,2,3,4]

currPos = 0
skipSize = 0
lengths = [130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224]

for length in lengths:
    revList = []
    for index in range(length):
        currIndex = (index + currPos) % len(myList)
        revList.append(myList[currIndex])
    revList = revList[::-1]
    for index, num in enumerate(revList):
        circIndex = (currPos+index) % (len(myList))
        myList[circIndex] = num
    currPos += length + skipSize
    skipSize += 1

print(myList[0]*myList[1])

