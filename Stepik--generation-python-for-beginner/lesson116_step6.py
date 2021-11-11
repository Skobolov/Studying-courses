# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список
# чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

lst_2 = input().split()
lst = []
for i in lst_2:
    lst.append(int(i))
min_i = lst.index(min(lst))
max_i = lst.index(max(lst))
lst[min_i], lst[max_i] = lst[max_i], lst[min_i]

print(*lst)
