def draw_triangle(fill, base):
    for i in range(1, base + 1):
        r = 1
        k = round(base / 2)
        for i in range(1, k):
            print(r, end='')
            r += 1
        for j in range(k, 0, -1):
            print(r, end='')
            r -= 1

draw_triangle('*', 9)