# Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3 состоящую из данного
# числа (числа отделены одним пробелом).

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 4):
        print(n, end=' ')
    print()