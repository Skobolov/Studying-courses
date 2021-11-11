# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая для каждого
# введенного числа x выводит значение функции f(x) = x**2 + 2*x + 1, каждое на отдельной строке.


n = int(input())
num = []
num_2 = []

for _ in range(n):
    num.append(int(input()))
for i in num:
    num_2.append(i ** 2 + 2 * i + 1)

print(*num, sep='\n')
print()
print(*num_2, sep='\n')