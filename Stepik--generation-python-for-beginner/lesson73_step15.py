# Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.
# Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой
# двух предыдущих:   1, 1, 2, 3, 5, 8, 13,  21, 34, 55, 89,…

n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

# n = int(input())
# total1, total2, total3 = 0, 0, 0
#
# for i in range(1, n + 1):
#     if i == 1:
#         print(i, end=' ')
#         total3 = i
#     elif i == 2:
#         total2 = total3
#         print(total2, end=' ')
#     else:
#         total1 = total2 + total3
#         print(total1, end=' ')
#         total3 = total2
#         total2 = total1



