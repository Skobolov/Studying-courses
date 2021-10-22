# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит натуральное
# число из отрезка [a;b] с максимальной суммой делителей.

n = int(input())
m = int(input())
digit = 0
sum_digit = 0

for x in range(n, m + 1):
    sum2 = 0
    for i in range(1, x + 1):
        if x % i == 0:
            sum2 += i
    if sum2 >= sum_digit:
        sum_digit = sum2
        digit = x

print(digit, sum_digit)
