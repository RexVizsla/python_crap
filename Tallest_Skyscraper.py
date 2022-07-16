skyline = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]
]

y_count = 0
for y in skyline:
    x_count = 0
    y_count = y_count + 1
    for x in y:
        x_count = x_count + 1
        if x:
            print("Tallest building found at x = " + str(x_count) + " and y = " + str(y_count))
            exit()