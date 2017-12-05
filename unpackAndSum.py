def compileOutput(out: "string to be added to", keys: "string to add", mySym: "integer to add") -> str:
    return out + keys[:-1] + ': ' + str(mySym) + ', '

mainList = [[('a', 2), ('b', 4), ('c', 3)], [('x', 1), ('y', 2), ('z', 3)]]

output = ''

for subList in mainList:
    mySum = 0
    key = ''
    for it in subList:
        key = key + it[0] + ' '
        mySum = mySum + it[1]
    output = compileOutput(output, key, mySum)

print(output[:-2])
