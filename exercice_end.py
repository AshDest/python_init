a, b, c = 3, 2, 1
while c < 15:
    print(c, ": ", b)
    a, b, c = b, a * b, c + 1
