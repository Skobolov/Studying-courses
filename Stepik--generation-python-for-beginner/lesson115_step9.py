# На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.


lst = input().split()
d = 0

for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if int(lst[i]) == int(lst[j]):
            d += 1
print(d)