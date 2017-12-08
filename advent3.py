import math
import numpy as np


def findClosestTopNum(myNum):
    mySqr = math.sqrt(myNum)
    while mySqr - math.floor(mySqr) > 0 or myNum % 2 != 1:
        myNum += 1
        mySqr = math.sqrt(myNum)
    return myNum


def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = S # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

def moveFromSide(startIndex, steps):
    if startIndex[1] == 0:
        currIndex = [startIndex[0], startIndex[1] + 1]
        steps += 1
    elif startIndex[1] == side - 1:
        currIndex = [startIndex[0], startIndex[1] - 1]
        steps += 1
    elif startIndex[0] == 0:
        currIndex = [startIndex[0] + 1, startIndex[1]]
        steps += 1
    elif startIndex[0] == side - 1:
        currIndex = [startIndex[0] - 1, startIndex[1]]
        steps += 1
    else:
        currIndex = startIndex
    return currIndex, steps

def move(spirMatrix, currIndex):
    print(currIndex)
    currVal = spirMatrix[currIndex[0], currIndex[1]]



    if spirMatrix[currIndex[0]+1, currIndex[1]] < currVal:
        currIndex = [currIndex[0]+1, currIndex[1]]
    elif spirMatrix[currIndex[0]-1, currIndex[1]] < currVal:
        currIndex = [currIndex[0]-1, currIndex[1]]
    elif spirMatrix[currIndex[0], currIndex[1]+1] < currVal:
        currIndex = [currIndex[0], currIndex[1]+1]
    elif spirMatrix[currIndex[0], currIndex[1]-1] < currVal:
        currIndex = [currIndex[0], currIndex[1]-1]

    return currIndex

myNum = 277678

topNum = findClosestTopNum(myNum)

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {N: W, E: N, S: E, W: S} # old -> new direction


side = int(math.sqrt(topNum))

spirMatrix = np.asarray(spiral(side, side))

startIndex = np.argwhere(spirMatrix == myNum)[0]

print_matrix(spirMatrix)

currIndex = []

steps = 0

currIndex, steps = moveFromSide(startIndex,steps)
currIndex, steps = moveFromSide(currIndex,steps)

currVal = spirMatrix[currIndex[0], currIndex[1]]

while currVal != 1:
    currIndex = move(spirMatrix, currIndex)
    currVal = spirMatrix[currIndex[0], currIndex[1]]
    steps += 1


print(currIndex, steps)

