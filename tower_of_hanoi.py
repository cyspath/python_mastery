def move(n, a, c, b):
    if n > 0:
        move(n-1, a, b, c)
        print('move', n, 'to', c)
        move(n-1, b, c, a)


move(3, 'A', 'B', 'C')
