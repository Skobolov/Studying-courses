# import pytest

# # d**e**f
# print('d', 'e', 'f', sep='**')

# # a b c@d e f@@
# print('a', 'b', 'c', end='@')
# print('d', 'e', 'f', end='@@')

# # abc
# print('a', 'b', 'c', sep='', end='')

# print(a, b, sep = '\n') # а и b выведутся на новых строках

# ** Возведение в степень
# % Остаток от деления
# // Целочисленное деление

# a = num % 10
# b = (num % 100) // 10
# c = num // 100

# a = (num // 10**3) % 10
# b = (num // 10**2) % 10
# c = (num // 10**1) % 10
# d = (num // 10**0) % 10

# n = int(input())
# a = n // 10000
# b = n % 10000 // 1000
# c = n % 1000 // 100
# d = n % 100 // 10
# e = n % 10

import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

from math import *

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)


# Строка
# s = (12345)
# print(s[::-1])  54321 - переворот строки

s = 'abcdefghijklmnopqrstuvwxyz'
# s = ''          # пустая строка
print(s[2])     # третий символ этой строки
print(s[-2])    # предпоследний символ этой строки
print(s[:5])    # первые пять символов этой строки
print(s[:-2])   # всю строку, кроме последних двух символов
print(s[0::2])  # все символы с четными индексами
print(s[1::2])  # все символы с нечетными индексами
print(s[::-1])  # все символы в обратном порядке
print(s[::-2])  # все символы строки через один в обратном порядке, начиная с последнего

s.capitalize()  # возвращает копию строки s, в которой первый символ имеет верхний регистр, а все остальные символы
                # имеют нижний регистр
s.swapcase()    # возвращает копию строки s, в которой все символы, имеющие верхний регистр, преобразуются в символы
                # нижнего регистра и наоборот
s.title()       # возвращает копию строки s, в которой первый символ каждого слова переводится в верхний регистр
s.lower()       # возвращает копию строки s, в которой все символы имеют нижний регистр
s.upper()       # возвращает копию строки s, в которой все символы имеют верхний регистр