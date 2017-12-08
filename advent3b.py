def spiral(myNum):
    N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
    NE, SW, NW, SE = (1, -1), (-1, 1), (-1, -1), (1, 1)  # directions
    turn_left = {N: W, E: N, S: E, W: S}  # old -> new direction
    allDirs = N, S, W, E, NE, SW, NW, SE

    width, height = 25, 25
    x, y = width // 2, height // 2
    dx, dy = S # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 1
    matrix[y][x] = 1
    while count < 500:
        count += 1
        # try to turn left
        new_dx, new_dy = turn_left[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        print(new_x,new_y)

        valToAdd = 0

        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            print(x,y,'turning',dx,dy)
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy

        else: # try to move straight
            print(x,y,'straight')
            x, y = x + dx, y + dy

        #try to add numbers around
        for xdir, ydir in allDirs:
            if matrix[y+ydir][x+xdir] is not None:
                valToAdd = valToAdd + matrix[y+ydir][x+xdir]

        matrix[y][x] = valToAdd

        if valToAdd > myNum:
            nextNum = valToAdd
            break

    return nextNum


myNum = 277678

nextNum = spiral(myNum)

print(nextNum)


