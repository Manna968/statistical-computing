def triangle(x):
    if (x < 0 or not isinstance(x, int)):
        return ('Invalid input')
    row = 1
    y = 1
    while(row <= x):
        col = 1
        while(col <= row):
            print(y, end = " ")
            col = col + 1
            y = y + 1
        row = row + 1
        print()

triangle(3)
triangle(6)

