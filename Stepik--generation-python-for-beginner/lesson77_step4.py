# На обработку поступает последовательность из 1010 целых чисел. Известно, что вводимые числа по абсолютной величине
# не превышают 10**6. Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел
# последовательности и максимальное отрицательное число в последовательности. Если отрицательных чисел нет,
# требуется вывести на экран «NO».


mx = -10**6
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s == 0:
    print('NO')

else:
    print(s)
    print(mx)