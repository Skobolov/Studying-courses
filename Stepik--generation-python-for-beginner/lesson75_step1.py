# Напишем программу, которая определяет есть ли в числе цифра 7.

num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')