for x in range(9):
    for y in range(1, 10):
        if x == y or x > y:
            continue
        if x == 8:
            print("{:d}{:d}".format(x, y))
        else:
            print("{:d}{:d}".format(x, y), end=', ')
