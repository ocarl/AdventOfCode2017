

def knot(lengths):
    myList = [i for i in range(256)]
    lengths = [ord(i) for i in lengths]
    [lengths.append(i) for i in [17, 31, 73, 47, 23]]
    currPos = 0
    skipSize = 0


    for i in range(64):
        for length in lengths:
            # reverse the sliced list
            revList = []
            for index in range(length):
                currIndex = (index + currPos) % len(myList)
                revList.append(myList[currIndex])
            revList = revList[::-1]

            # insert into original list
            for index, num in enumerate(revList):
                circIndex = (currPos+index) % (len(myList))
                myList[circIndex] = num

            #increment for next loop
            currPos += (length + skipSize)
            currPos %= len(myList)
            skipSize += 1
            skipSize %= len(myList)

    outString = denseMaker(myList, 16)

    return outString

def denseMaker(someList, divisionLength):
    outString = ''
    for i in range(int(256/divisionLength)):
        subList = someList[i*divisionLength:(i+1)*divisionLength]
        num = xor16(subList)
        hexRep = hexit(num)
        outString += hexRep
    return outString

def xor16(aList):
    dense = aList[0]
    for x in aList[1:16]:
        dense = dense ^ x
    return dense

def hexit(num):
    return hex(num)[2:] if len(hex(num)) > 3 else '0' + hex(num)[2:]

assert xor16([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64

assert hexit(64) == "40"
assert hexit(7) == "07"
assert hexit(255) == "ff"


assert knot('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

lengths = """130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"""

print(knot(lengths))
