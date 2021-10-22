# На вход программе подаются два числа, каждое на отдельной строке.
# Программа должна вывести все простые числа от a до b включительно, каждое на отдельной строке.
# Число 1 простым не является.

n = int(input())
m = int(input())

for i in range(n, m + 1):
    if i == 1:
        continue
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i)