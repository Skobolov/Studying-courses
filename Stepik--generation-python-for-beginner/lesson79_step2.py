# Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
# ...

n = int(input())
for x in range(1, n + 1):
    r = 1
    for i in range(1, x ):
        print(r, end='')
        r += 1
    for j in range(x, 0, -1):
        print(r, end='')
        r -=1
    print()


# n = int(input())
# for i in range(1, n + 1):
#     for k in range(1, i + 1, 1):
#         print(k, end='')
#     for l in range(i - 1, 0, -1):
#         print(l, end='')
#     print()