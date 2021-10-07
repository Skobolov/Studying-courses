# Напишем программу, которая определяет есть ли в числе цифра 7.

num = int(input())
min_digit = 9
max_digit = 0

while num != 0:
    last_digit = num % 10
    if last_digit < min_digit:
        min_digit = last_digit
    if last_digit > max_digit:
        max_digit = last_digit
    num = num // 10

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
