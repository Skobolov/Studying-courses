# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Sample Input 1:
#
# Москва
# Санкт-Петербург
# Екатеринбург
# Sample Output 1:
#
# Москва
# Санкт-Петербург


a, b, c = str(input()), str(input()), str(input())
print(min(a, b, c, key=len))
print(max(a, b, c, key=len))

