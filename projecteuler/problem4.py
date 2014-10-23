x, y = 999, 999
while True:
    if str(x*y) == str(x*y)[::-1]:
        print x*y
        break
    else:
        if y < 900:
            x = x - 1
            y = 999
        y = y - 1
