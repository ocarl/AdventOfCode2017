def myFunc(inp):
    myDict = {'a': 4, 'b': 3, 'c': 5}
    return myDict[inp]


inputs = 'a', 'b', 'c'
index = None
func = None
minVal = None

for ind, inp in enumerate(inputs):
    val = myFunc(inp)
    if minVal is None or val < minVal:
        index = ind
        func = inp
        minVal = val

print('Result: {}, Input: "{}", Index: {}'.format(minVal, func, index+1))
