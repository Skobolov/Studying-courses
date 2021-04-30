# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое
# на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

n = int(input())
count, total1, total2 = 0, 0, 0

for i in range(n):
    n = int(input())
    if n > total1:
        count += 1
        if count == 1:
            total2 = total1
            count = 0
            total1 = n
        else:
            total1 = n
    if n < total1:
        if n > total2:
            total2 = n
print(total1)
print(total2)

# n = int(input())
# max1, max2 = -1, -1
# for _ in range(n):
#     num = int(input())
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2:
#         max2 = num
# print(max1)
# print(max2)